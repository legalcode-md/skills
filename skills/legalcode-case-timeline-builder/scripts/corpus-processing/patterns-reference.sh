#!/usr/bin/env bash
# ==============================================================================
# patterns-reference.sh
#
# Self-contained reference of shell patterns for parallel document processing.
# Each section is independently copy-pasteable. This file is not meant to be
# executed as a whole; source individual functions or copy blocks as needed.
#
# Table of Contents:
#   1. Portable macOS/Linux shims
#   2. xargs -P patterns
#   3. GNU parallel patterns
#   4. Bash background job patterns
#   5. Error collection and retry
#   6. Progress tracking
#   7. Signal trapping and cleanup
#   8. Resume / skip-already-done
#   9. jq aggregation patterns
#  10. Cost-tracking integration patterns
#  11. Lock-free append patterns
#  12. Large-corpus streaming patterns
# ==============================================================================

# ============================================================
# 1. PORTABLE macOS / Linux SHIMS
# ============================================================
# Problem: stat, date, readlink, timeout, md5sum all differ between BSD and GNU.
# Solution: Write shim functions, test once, use everywhere.

_stat_size() {
    if stat --version >/dev/null 2>&1; then stat -c '%s' "$1"
    else stat -f '%z' "$1"; fi
}

_stat_mtime_epoch() {
    if stat --version >/dev/null 2>&1; then stat -c '%Y' "$1"
    else stat -f '%m' "$1"; fi
}

_iso_date_from_epoch() {
    if date --version >/dev/null 2>&1; then date -d "@$1" -u '+%Y-%m-%dT%H:%M:%SZ'
    else date -r "$1" -u '+%Y-%m-%dT%H:%M:%SZ'; fi
}

_sha256() {
    if command -v sha256sum >/dev/null 2>&1; then sha256sum "$1" | awk '{print $1}'
    else shasum -a 256 "$1" | awk '{print $1}'; fi
}

# Portable timeout: GNU coreutils `timeout` vs macOS perl fallback
_timeout() {
    local secs="$1"; shift
    if command -v timeout >/dev/null 2>&1; then
        timeout "$secs" "$@"
    else
        perl -e '
            $SIG{ALRM} = sub { kill 9, $pid; exit 124 };
            alarm shift @ARGV;
            $pid = fork;
            if ($pid == 0) { exec @ARGV; die "exec: $!" }
            waitpid($pid, 0);
            exit($? >> 8);
        ' "$secs" "$@"
    fi
}

# Portable readlink -f
_realpath() {
    if command -v realpath >/dev/null 2>&1; then realpath "$1"
    elif command -v grealpath >/dev/null 2>&1; then grealpath "$1"
    else python3 -c "import os,sys; print(os.path.realpath(sys.argv[1]))" "$1"; fi
}


# ============================================================
# 2. xargs -P PATTERNS
# ============================================================

# --- Pattern 2a: Simple N-at-a-time processing ---
# Process all .pdf files, 8 at a time, each with a 5-minute timeout
pattern_xargs_simple() {
    find ./documents -name '*.pdf' -print0 |
        xargs -0 -P 8 -I {} bash -c '
            echo "Processing: {}"
            _timeout 300 ./process-file.sh "{}" ./results/ || {
                echo "FAILED: {}" >> ./errors.log
            }
        '
}

# --- Pattern 2b: xargs from a file list (one path per line) ---
pattern_xargs_from_filelist() {
    local filelist="$1"
    local jobs="${2:-8}"

    cat "$filelist" |
        xargs -P "$jobs" -I {} bash -c '
            file_id="$(echo -n "{}" | shasum -a 256 | cut -c1-16)"
            ./processor.sh "{}" ./results "$file_id"
        '
}

# --- Pattern 2c: xargs with NUL delimiter (safe for spaces/special chars) ---
pattern_xargs_null_safe() {
    find ./documents -type f -print0 |
        xargs -0 -P 8 -n 1 ./processor.sh
    # Note: -n 1 means one argument per invocation (one file per process)
}

# --- Pattern 2d: xargs with progress via a named pipe ---
pattern_xargs_with_progress() {
    local total
    total="$(wc -l < filelist.txt | tr -d ' ')"
    local progress_pipe
    progress_pipe="$(mktemp -u)"
    mkfifo "$progress_pipe"

    # Background progress counter
    (
        local done=0
        while read -r line; do
            done=$((done + 1))
            printf '\r  Progress: %d / %d (%d%%)' "$done" "$total" "$((done * 100 / total))" >&2
        done < "$progress_pipe"
    ) &
    local progress_pid=$!

    # Process files; echo file path to pipe on completion
    cat filelist.txt | xargs -P 8 -I {} bash -c '
        ./processor.sh "{}" ./results "$(echo -n "{}" | shasum -a 256 | cut -c1-16)"
        echo "{}" > '"$progress_pipe"'
    '

    wait "$progress_pid" 2>/dev/null || true
    rm -f "$progress_pipe"
    echo "" >&2
}


# ============================================================
# 3. GNU parallel PATTERNS
# ============================================================

# --- Pattern 3a: Basic GNU parallel with job logging ---
pattern_parallel_basic() {
    parallel \
        --jobs 8 \
        --bar \
        --joblog ./joblog.tsv \
        ./processor.sh {} ./results {#} \
        :::: filelist.txt

    # {#} = job sequence number (useful as file ID)
    # --bar = progress bar to stderr
    # --joblog = tab-separated log of each job (start, end, exit code, signal, etc.)
}

# --- Pattern 3b: GNU parallel with retry and halt-on-failure ---
pattern_parallel_resilient() {
    parallel \
        --jobs 8 \
        --bar \
        --joblog ./joblog.tsv \
        --retries 3 \
        --timeout 300 \
        --halt soon,fail=5% \
        --resume-failed \
        --results ./parallel-output/ \
        ./processor.sh {} \
        :::: filelist.txt

    # --retries 3     = retry failed jobs up to 3 times
    # --timeout 300   = kill job after 300 seconds
    # --halt soon,fail=5%  = stop starting new jobs after 5% failure rate
    # --resume-failed = on re-run, only retry previously failed jobs
    # --results DIR   = save stdout/stderr per job to structured directory
}

# --- Pattern 3c: GNU parallel with structured output ---
pattern_parallel_structured() {
    # GNU parallel can capture stdout/stderr per job in a directory tree:
    parallel \
        --jobs 8 \
        --results ./output-tree/ \
        --joblog ./joblog.tsv \
        'echo {} | ./processor.sh' \
        :::: filelist.txt

    # Output tree: ./output-tree/1/<argnum>/stdout, stderr
    # Job log columns: Seq Host Starttime JobRuntime Send Receive Exitval Signal Command
}

# --- Pattern 3d: GNU parallel from CSV with multiple arguments ---
pattern_parallel_csv_input() {
    # Input CSV: filepath,category,priority
    parallel \
        --jobs 8 \
        --colsep ',' \
        --header : \
        --joblog ./joblog.tsv \
        './processor.sh {filepath} --category {category} --priority {priority}' \
        :::: input.csv
}


# ============================================================
# 4. BASH BACKGROUND JOB PATTERNS
# ============================================================

# --- Pattern 4a: Simple throttled background jobs ---
pattern_background_throttled() {
    local max_jobs=8
    local active=0

    while IFS= read -r filepath; do
        ./processor.sh "$filepath" ./results &
        active=$((active + 1))

        if [[ $active -ge $max_jobs ]]; then
            wait -n  # Wait for any ONE job to finish (bash 4.3+)
            active=$((active - 1))
        fi
    done < filelist.txt

    wait  # Wait for all remaining
}

# --- Pattern 4b: Background jobs with exit code collection ---
pattern_background_with_errors() {
    local max_jobs=8
    declare -A running_pids  # PID -> filepath mapping (requires bash 4+)

    failed_files=()

    while IFS= read -r filepath; do
        # Throttle
        while [[ ${#running_pids[@]} -ge $max_jobs ]]; do
            for pid in "${!running_pids[@]}"; do
                if ! kill -0 "$pid" 2>/dev/null; then
                    wait "$pid" || failed_files+=("${running_pids[$pid]}")
                    unset "running_pids[$pid]"
                fi
            done
            [[ ${#running_pids[@]} -ge $max_jobs ]] && sleep 0.1
        done

        ./processor.sh "$filepath" ./results &
        running_pids[$!]="$filepath"

    done < filelist.txt

    # Drain remaining
    for pid in "${!running_pids[@]}"; do
        wait "$pid" || failed_files+=("${running_pids[$pid]}")
    done

    if [[ ${#failed_files[@]} -gt 0 ]]; then
        echo "Failed files:" >&2
        printf '  %s\n' "${failed_files[@]}" >&2
    fi
}

# --- Pattern 4c: Background jobs with FIFO semaphore (no wait -n needed) ---
# Works on bash 3.x (macOS default)
pattern_background_fifo_semaphore() {
    local max_jobs=8
    local fifo
    fifo="$(mktemp -u)"
    mkfifo "$fifo"

    # Pre-fill the FIFO with N tokens
    exec 3<>"$fifo"
    for ((i = 0; i < max_jobs; i++)); do
        echo >&3
    done

    while IFS= read -r filepath; do
        read -u 3  # Block until a token is available (a slot is free)

        (
            ./processor.sh "$filepath" ./results
            echo >&3  # Return the token when done
        ) &
    done < filelist.txt

    wait
    exec 3>&-
    rm -f "$fifo"
}


# ============================================================
# 5. ERROR COLLECTION AND RETRY
# ============================================================

# --- Pattern 5a: Retry with exponential backoff ---
retry_with_backoff() {
    local cmd="$1"
    local max_retries="${2:-3}"
    local attempt=0

    while [[ $attempt -lt $max_retries ]]; do
        attempt=$((attempt + 1))
        if eval "$cmd"; then
            return 0
        fi
        local wait_time=$((1 << (attempt - 1)))  # 1, 2, 4, 8 ...
        echo "  Attempt $attempt failed, retrying in ${wait_time}s..." >&2
        sleep "$wait_time"
    done

    echo "  All $max_retries attempts failed" >&2
    return 1
}

# Usage: retry_with_backoff "./processor.sh /path/to/file" 3

# --- Pattern 5b: Collect errors to a structured log ---
pattern_error_collector() {
    local error_log="./errors.jsonl"
    : > "$error_log"

    process_with_error_logging() {
        local filepath="$1"
        local file_id="$2"
        local exit_code=0

        local stderr_capture
        stderr_capture="$(mktemp)"

        ./processor.sh "$filepath" ./results "$file_id" 2>"$stderr_capture" || exit_code=$?

        if [[ $exit_code -ne 0 ]]; then
            local stderr_content
            stderr_content="$(cat "$stderr_capture" | head -c 1000)"
            jq -n -c \
                --arg file "$filepath" \
                --arg id "$file_id" \
                --argjson code "$exit_code" \
                --arg stderr "$stderr_content" \
                --arg ts "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
                '{ file: $file, id: $id, exit_code: $code, stderr: $stderr, timestamp: $ts }' \
                >> "$error_log"
        fi

        rm -f "$stderr_capture"
        return $exit_code
    }

    # Use in xargs:
    export -f process_with_error_logging
    cat filelist.txt | xargs -P 8 -I {} bash -c 'process_with_error_logging "{}" "$(echo -n "{}" | shasum -a 256 | cut -c1-16)"'
}

# --- Pattern 5c: Retry failed files from error log ---
pattern_retry_from_errors() {
    local error_log="./errors.jsonl"

    if [[ ! -f "$error_log" ]]; then
        echo "No error log found" >&2
        return 0
    fi

    local retry_count
    retry_count="$(wc -l < "$error_log" | tr -d ' ')"
    echo "Retrying $retry_count failed files..." >&2

    jq -r '.file' "$error_log" | xargs -P 4 -I {} bash -c '
        file_id="$(echo -n "{}" | shasum -a 256 | cut -c1-16)"
        ./processor.sh "{}" ./results "$file_id"
    '
}


# ============================================================
# 6. PROGRESS TRACKING
# ============================================================

# --- Pattern 6a: Atomic counter file ---
pattern_progress_atomic() {
    local total="$1"
    local counter_file="./progress_count"
    echo "0" > "$counter_file"

    increment_progress() {
        # Portable atomic-ish increment (flock on Linux, no-lock on macOS)
        if command -v flock >/dev/null 2>&1; then
            flock "$counter_file.lock" bash -c "
                n=\$(cat '$counter_file'); n=\$((n+1)); echo \$n > '$counter_file'
                printf '\rProgress: %d / $total (%d%%)' \$n \$((\$n * 100 / $total)) >&2
            "
        else
            # macOS: accept occasional miscount on display (results are still correct)
            local n
            n="$(cat "$counter_file")"
            n=$((n + 1))
            echo "$n" > "$counter_file"
            printf '\rProgress: %d / %d (%d%%)' "$n" "$total" "$((n * 100 / total))" >&2
        fi
    }
    export -f increment_progress
}

# --- Pattern 6b: ETA estimation ---
pattern_eta() {
    local total="$1"
    local start_time="$2"  # epoch
    local done="$3"

    if [[ "$done" -eq 0 ]]; then
        echo "ETA: calculating..."
        return
    fi

    local now
    now="$(date +%s)"
    local elapsed=$((now - start_time))
    local rate  # files per second
    rate="$(echo "scale=2; $done / $elapsed" | bc 2>/dev/null || echo "0")"
    local remaining=$((total - done))
    local eta_seconds
    eta_seconds="$(echo "scale=0; $remaining / $rate" | bc 2>/dev/null || echo "?")"

    if [[ "$eta_seconds" == "?" ]]; then
        echo "ETA: unknown"
    elif [[ "$eta_seconds" -lt 60 ]]; then
        echo "ETA: ${eta_seconds}s"
    elif [[ "$eta_seconds" -lt 3600 ]]; then
        echo "ETA: $((eta_seconds / 60))m $((eta_seconds % 60))s"
    else
        echo "ETA: $((eta_seconds / 3600))h $((eta_seconds % 3600 / 60))m"
    fi
}


# ============================================================
# 7. SIGNAL TRAPPING AND CLEANUP
# ============================================================

# --- Pattern 7a: Comprehensive trap setup ---
pattern_signal_handling() {
    TEMP_FILES=()
    CHILD_PIDS=()

    cleanup() {
        local exit_code="${1:-1}"
        echo "" >&2
        echo "Cleaning up (exit=$exit_code)..." >&2

        # Kill child processes
        for pid in "${CHILD_PIDS[@]+"${CHILD_PIDS[@]}"}"; do
            kill "$pid" 2>/dev/null || true
        done

        # Remove temp files
        for f in "${TEMP_FILES[@]+"${TEMP_FILES[@]}"}"; do
            rm -f "$f" 2>/dev/null || true
        done

        # Write state for resume
        echo "$exit_code" > ./.last-exit-code

        exit "$exit_code"
    }

    trap 'cleanup $?' EXIT
    trap 'echo "Interrupted (SIGINT)" >&2; exit 130' INT
    trap 'echo "Terminated (SIGTERM)" >&2; exit 143' TERM

    # Usage: register temp files and PIDs
    tmpfile="$(mktemp)"
    TEMP_FILES+=("$tmpfile")

    some_command &
    CHILD_PIDS+=($!)
}


# ============================================================
# 8. RESUME / SKIP-ALREADY-DONE
# ============================================================

# --- Pattern 8a: Skip files with existing results ---
pattern_resume_by_results() {
    local results_dir="./results"
    local filelist="./filelist.txt"
    local remaining
    remaining="$(mktemp)"

    while IFS= read -r filepath; do
        file_id="$(echo -n "$filepath" | shasum -a 256 | cut -c1-16)"
        if [[ ! -f "$results_dir/${file_id}.json" ]]; then
            echo "$filepath" >> "$remaining"
        fi
    done < "$filelist"

    local total
    total="$(wc -l < "$filelist" | tr -d ' ')"
    local todo
    todo="$(wc -l < "$remaining" | tr -d ' ')"
    echo "Resume: $((total - todo)) already done, $todo remaining" >&2

    # Process only remaining files
    cat "$remaining" | xargs -P 8 -I {} ./processor.sh "{}" "$results_dir"
    rm -f "$remaining"
}

# --- Pattern 8b: Checkpoint file with stage tracking ---
pattern_checkpoint() {
    local checkpoint_file="./.checkpoint"

    save_checkpoint() {
        jq -n \
            --arg stage "$1" \
            --arg ts "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
            --argjson last_index "${2:-0}" \
            '{ stage: $stage, timestamp: $ts, last_processed_index: $last_index }' \
            > "$checkpoint_file"
    }

    load_checkpoint() {
        if [[ -f "$checkpoint_file" ]]; then
            jq -r '.stage' "$checkpoint_file"
        else
            echo "none"
        fi
    }

    get_last_index() {
        if [[ -f "$checkpoint_file" ]]; then
            jq -r '.last_processed_index' "$checkpoint_file"
        else
            echo "0"
        fi
    }

    # Usage in pipeline (sequential stages, skip completed ones):
    local stage
    stage="$(load_checkpoint)"

    if [[ "$stage" == "none" || "$stage" == "discovery" ]]; then
        echo "Running discovery..."
        # ... discovery logic ...
        save_checkpoint "discovery" 0
        stage="discovery"
    fi

    if [[ "$stage" == "discovery" || "$stage" == "processing" ]]; then
        local start_idx
        start_idx="$(get_last_index)"
        echo "Running processing from index $start_idx..."
        # ... processing logic, periodically: save_checkpoint "processing" $current_idx ...
        save_checkpoint "processing_done" 0
        stage="processing_done"
    fi

    if [[ "$stage" == "processing_done" || "$stage" == "aggregation" ]]; then
        echo "Running aggregation..."
        # ... aggregation logic ...
        save_checkpoint "complete" 0
        stage="complete"
    fi

    if [[ "$stage" == "complete" ]]; then
        echo "Pipeline already complete."
    fi
}


# ============================================================
# 9. jq AGGREGATION PATTERNS
# ============================================================

# --- Pattern 9a: Merge JSON files into array ---
pattern_jq_merge_simple() {
    # Slurp all JSON files in a directory into a single array
    jq -s '.' ./results/*.json > consolidated.json
}

# --- Pattern 9b: Merge with deduplication ---
pattern_jq_dedup() {
    jq -s '
        [group_by(.file)[] | first]
    ' ./results/*.json > consolidated.json
}

# --- Pattern 9c: Merge and sort ---
pattern_jq_sort() {
    jq -s '
        sort_by(.risk_score) | reverse
    ' ./results/*.json > consolidated.json
}

# --- Pattern 9d: Generate summary statistics ---
pattern_jq_summary() {
    jq -s '
    {
        total: length,
        by_status: (group_by(.status) | map({key: .[0].status, value: length}) | from_entries),
        by_category: (group_by(.category) | map({key: .[0].category, value: length}) | from_entries),
        risk_stats: {
            scores: [.[].risk_score | select(. != null)],
            min: ([.[].risk_score | select(. != null)] | min),
            max: ([.[].risk_score | select(. != null)] | max),
            avg: ([.[].risk_score | select(. != null)] | add / length)
        }
    }' ./results/*.json
}

# --- Pattern 9e: Streaming merge for very large result sets ---
# When you have 100k+ JSON files, jq -s will run out of memory.
# Use this streaming approach instead.
pattern_jq_streaming_merge() {
    local results_dir="$1"
    local output="$2"

    echo "[" > "$output"
    local first=true
    for f in "$results_dir"/*.json; do
        if [[ "$first" == true ]]; then
            first=false
        else
            echo "," >> "$output"
        fi
        cat "$f" >> "$output"
    done
    echo "]" >> "$output"

    echo "Merged $(ls "$results_dir"/*.json | wc -l | tr -d ' ') files" >&2
}

# --- Pattern 9f: JSONL for streaming consumers ---
pattern_jsonl_output() {
    # Convert per-file results to one JSON object per line
    for f in ./results/*.json; do
        jq -c '.' "$f"
    done > results.jsonl
}

# --- Pattern 9g: Combine array + summary into final report ---
pattern_jq_full_report() {
    local results_dir="$1"
    local manifest="$2"

    jq -n \
        --arg ts "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
        --slurpfile results <(jq -s '.' "$results_dir"/*.json) \
        --slurpfile manifest "$manifest" \
        '{
            report: {
                generated_at: $ts,
                manifest_files: ($manifest[0].manifest.total_files // ($manifest[0].files | length)),
                processed_files: ($results[0] | length),
                completion_pct: (
                    ($results[0] | length) /
                    ($manifest[0].manifest.total_files // ($manifest[0].files | length)) * 100 |
                    . * 10 | round / 10
                )
            },
            summary: ($results[0] | {
                total: length,
                by_status: (group_by(.status) | map({key: .[0].status, value: length}) | from_entries)
            }),
            results: $results[0]
        }'
}


# ============================================================
# 10. COST-TRACKING INTEGRATION PATTERNS
# ============================================================

# --- Pattern 10a: Inline cost tracking per file ---
pattern_cost_inline() {
    local cost_file="./costs.jsonl"
    : > "$cost_file"

    process_and_track_cost() {
        local filepath="$1"
        local start_time
        start_time="$(date +%s)"

        # Process and capture token usage from API response
        local response
        response="$(call_api "$filepath")"

        local input_tokens output_tokens
        input_tokens="$(echo "$response" | jq '.usage.input_tokens // 0')"
        output_tokens="$(echo "$response" | jq '.usage.output_tokens // 0')"

        # Calculate cost
        local cost
        cost="$(echo "scale=6; $input_tokens * 0.015 / 1000 + $output_tokens * 0.075 / 1000" | bc)"

        local end_time
        end_time="$(date +%s)"

        # Append to cost log (JSONL for lock-free parallel append)
        jq -n -c \
            --arg file "$filepath" \
            --argjson in "$input_tokens" \
            --argjson out "$output_tokens" \
            --argjson cost "$cost" \
            --argjson dur "$((end_time - start_time))" \
            '{ file: $file, tokens_in: $in, tokens_out: $out, cost: $cost, duration: $dur }' \
            >> "$cost_file"
    }
}

# --- Pattern 10b: Budget gate in xargs pipeline ---
pattern_budget_gate() {
    local budget=50.00
    local cost_file="./costs.jsonl"

    check_budget_inline() {
        if [[ ! -f "$cost_file" ]]; then return 0; fi
        local total_cost
        total_cost="$(jq -s '[.[].cost] | add // 0' "$cost_file")"
        local exceeded
        exceeded="$(echo "$total_cost >= $budget" | bc 2>/dev/null || echo "0")"
        if [[ "$exceeded" == "1" ]]; then
            echo "BUDGET EXCEEDED: \$$total_cost >= \$$budget" >&2
            return 1
        fi
        return 0
    }

    # Wrap each file processing with budget check:
    # (The budget check introduces a serial bottleneck, so check every N files)
    local check_interval=10
    local counter=0

    while IFS= read -r filepath; do
        counter=$((counter + 1))
        if [[ $((counter % check_interval)) -eq 0 ]]; then
            check_budget_inline || break
        fi
        echo "$filepath"
    done < filelist.txt | xargs -P 8 -I {} ./processor.sh "{}"
}


# ============================================================
# 11. LOCK-FREE APPEND PATTERNS
# ============================================================
# When multiple parallel processes write to the same file, you need to ensure
# writes are atomic. JSONL (one JSON per line) is ideal for this.

# --- Pattern 11a: JSONL append (atomic on POSIX for lines < PIPE_BUF) ---
pattern_lockfree_jsonl() {
    # POSIX guarantees atomic writes for sizes <= PIPE_BUF (typically 4096 bytes).
    # A single jq -c output is almost always under this limit.

    local output="./results.jsonl"

    append_result() {
        # This is safe for parallel append (no lock needed)
        jq -n -c --arg f "$1" --arg s "$2" '{ file: $f, status: $s }' >> "$output"
    }
}

# --- Pattern 11b: Per-file output (no contention) ---
# The simplest pattern: each process writes to its own file.
# Merge at the end. Zero contention, zero corruption risk.
pattern_per_file_output() {
    process_file() {
        local filepath="$1"
        local results_dir="$2"
        local file_id
        file_id="$(echo -n "$filepath" | shasum -a 256 | cut -c1-16)"

        # Each process writes its own file -- no contention
        jq -n --arg f "$filepath" '{ file: $f, status: "ok" }' \
            > "$results_dir/${file_id}.json"
    }
}


# ============================================================
# 12. LARGE-CORPUS STREAMING PATTERNS
# ============================================================

# --- Pattern 12a: Process in batches ---
pattern_batch_processing() {
    local batch_size=1000
    local batch_num=0
    local filelist="./filelist.txt"
    local total
    total="$(wc -l < "$filelist" | tr -d ' ')"

    while true; do
        local offset=$((batch_num * batch_size))
        if [[ $offset -ge $total ]]; then break; fi

        local batch_file
        batch_file="$(mktemp)"
        tail -n "+$((offset + 1))" "$filelist" | head -n "$batch_size" > "$batch_file"

        local batch_count
        batch_count="$(wc -l < "$batch_file" | tr -d ' ')"
        echo "Processing batch $batch_num ($batch_count files, offset $offset)..." >&2

        cat "$batch_file" | xargs -P 8 -I {} ./processor.sh "{}" ./results
        rm -f "$batch_file"

        # Budget check between batches
        # ./05-cost-tracker.sh check || { echo "Budget exceeded after batch $batch_num" >&2; break; }

        batch_num=$((batch_num + 1))
    done
}

# --- Pattern 12b: Split file list for independent workers ---
pattern_split_workers() {
    local filelist="$1"
    local num_workers="${2:-4}"
    local split_dir
    split_dir="$(mktemp -d)"

    # Split file list into N chunks
    split -n "l/$num_workers" "$filelist" "$split_dir/chunk_"

    # Launch one worker per chunk
    local pids=()
    for chunk in "$split_dir"/chunk_*; do
        (
            while IFS= read -r filepath; do
                ./processor.sh "$filepath" ./results
            done < "$chunk"
        ) &
        pids+=($!)
    done

    # Wait for all workers
    for pid in "${pids[@]}"; do
        wait "$pid"
    done

    rm -rf "$split_dir"
}
