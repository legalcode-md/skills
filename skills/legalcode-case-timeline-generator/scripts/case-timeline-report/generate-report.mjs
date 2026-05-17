#!/usr/bin/env node
import { readFile, writeFile } from "node:fs/promises";
import { basename } from "node:path";

function usage() {
  console.error(
    [
      "Usage:",
      '  node scripts/case-timeline-report/generate-report.mjs <timeline-data.json> <report.html> [--title "Matter timeline"]',
      "",
      "Input JSON should follow scripts/case-timeline-report/schema.md.",
    ].join("\n"),
  );
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function asArray(value) {
  return Array.isArray(value) ? value : [];
}

function sourceText(source) {
  if (typeof source === "string") return source;
  if (!source || typeof source !== "object") return "";
  return [source.label, source.path, source.page ? `p. ${source.page}` : "", source.quote]
    .filter(Boolean)
    .join(" - ");
}

function renderSources(sources) {
  const items = asArray(sources)
    .map(sourceText)
    .filter(Boolean)
    .map((source) => `<li>${escapeHtml(source)}</li>`)
    .join("");
  return items ? `<ul class="sources">${items}</ul>` : "";
}

function renderEvents(events) {
  return asArray(events)
    .map((event) => {
      const tags = asArray(event.tags)
        .map((tag) => `<span>${escapeHtml(tag)}</span>`)
        .join("");
      return `
        <article class="event">
          <div class="date">${escapeHtml(event.date || "Undated")}</div>
          <div class="body">
            <h2>${escapeHtml(event.title || "Untitled event")}</h2>
            <p>${escapeHtml(event.description || "")}</p>
            <div class="meta">
              ${event.confidence ? `<span>Confidence: ${escapeHtml(event.confidence)}</span>` : ""}
              ${tags ? `<span class="tags">${tags}</span>` : ""}
            </div>
            ${renderSources(event.sources)}
          </div>
        </article>`;
    })
    .join("");
}

function renderPanel(title, items, emptyText) {
  const body = asArray(items)
    .map(
      (item) => `
        <li>
          <strong>${escapeHtml(item.title || item.name || "Untitled")}</strong>
          ${item.severity ? `<span class="pill">${escapeHtml(item.severity)}</span>` : ""}
          ${item.priority ? `<span class="pill">${escapeHtml(item.priority)}</span>` : ""}
          ${item.status ? `<span class="pill">${escapeHtml(item.status)}</span>` : ""}
          ${item.owner ? `<span class="pill">Owner: ${escapeHtml(item.owner)}</span>` : ""}
          ${item.deadline ? `<span class="pill">Due: ${escapeHtml(item.deadline)}</span>` : ""}
          <p>${escapeHtml(item.description || item.needed_evidence || "")}</p>
          ${renderSources(item.sources)}
        </li>`,
    )
    .join("");
  return `
    <section class="panel">
      <h2>${escapeHtml(title)}</h2>
      <ul>${body || `<li class="empty">${escapeHtml(emptyText)}</li>`}</ul>
    </section>`;
}

function renderHtml(data, title) {
  const reportTitle = title || data.matter || "Case Timeline";
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${escapeHtml(reportTitle)}</title>
  <style>
    :root { color-scheme: light; font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    body { margin: 0; color: #15201d; background: #f7f8f6; }
    header { padding: 32px 40px 20px; background: #0f302b; color: white; }
    header h1 { margin: 0 0 8px; font-size: 30px; }
    header p { max-width: 900px; margin: 0; color: #d7e4df; }
    main { display: grid; grid-template-columns: minmax(0, 1fr) 360px; gap: 24px; padding: 28px 40px 44px; }
    .timeline { position: relative; padding-left: 22px; }
    .timeline:before { content: ""; position: absolute; left: 5px; top: 0; bottom: 0; width: 2px; background: #b5c9c1; }
    .event { display: grid; grid-template-columns: 150px minmax(0, 1fr); gap: 18px; margin: 0 0 18px; position: relative; }
    .event:before { content: ""; position: absolute; left: -22px; top: 8px; width: 12px; height: 12px; border-radius: 50%; background: #0f766e; border: 3px solid #f7f8f6; }
    .date { font-weight: 700; color: #31534c; }
    .body, .panel { background: white; border: 1px solid #dfe7e3; border-radius: 8px; padding: 16px; box-shadow: 0 1px 2px rgba(21, 32, 29, .05); }
    h2 { margin: 0 0 8px; font-size: 18px; }
    p { line-height: 1.5; }
    .meta { display: flex; flex-wrap: wrap; gap: 8px; color: #4c625c; font-size: 13px; }
    .tags span, .pill { display: inline-block; margin: 0 5px 5px 0; padding: 2px 7px; border: 1px solid #cddbd6; border-radius: 999px; background: #eef5f2; font-size: 12px; }
    .sources { margin: 12px 0 0; padding-left: 18px; color: #405650; font-size: 13px; }
    aside { display: grid; gap: 16px; align-content: start; }
    .panel ul { margin: 0; padding-left: 18px; }
    .panel li { margin-bottom: 12px; }
    .empty { color: #6b7774; }
    @media (max-width: 900px) { main { grid-template-columns: 1fr; padding: 20px; } header { padding: 24px 20px; } .event { grid-template-columns: 1fr; } }
  </style>
</head>
<body>
  <header>
    <h1>${escapeHtml(reportTitle)}</h1>
    ${data.summary ? `<p>${escapeHtml(data.summary)}</p>` : ""}
  </header>
  <main>
    <section class="timeline">
      ${renderEvents(data.events) || '<p class="empty">No events found.</p>'}
    </section>
    <aside>
      ${renderPanel("Contradictions", data.contradictions, "No contradictions recorded.")}
      ${renderPanel("Evidence Gaps", data.gaps, "No evidence gaps recorded.")}
      ${renderPanel("Obligations", data.obligations, "No obligations recorded.")}
    </aside>
  </main>
</body>
</html>`;
}

const args = process.argv.slice(2);
if (args.length < 2 || args.includes("--help")) {
  usage();
  process.exit(args.includes("--help") ? 0 : 1);
}

const [inputPath, outputPath] = args;
const titleIndex = args.indexOf("--title");
const title = titleIndex >= 0 ? args[titleIndex + 1] : undefined;
const raw = await readFile(inputPath, "utf8");
const data = JSON.parse(raw);
await writeFile(outputPath, renderHtml(data, title || data.title || basename(inputPath)), "utf8");
console.log(`Wrote ${outputPath}`);
