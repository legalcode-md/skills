#!/usr/bin/env bash
#
# Stage 1: Document Conversion
#
# Converts raw documents (PDF, DOCX, MSG, EML, images, text) to markdown.
# Uses LOCAL tools only -- no API calls. Zero cost.
#
# Conversion strategy per format:
#   PDF   -> magic-pdf (MinerU) or pdftotext fallback
#   DOCX  -> pandoc or python-docx
#   MSG   -> extract-msg (Python) or manual parse
#   EML   -> Python email stdlib
#   TXT   -> copy with frontmatter wrapper
#   HTML  -> pandoc
#   Image -> copy to converted/ for Stage 2 vision processing
#
# Each converted document gets a frontmatter header with source metadata.

run_stage_1_convert() {
  stage "1" "Document Conversion (local, no API)"

  local converted_dir="${TIMELINE_DIR}/converted"
  local log_dir="${TIMELINE_DIR}/logs/stage-1"
  ensure_dir "$converted_dir"
  ensure_dir "$log_dir"

  # Determine available conversion tools
  local has_magic_pdf=false
  local has_pandoc=false
  local has_pdftotext=false

  command -v magic-pdf &>/dev/null && has_magic_pdf=true
  command -v pandoc &>/dev/null    && has_pandoc=true
  command -v pdftotext &>/dev/null && has_pdftotext=true

  log "Available tools: magic-pdf=$has_magic_pdf pandoc=$has_pandoc pdftotext=$has_pdftotext"

  if [[ "$has_magic_pdf" == "false" && "$has_pdftotext" == "false" && "$has_pandoc" == "false" ]]; then
    warn "No PDF conversion tools found. Install one of:"
    warn "  pip install magic-pdf    # MinerU (recommended)"
    warn "  brew install poppler     # pdftotext"
    warn "  brew install pandoc      # pandoc"
    warn "Falling back to text-only extraction where possible."
  fi

  local total=0
  local succeeded=0
  local failed=0
  local skipped=0

  # Process each pending document from manifest
  while IFS=$'\t' read -r source_id original_path _; do
    total=$((total + 1))
    local ext="${original_path##*.}"
    ext="$(echo "$ext" | tr '[:upper:]' '[:lower:]')"
    local out_file="${converted_dir}/${source_id}.md"
    local conv_log="${log_dir}/${source_id}.log"

    # Skip if already converted
    if [[ -f "$out_file" ]]; then
      skipped=$((skipped + 1))
      manifest_update_status "$source_id" "status" "converted"
      manifest_update_status "$source_id" "converted_path" "$out_file"
      continue
    fi

    log "[$total] Converting ${source_id} (${ext}): $(basename "$original_path")"

    local convert_ok=false

    case "$ext" in
      pdf)
        convert_pdf "$source_id" "$original_path" "$out_file" "$conv_log" \
          "$has_magic_pdf" "$has_pdftotext" "$has_pandoc" && convert_ok=true
        ;;
      docx|doc)
        convert_docx "$source_id" "$original_path" "$out_file" "$conv_log" \
          "$has_pandoc" && convert_ok=true
        ;;
      msg)
        convert_msg "$source_id" "$original_path" "$out_file" "$conv_log" && convert_ok=true
        ;;
      eml)
        convert_eml "$source_id" "$original_path" "$out_file" "$conv_log" && convert_ok=true
        ;;
      txt|rtf)
        convert_text "$source_id" "$original_path" "$out_file" "$conv_log" && convert_ok=true
        ;;
      html|htm)
        convert_html "$source_id" "$original_path" "$out_file" "$conv_log" \
          "$has_pandoc" && convert_ok=true
        ;;
      png|jpg|jpeg|tiff|tif)
        convert_image "$source_id" "$original_path" "$out_file" "$conv_log" && convert_ok=true
        ;;
      *)
        warn "  Unknown format: $ext -- skipping"
        manifest_update_status "$source_id" "status" "unsupported"
        skipped=$((skipped + 1))
        continue
        ;;
    esac

    if [[ "$convert_ok" == "true" ]]; then
      manifest_update_status "$source_id" "status" "converted"
      manifest_update_status "$source_id" "converted_path" "$out_file"
      succeeded=$((succeeded + 1))
    else
      manifest_update_status "$source_id" "status" "failed"
      failed=$((failed + 1))
    fi

  done < <(manifest_get_by_status "status" "pending")

  divider
  ok "Stage 1 complete: $succeeded converted, $skipped skipped, $failed failed (of $total)"

  if [[ $failed -gt 0 ]]; then
    warn "$failed documents failed conversion. Check logs in ${log_dir}/"
    # Non-fatal: continue pipeline with what we have
  fi

  return 0
}

# ─── Format-specific converters ────────────────────────────────────────────

write_frontmatter() {
  local out_file="$1"
  local source_id="$2"
  local original_path="$3"
  local doc_type="$4"
  local extra="${5:-}"

  cat > "$out_file" <<FMEOF
---
source_id: ${source_id}
original_path: ${original_path}
document_type: ${doc_type}
converted_at: $(date -u +%Y-%m-%dT%H:%M:%SZ)
filename: $(basename "$original_path")
${extra}---

FMEOF
}

convert_pdf() {
  local source_id="$1" original_path="$2" out_file="$3" conv_log="$4"
  local has_magic_pdf="$5" has_pdftotext="$6" has_pandoc="$7"

  if [[ "$has_magic_pdf" == "true" ]]; then
    local tmp_dir="${TIMELINE_DIR}/converted/.tmp-${source_id}"
    mkdir -p "$tmp_dir"
    if magic-pdf -p "$original_path" -o "$tmp_dir" -m auto > "$conv_log" 2>&1; then
      # Find the generated markdown
      local md_file
      md_file="$(find "$tmp_dir" -name "*.md" -type f | head -1)"
      if [[ -n "$md_file" ]]; then
        write_frontmatter "$out_file" "$source_id" "$original_path" "pdf"
        cat "$md_file" >> "$out_file"
        rm -rf "$tmp_dir"
        ok "  ${source_id}: PDF converted via MinerU"
        return 0
      fi
    fi
    rm -rf "$tmp_dir"
  fi

  if [[ "$has_pdftotext" == "true" ]]; then
    write_frontmatter "$out_file" "$source_id" "$original_path" "pdf" "conversion_tool: pdftotext
"
    if pdftotext -layout "$original_path" - >> "$out_file" 2> "$conv_log"; then
      ok "  ${source_id}: PDF converted via pdftotext"
      return 0
    fi
  fi

  if [[ "$has_pandoc" == "true" ]]; then
    write_frontmatter "$out_file" "$source_id" "$original_path" "pdf" "conversion_tool: pandoc
"
    if pandoc -f pdf -t markdown "$original_path" >> "$out_file" 2> "$conv_log"; then
      ok "  ${source_id}: PDF converted via pandoc"
      return 0
    fi
  fi

  fail "  ${source_id}: No PDF converter available or all failed"
  return 1
}

convert_docx() {
  local source_id="$1" original_path="$2" out_file="$3" conv_log="$4"
  local has_pandoc="$5"

  if [[ "$has_pandoc" == "true" ]]; then
    write_frontmatter "$out_file" "$source_id" "$original_path" "docx" "conversion_tool: pandoc
"
    if pandoc -f docx -t markdown --wrap=none "$original_path" >> "$out_file" 2> "$conv_log"; then
      ok "  ${source_id}: DOCX converted via pandoc"
      return 0
    fi
  fi

  # Fallback: try python-docx extraction
  write_frontmatter "$out_file" "$source_id" "$original_path" "docx" "conversion_tool: python-docx
"
  if python3 - "$original_path" >> "$out_file" 2> "$conv_log" <<'PYEOF'
import sys
try:
    from docx import Document
    doc = Document(sys.argv[1])
    for para in doc.paragraphs:
        print(para.text)
except ImportError:
    # No python-docx; try raw XML extraction
    import zipfile
    import xml.etree.ElementTree as ET
    z = zipfile.ZipFile(sys.argv[1])
    tree = ET.parse(z.open('word/document.xml'))
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        texts = [t.text for t in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
        if texts:
            print(''.join(texts))
PYEOF
  then
    ok "  ${source_id}: DOCX converted via python"
    return 0
  fi

  fail "  ${source_id}: DOCX conversion failed"
  return 1
}

convert_msg() {
  local source_id="$1" original_path="$2" out_file="$3" conv_log="$4"

  write_frontmatter "$out_file" "$source_id" "$original_path" "email" "conversion_tool: extract-msg
"

  if python3 - "$original_path" "$source_id" >> "$out_file" 2> "$conv_log" <<'PYEOF'
import sys
try:
    import extract_msg
    msg = extract_msg.Message(sys.argv[1])
    source_id = sys.argv[2]
    print(f"# Email: {msg.subject or '(no subject)'}\n")
    print(f"**From:** {msg.sender or '(unknown)'}")
    print(f"**To:** {msg.to or '(unknown)'}")
    if msg.cc:
        print(f"**CC:** {msg.cc}")
    print(f"**Date:** {msg.date or '(unknown)'}")
    print(f"\n---\n")
    print(msg.body or "(empty body)")
    if msg.attachments:
        print(f"\n---\n\n**Attachments:**")
        for i, att in enumerate(msg.attachments, 1):
            print(f"{i}. {att.longFilename or att.shortFilename or 'unnamed'} (see {source_id}-ATT-{i:03d})")
except ImportError:
    print("(MSG file -- requires extract-msg package for parsing)")
    print(f"Original file: {sys.argv[1]}")
    sys.exit(1)
PYEOF
  then
    ok "  ${source_id}: MSG email converted"
    return 0
  fi

  fail "  ${source_id}: MSG conversion failed (install: pip install extract-msg)"
  return 1
}

convert_eml() {
  local source_id="$1" original_path="$2" out_file="$3" conv_log="$4"

  write_frontmatter "$out_file" "$source_id" "$original_path" "email" "conversion_tool: python-email
"

  if python3 - "$original_path" "$source_id" >> "$out_file" 2> "$conv_log" <<'PYEOF'
import sys, email, email.policy

with open(sys.argv[1], 'rb') as f:
    msg = email.message_from_binary_file(f, policy=email.policy.default)

source_id = sys.argv[2]
print(f"# Email: {msg['subject'] or '(no subject)'}\n")
print(f"**From:** {msg['from'] or '(unknown)'}")
print(f"**To:** {msg['to'] or '(unknown)'}")
if msg['cc']:
    print(f"**CC:** {msg['cc']}")
print(f"**Date:** {msg['date'] or '(unknown)'}")
print(f"\n---\n")

body = msg.get_body(preferencelist=('plain', 'html'))
if body:
    content = body.get_content()
    print(content)
else:
    print("(empty body)")

attachments = [p for p in msg.iter_attachments()]
if attachments:
    print(f"\n---\n\n**Attachments:**")
    for i, att in enumerate(attachments, 1):
        fname = att.get_filename() or 'unnamed'
        print(f"{i}. {fname} (see {source_id}-ATT-{i:03d})")
PYEOF
  then
    ok "  ${source_id}: EML email converted"
    return 0
  fi

  fail "  ${source_id}: EML conversion failed"
  return 1
}

convert_text() {
  local source_id="$1" original_path="$2" out_file="$3" conv_log="$4"

  write_frontmatter "$out_file" "$source_id" "$original_path" "text"

  if cat "$original_path" >> "$out_file" 2> "$conv_log"; then
    ok "  ${source_id}: Text file wrapped"
    return 0
  fi

  fail "  ${source_id}: Text conversion failed"
  return 1
}

convert_html() {
  local source_id="$1" original_path="$2" out_file="$3" conv_log="$4"
  local has_pandoc="$5"

  if [[ "$has_pandoc" == "true" ]]; then
    write_frontmatter "$out_file" "$source_id" "$original_path" "html" "conversion_tool: pandoc
"
    if pandoc -f html -t markdown --wrap=none "$original_path" >> "$out_file" 2> "$conv_log"; then
      ok "  ${source_id}: HTML converted via pandoc"
      return 0
    fi
  fi

  # Fallback: strip tags with python
  write_frontmatter "$out_file" "$source_id" "$original_path" "html" "conversion_tool: python-html
"
  if python3 - "$original_path" >> "$out_file" 2> "$conv_log" <<'PYEOF'
import sys
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
    def handle_data(self, data):
        self.text.append(data)
    def get_text(self):
        return '\n'.join(self.text)

with open(sys.argv[1], 'r', errors='replace') as f:
    parser = TextExtractor()
    parser.feed(f.read())
    print(parser.get_text())
PYEOF
  then
    ok "  ${source_id}: HTML converted via python"
    return 0
  fi

  fail "  ${source_id}: HTML conversion failed"
  return 1
}

convert_image() {
  local source_id="$1" original_path="$2" out_file="$3" conv_log="$4"

  # Images cannot be converted to text locally without OCR.
  # We mark them for Stage 2 vision processing.
  local ext="${original_path##*.}"

  write_frontmatter "$out_file" "$source_id" "$original_path" "image" "requires_vision: true
image_format: ${ext}
"

  cat >> "$out_file" <<EOF
# Image Document: $(basename "$original_path")

This document is an image file and requires vision model processing for content extraction.
The image will be analyzed in Stage 2 using Claude vision capabilities.

**Original file:** ${original_path}
**Format:** ${ext}
EOF

  # Copy image to converted dir for easy access in Stage 2
  cp "$original_path" "${TIMELINE_DIR}/converted/${source_id}.${ext}" 2> "$conv_log"

  ok "  ${source_id}: Image staged for vision processing"
  return 0
}
