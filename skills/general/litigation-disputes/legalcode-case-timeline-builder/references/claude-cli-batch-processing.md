# Claude Code CLI (`claude -p`) Batch Processing Research

> Research date: 2026-02-28
> Sources: https://code.claude.com/docs/en/cli-reference.md, https://code.claude.com/docs/en/headless.md, https://code.claude.com/docs/en/common-workflows.md, https://platform.claude.com/docs/en/agent-sdk/overview, https://platform.claude.com/docs/en/agent-sdk/structured-outputs

---

## 1. The `-p` (Print / SDK) Mode

The `-p` flag (alias `--print`) runs Claude Code **non-interactively**: it accepts a prompt, executes the agentic loop (reading files, running commands, etc.), prints the result, and exits. This is the foundation for all scripting and batch work.

```bash
# Basic non-interactive query
claude -p "Explain the auth module"

# With an initial prompt passed as a positional argument
claude -p "What does this function do?"
```

Key behavior:

- Claude runs autonomously -- it can read files, run Bash, grep, etc. just like interactive mode.
- When it finishes (or hits a limit), it prints the result and exits with a status code.
- Skills/slash-commands (like `/commit`) are NOT available in `-p` mode. Describe the task in prose instead.

---

## 2. Complete Flag Reference (Relevant to Batch Processing)

### Core Flags

| Flag                             | Description                                                              | Example                                                   |
| -------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------- |
| `-p`, `--print`                  | Non-interactive mode. Exits after responding.                            | `claude -p "query"`                                       |
| `--model`                        | Set model. Accepts alias (`sonnet`, `opus`, `haiku`) or full name.       | `claude -p --model sonnet "query"`                        |
| `--output-format`                | Output format: `text` (default), `json`, `stream-json`                   | `claude -p --output-format json "query"`                  |
| `--max-turns`                    | Limit agentic turns. Exits with error when reached. No limit by default. | `claude -p --max-turns 3 "query"`                         |
| `--max-budget-usd`               | Cap dollar spend per invocation. Print mode only.                        | `claude -p --max-budget-usd 0.50 "query"`                 |
| `--json-schema`                  | Get validated JSON output matching a JSON Schema.                        | `claude -p --json-schema '{"type":"object",...}' "query"` |
| `--allowedTools`                 | Auto-approve specific tools (no permission prompts).                     | `claude -p --allowedTools "Read,Bash,Glob" "query"`       |
| `--disallowedTools`              | Remove tools entirely from context.                                      | `claude -p --disallowedTools "Edit,Write" "query"`        |
| `--tools`                        | Restrict available tools. `""` disables all, `"default"` enables all.    | `claude -p --tools "Read,Grep,Glob" "query"`              |
| `--dangerously-skip-permissions` | Skip ALL permission prompts.                                             | `claude -p --dangerously-skip-permissions "query"`        |
| `--permission-mode`              | Set permission mode: `plan` (read-only), etc.                            | `claude -p --permission-mode plan "query"`                |
| `--no-session-persistence`       | Don't save session to disk. Print mode only.                             | `claude -p --no-session-persistence "query"`              |
| `--fallback-model`               | Auto-fallback when primary model is overloaded. Print mode only.         | `claude -p --fallback-model sonnet "query"`               |
| `--verbose`                      | Show full turn-by-turn output.                                           | `claude -p --verbose "query"`                             |

### System Prompt Flags

| Flag                               | Behavior                                    | Modes               |
| ---------------------------------- | ------------------------------------------- | ------------------- |
| `--system-prompt "text"`           | **Replaces** entire default prompt          | Interactive + Print |
| `--system-prompt-file path`        | **Replaces** with file contents             | Print only          |
| `--append-system-prompt "text"`    | **Appends** to default prompt               | Interactive + Print |
| `--append-system-prompt-file path` | **Appends** file contents to default prompt | Print only          |

`--system-prompt` and `--system-prompt-file` are mutually exclusive.
`--append-*` flags can combine with either replacement flag.

### Session Flags

| Flag                | Description                              | Example                                                    |
| ------------------- | ---------------------------------------- | ---------------------------------------------------------- |
| `-c`, `--continue`  | Continue most recent conversation in cwd | `claude -c -p "follow up"`                                 |
| `-r`, `--resume ID` | Resume specific session by ID or name    | `claude -r "session-name" -p "continue"`                   |
| `--session-id UUID` | Use a specific session UUID              | `claude --session-id "550e8400-..." -p "query"`            |
| `--fork-session`    | Fork when resuming (new session ID)      | `claude -r abc --fork-session -p "try different approach"` |

### Other Useful Flags

| Flag                    | Description                         |
| ----------------------- | ----------------------------------- |
| `--add-dir path`        | Add additional working directories  |
| `--mcp-config path`     | Load MCP servers from JSON config   |
| `--agent name`          | Use a specific agent                |
| `--agents JSON`         | Define subagents dynamically        |
| `-w`, `--worktree name` | Start in isolated git worktree      |
| `--debug "category"`    | Debug logging (e.g., `"api,hooks"`) |

---

## 3. Piping Content via stdin

You can pipe file content (or any text) into `claude -p` via stdin. Claude receives the piped content as context alongside your prompt.

```bash
# Pipe a file and ask a question about it
cat contract.txt | claude -p "Extract all dates mentioned in this document"

# Pipe command output
git diff HEAD~5 | claude -p "Summarize these changes"

# Pipe and redirect output
cat build-error.txt | claude -p "Explain the root cause of this build error" > diagnosis.txt

# Pipe a PR diff for security review
gh pr diff 42 | claude -p \
  --append-system-prompt "You are a security engineer. Review for vulnerabilities." \
  --output-format json
```

---

## 4. JSON Output Format

### `--output-format text` (default)

Returns plain text -- just the final response.

### `--output-format json`

Returns a JSON object with metadata. Key fields:

| Field               | Type        | Description                                                               |
| ------------------- | ----------- | ------------------------------------------------------------------------- |
| `result`            | string      | The text response from Claude                                             |
| `session_id`        | string      | UUID for the session (use with `--resume` for follow-ups)                 |
| `structured_output` | object/null | Present when `--json-schema` is used; validated JSON matching your schema |
| `subtype`           | string      | `"success"` or `"error_max_structured_output_retries"`                    |

Extract the text result with `jq`:

```bash
claude -p "Summarize this project" --output-format json | jq -r '.result'
```

Extract structured output:

```bash
claude -p "Extract function names from auth.py" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"functions":{"type":"array","items":{"type":"string"}}},"required":["functions"]}' \
  | jq '.structured_output'
```

Capture session ID for follow-up:

```bash
session_id=$(claude -p "Start a review" --output-format json | jq -r '.session_id')
claude -p "Continue that review" --resume "$session_id"
```

### `--output-format stream-json`

Returns newline-delimited JSON objects in real-time as Claude processes. Each line is a valid JSON object, but the entire output is NOT valid JSON if concatenated.

```bash
# Stream tokens as they arrive
claude -p "Write a poem" \
  --output-format stream-json \
  --verbose \
  --include-partial-messages | \
  jq -rj 'select(.type == "stream_event" and .event.delta.type? == "text_delta") | .event.delta.text'
```

### `--json-schema` for Validated Structured Output

Forces Claude to return JSON matching your schema. The result appears in the `structured_output` field of the JSON response.

```bash
claude -p "Analyze this contract for key dates and parties" \
  --output-format json \
  --json-schema '{
    "type": "object",
    "properties": {
      "parties": {"type": "array", "items": {"type": "string"}},
      "effective_date": {"type": "string"},
      "termination_date": {"type": "string"},
      "governing_law": {"type": "string"}
    },
    "required": ["parties", "effective_date"]
  }'
```

---

## 5. Parallel Execution Patterns

### Pattern A: `xargs -P` (Simplest)

Run N files in parallel, each processed by a separate `claude -p` instance:

```bash
# Process 4 files at a time in parallel
ls contracts/*.txt | xargs -P 4 -I {} sh -c '
  cat "{}" | claude -p \
    --model sonnet \
    --max-budget-usd 0.25 \
    --output-format json \
    --no-session-persistence \
    "Extract all dates, parties, and governing law from this contract" \
    > "results/$(basename {} .txt).json"
'
```

With `find` for recursive discovery:

```bash
find ./docs -name "*.md" -type f | xargs -P 8 -I {} sh -c '
  outfile="results/$(echo "{}" | sed "s|/|__|g").json"
  cat "{}" | claude -p \
    --model sonnet \
    --max-budget-usd 0.10 \
    --output-format json \
    --no-session-persistence \
    "Summarize this document in 3 bullet points" \
    > "$outfile"
'
```

### Pattern B: GNU `parallel` (More Robust)

GNU parallel provides better job control, progress reporting, and error handling:

```bash
# Install: brew install parallel (macOS) or apt install parallel (Linux)

# Process all contracts with 6 parallel jobs, show progress
find contracts/ -name "*.txt" | parallel -j 6 --bar '
  cat {} | claude -p \
    --model sonnet \
    --max-budget-usd 0.25 \
    --output-format json \
    --no-session-persistence \
    "Extract key terms from this contract" \
    > results/{/.}.json
'
```

GNU parallel placeholders:

- `{}` = full path
- `{.}` = path without extension
- `{/}` = basename
- `{/.}` = basename without extension
- `{//}` = directory

With structured output and retry:

```bash
find contracts/ -name "*.pdf" | parallel -j 4 --retries 2 --joblog joblog.txt '
  claude -p \
    --model sonnet \
    --max-budget-usd 0.50 \
    --output-format json \
    --no-session-persistence \
    --json-schema '"'"'{"type":"object","properties":{"risk_level":{"type":"string","enum":["low","medium","high"]},"issues":{"type":"array","items":{"type":"string"}},"summary":{"type":"string"}},"required":["risk_level","summary"]}'"'"' \
    "Read and analyze the contract at {}" \
    > results/{/.}.json
'
```

Review the joblog for failures:

```bash
# joblog.txt columns: Seq Host Starttime JobRuntime Send Receive Exitval Signal Command
awk '$7 != 0' joblog.txt  # Show failed jobs
```

### Pattern C: Bash Background Jobs with `wait`

For simple cases where you want explicit control:

```bash
#!/usr/bin/env bash
set -euo pipefail

MAX_PARALLEL=4
results_dir="./results"
mkdir -p "$results_dir"

# Track background PIDs
pids=()

for file in contracts/*.txt; do
    # Wait if we have MAX_PARALLEL jobs running
    while [ ${#pids[@]} -ge $MAX_PARALLEL ]; do
        # Wait for any one job to finish
        wait -n 2>/dev/null || true
        # Clean up finished PIDs
        new_pids=()
        for pid in "${pids[@]}"; do
            if kill -0 "$pid" 2>/dev/null; then
                new_pids+=("$pid")
            fi
        done
        pids=("${new_pids[@]}")
    done

    basename=$(basename "$file" .txt)
    (
        cat "$file" | claude -p \
            --model sonnet \
            --max-budget-usd 0.25 \
            --output-format json \
            --no-session-persistence \
            "Triage this NDA. Classify as GREEN, YELLOW, or RED." \
            > "$results_dir/${basename}.json" 2>"$results_dir/${basename}.err"
    ) &
    pids+=($!)
    echo "Started processing: $file (PID: $!)"
done

# Wait for all remaining jobs
wait
echo "All files processed."
```

### Pattern D: Full Batch Script with Aggregation

A complete script that processes files, handles errors, and aggregates results:

```bash
#!/usr/bin/env bash
set -euo pipefail

INPUT_DIR="${1:?Usage: $0 <input-dir>}"
RESULTS_DIR="./batch-results"
PARALLEL_JOBS=6
MAX_COST_PER_FILE=0.25
MODEL="sonnet"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

mkdir -p "$RESULTS_DIR"

SCHEMA='{
  "type": "object",
  "properties": {
    "classification": {
      "type": "string",
      "enum": ["GREEN", "YELLOW", "RED"]
    },
    "confidence": { "type": "number" },
    "key_issues": {
      "type": "array",
      "items": { "type": "string" }
    },
    "summary": { "type": "string" }
  },
  "required": ["classification", "confidence", "summary"]
}'

PROMPT="You are a contract triage specialist. Analyze this document and classify it:
- GREEN: Standard terms, no significant risk
- YELLOW: Non-standard terms requiring review
- RED: High-risk terms requiring immediate attention
Identify key issues and provide a confidence score (0-1)."

echo "=== Batch Processing Started: $TIMESTAMP ==="
echo "Input: $INPUT_DIR"
echo "Parallelism: $PARALLEL_JOBS"
echo "Max cost per file: \$$MAX_COST_PER_FILE"
echo ""

# Process all files in parallel
find "$INPUT_DIR" -type f \( -name "*.txt" -o -name "*.md" -o -name "*.pdf" \) \
  | parallel -j "$PARALLEL_JOBS" --bar --joblog "$RESULTS_DIR/joblog_${TIMESTAMP}.txt" '
    outfile="'"$RESULTS_DIR"'/{/.}_'"$TIMESTAMP"'.json"
    cat {} | claude -p \
      --model '"$MODEL"' \
      --max-budget-usd '"$MAX_COST_PER_FILE"' \
      --output-format json \
      --no-session-persistence \
      --json-schema '"'"'"$SCHEMA"'"'"' \
      "'"$PROMPT"'" \
      > "$outfile" 2>"$outfile.err"

    # Check if the output is valid JSON
    if ! jq empty "$outfile" 2>/dev/null; then
      echo "WARN: Invalid JSON output for {}" >&2
    fi
  '

echo ""
echo "=== Aggregating Results ==="

# Aggregate all results into a single JSON array
jq -s '[.[] | {
  file: input_filename,
  classification: .structured_output.classification,
  confidence: .structured_output.confidence,
  summary: .structured_output.summary,
  issues: .structured_output.key_issues
}]' "$RESULTS_DIR"/*_${TIMESTAMP}.json > "$RESULTS_DIR/aggregate_${TIMESTAMP}.json"

# Print summary
echo ""
echo "=== Summary ==="
jq -r '
  "Total files: \(length)",
  "GREEN: \([.[] | select(.classification == "GREEN")] | length)",
  "YELLOW: \([.[] | select(.classification == "YELLOW")] | length)",
  "RED: \([.[] | select(.classification == "RED")] | length)",
  "",
  "RED items requiring attention:",
  (.[] | select(.classification == "RED") | "  - \(.file): \(.summary)")
' "$RESULTS_DIR/aggregate_${TIMESTAMP}.json"

# Show any failures from joblog
failed=$(awk 'NR>1 && $7 != 0 {print $0}' "$RESULTS_DIR/joblog_${TIMESTAMP}.txt" | wc -l | tr -d ' ')
if [ "$failed" -gt 0 ]; then
    echo ""
    echo "WARNING: $failed file(s) failed processing. Check joblog for details:"
    echo "  $RESULTS_DIR/joblog_${TIMESTAMP}.txt"
fi
```

---

## 6. Cost Control

### Per-Invocation Budget Cap

```bash
# Hard limit: stop if cost exceeds $0.50
claude -p --max-budget-usd 0.50 "Analyze this codebase"
```

When the budget is exceeded, Claude stops and exits. The response up to that point is still returned.

### Turn Limits

```bash
# Limit to 3 agentic turns (read/execute/respond cycles)
claude -p --max-turns 3 "Review this file"
```

Exits with an error when the limit is reached. Use this to prevent runaway loops.

### Model Selection for Cost

```bash
# Use Haiku (cheapest) for simple extraction
claude -p --model haiku "Extract the title from this document"

# Use Sonnet (mid-range) for analysis
claude -p --model sonnet "Review this contract for risks"

# Use Opus (most capable, most expensive) for complex reasoning
claude -p --model opus "Draft a comprehensive legal analysis"
```

### Combining Cost Controls

```bash
claude -p \
  --model sonnet \
  --max-turns 5 \
  --max-budget-usd 0.25 \
  --no-session-persistence \
  "Analyze this contract"
```

### Estimating Batch Costs

```bash
# Count files first
file_count=$(find contracts/ -name "*.txt" | wc -l)
max_per_file=0.25
echo "Max batch cost: \$$(echo "$file_count * $max_per_file" | bc)"

# Then run
find contracts/ -name "*.txt" | parallel -j 4 '
  cat {} | claude -p --model sonnet --max-budget-usd 0.25 --output-format json \
    "Analyze this contract" > results/{/.}.json
'
```

---

## 7. Error Handling

### Exit Codes

Claude CLI uses standard exit codes:

- `0` = success
- Non-zero = error (tool failure, budget exceeded, max turns exceeded, etc.)

### Checking Exit Codes in Scripts

```bash
if ! output=$(cat contract.txt | claude -p \
    --model sonnet \
    --max-budget-usd 0.25 \
    --output-format json \
    "Analyze this contract" 2>error.log); then
    echo "FAILED: $(cat error.log)" >&2
    exit 1
fi
echo "$output" > result.json
```

### Retry Pattern

```bash
process_file() {
    local file="$1"
    local max_retries=3
    local attempt=1

    while [ $attempt -le $max_retries ]; do
        if cat "$file" | claude -p \
            --model sonnet \
            --max-budget-usd 0.25 \
            --output-format json \
            --no-session-persistence \
            "Analyze this contract" \
            > "results/$(basename "$file" .txt).json" 2>/dev/null; then
            echo "OK: $file"
            return 0
        fi
        echo "RETRY $attempt/$max_retries: $file" >&2
        attempt=$((attempt + 1))
        sleep $((attempt * 2))  # Exponential backoff: 2s, 4s, 6s
    done

    echo "FAILED after $max_retries retries: $file" >&2
    return 1
}

export -f process_file
find contracts/ -name "*.txt" | parallel -j 4 process_file {}
```

### GNU Parallel Built-in Retries

```bash
find contracts/ -name "*.txt" | parallel -j 4 --retries 3 '
  cat {} | claude -p \
    --model sonnet \
    --max-budget-usd 0.25 \
    --output-format json \
    --no-session-persistence \
    "Analyze this contract" \
    > results/{/.}.json
'
```

### Fallback Model

Use `--fallback-model` to automatically fall back when the primary model is overloaded:

```bash
claude -p \
  --model opus \
  --fallback-model sonnet \
  --max-budget-usd 0.50 \
  "Deep analysis of this contract"
```

---

## 8. Session Management for Multi-Step Batch Workflows

### Capture Session ID, Then Follow Up

```bash
# Step 1: Initial analysis
session_id=$(claude -p "Review the auth module" --output-format json | jq -r '.session_id')

# Step 2: Follow up with context from step 1
claude -p "Now focus on the database queries" --resume "$session_id"

# Step 3: Generate summary
claude -p "Generate a summary of all issues found" --resume "$session_id"
```

### Continue Most Recent Session

```bash
# First pass
claude -p "Review this codebase for performance issues"

# Continue (uses most recent session in current directory)
claude -p "Now focus on the database queries" --continue
claude -p "Generate a summary of all issues found" --continue
```

---

## 9. Permission Patterns for Automation

### Read-Only Analysis (Safest)

```bash
claude -p \
  --permission-mode plan \
  "Analyze the authentication system and suggest improvements"
```

Plan mode restricts Claude to read-only operations.

### Explicit Tool Allowlist

```bash
claude -p \
  --allowedTools "Read,Grep,Glob,Bash(git log *),Bash(git diff *)" \
  "Review changes since last release"
```

Note: The trailing ` *` enables prefix matching. `Bash(git diff *)` matches any command starting with `git diff`. The space before `*` is important: `Bash(git diff*)` would also match `git diff-index`.

### Skip All Permissions (CI/CD only -- use with extreme caution)

```bash
claude -p \
  --dangerously-skip-permissions \
  "Run tests and fix any failures"
```

---

## 10. Practical Recipes

### Recipe: Lint All Changed Files

```bash
git diff --name-only HEAD~1 | parallel -j 4 '
  cat {} | claude -p \
    --model haiku \
    --max-budget-usd 0.05 \
    --output-format text \
    --no-session-persistence \
    "Review this file for code quality issues. Report filename:line and description." \
  >> lint-report.txt
'
```

### Recipe: Extract Metadata from a Directory of Documents

```bash
SCHEMA='{"type":"object","properties":{"title":{"type":"string"},"date":{"type":"string"},"parties":{"type":"array","items":{"type":"string"}},"document_type":{"type":"string"}},"required":["title","document_type"]}'

find documents/ -name "*.txt" | parallel -j 6 --bar '
  cat {} | claude -p \
    --model sonnet \
    --max-budget-usd 0.10 \
    --output-format json \
    --no-session-persistence \
    --json-schema '"'"''"$SCHEMA"''"'"' \
    "Extract metadata from this document" \
    > metadata/{/.}.json
'

# Aggregate into single CSV-like output
jq -rs '.[] | [.structured_output.title, .structured_output.document_type, .structured_output.date, (.structured_output.parties // [] | join("; "))] | @csv' metadata/*.json > metadata.csv
```

### Recipe: NDA Triage Batch Pipeline

```bash
#!/usr/bin/env bash
# Batch-triage NDAs using the legalcode NDA triage methodology
set -euo pipefail

NDA_DIR="${1:?Usage: $0 <nda-directory>}"
RESULTS="./nda-triage-results"
mkdir -p "$RESULTS"

PROMPT="Triage this NDA. Classify as:
- GREEN: All standard carveouts present, reasonable scope, standard terms
- YELLOW: Missing 1-2 carveouts or non-standard terms requiring negotiation
- RED: Overbroad, missing critical protections, or contains unusual penalties

For each finding, cite the specific clause. Provide a confidence score 0-1."

SCHEMA='{
  "type":"object",
  "properties":{
    "classification":{"type":"string","enum":["GREEN","YELLOW","RED"]},
    "confidence":{"type":"number"},
    "findings":{"type":"array","items":{"type":"object","properties":{"clause":{"type":"string"},"issue":{"type":"string"},"severity":{"type":"string","enum":["low","medium","high"]}},"required":["clause","issue","severity"]}},
    "recommended_action":{"type":"string"},
    "summary":{"type":"string"}
  },
  "required":["classification","confidence","findings","summary"]
}'

find "$NDA_DIR" -type f \( -name "*.txt" -o -name "*.md" -o -name "*.pdf" \) \
  | parallel -j 4 --bar --retries 2 --joblog "$RESULTS/joblog.txt" \
    "cat {} | claude -p \
      --model sonnet \
      --max-budget-usd 0.30 \
      --output-format json \
      --no-session-persistence \
      --json-schema '""$SCHEMA""' \
      '""$PROMPT""' \
      > '$RESULTS'/{/.}.json 2>'$RESULTS'/{/.}.err"

# Summary report
echo "=== NDA Triage Results ==="
for f in "$RESULTS"/*.json; do
    name=$(basename "$f" .json)
    class=$(jq -r '.structured_output.classification // "UNKNOWN"' "$f")
    conf=$(jq -r '.structured_output.confidence // "?"' "$f")
    summary=$(jq -r '.structured_output.summary // "No summary"' "$f")
    printf "%-30s [%s] (%.0f%%) %s\n" "$name" "$class" "$(echo "$conf * 100" | bc)" "$summary"
done
```

### Recipe: Use with Git Worktrees for Isolated Parallel Work

```bash
# Start Claude in isolated worktrees for parallel tasks
claude --worktree feature-auth    # Creates .claude/worktrees/feature-auth/
claude --worktree bugfix-123      # Creates .claude/worktrees/bugfix-123/

# Or use -p mode in worktrees
claude -w feature-auth -p "Implement the OAuth2 flow" \
  --allowedTools "Read,Edit,Bash"
```

---

## 11. Key Gotchas and Best Practices

1. **Always use `--no-session-persistence`** for batch jobs where you don't need to resume. This prevents cluttering the session store.

2. **Always use `--output-format json`** when you need to parse results programmatically. The `text` format is for human reading only.

3. **Set `--max-budget-usd`** on every batch invocation. A single runaway query can be expensive.

4. **Set `--max-turns`** to prevent infinite loops where Claude keeps trying tools that fail.

5. **Use `--model sonnet` or `--model haiku`** for batch work unless you specifically need Opus-level reasoning. The cost difference is significant at scale.

6. **Escape JSON schemas carefully** when embedding in shell scripts. The nested quoting (`'"'"'`) is necessary for single quotes inside single-quoted strings.

7. **Use `--fallback-model`** for long batch runs so that rate limits on one model don't halt the entire pipeline.

8. **GNU `parallel --joblog`** is invaluable for tracking which files succeeded/failed in a batch run.

9. **Pipe content via stdin** (e.g., `cat file | claude -p`) for per-file processing. For multi-file analysis, use `--add-dir` or let Claude read files with its built-in Read tool.

10. **Use `--permission-mode plan`** for read-only analysis tasks to prevent any accidental writes.

---

## 12. Summary of Output Formats

| Format        | Flag                                         | Best For                                 | Parse With              |
| ------------- | -------------------------------------------- | ---------------------------------------- | ----------------------- |
| Plain text    | `--output-format text`                       | Human reading, simple pipes              | `cat`, redirect         |
| JSON          | `--output-format json`                       | Scripting, aggregation, metadata capture | `jq`                    |
| JSON + Schema | `--output-format json --json-schema '{...}'` | Structured extraction, typed data        | `jq .structured_output` |
| Stream JSON   | `--output-format stream-json`                | Real-time display, progress tracking     | `jq` line-by-line       |
