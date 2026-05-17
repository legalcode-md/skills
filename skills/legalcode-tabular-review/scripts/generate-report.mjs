#!/usr/bin/env node

import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

const STATUS_VALUES = new Set(["verified", "needs_review", "conflict", "not_found", "failed"]);
const CONFIDENCE_VALUES = new Set(["definite", "high", "probable", "possible", "unlikely"]);

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help || !args.input || !args.output) {
    printUsage(args.help ? 0 : 1);
    return;
  }

  const inputPath = path.resolve(args.input);
  const outputPath = path.resolve(args.output);
  const baseDir = path.dirname(fileURLToPath(import.meta.url));

  const [rawInput, template, css, js] = await Promise.all([
    fs.readFile(inputPath, "utf8"),
    fs.readFile(path.join(baseDir, "report.html"), "utf8"),
    fs.readFile(path.join(baseDir, "report.css"), "utf8"),
    fs.readFile(path.join(baseDir, "report.js"), "utf8"),
  ]);

  const data = JSON.parse(rawInput);
  validateReportData(data);
  const normalized = normalizeReportData(data, args.title);

  const html = template
    .replace("__REPORT_TITLE__", escapeHtml(normalized.meta.reportTitle))
    .replace("__INLINE_CSS__", css.trimEnd())
    .replace("__INLINE_JS__", js.trimEnd())
    .replace("__REPORT_DATA__", safeJson(normalized));

  await fs.mkdir(path.dirname(outputPath), { recursive: true });
  await fs.writeFile(outputPath, html, "utf8");
  process.stdout.write(`Generated ${outputPath}\n`);
}

function parseArgs(argv) {
  const args = { input: "", output: "", title: "", help: false };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--help" || arg === "-h") {
      args.help = true;
      break;
    }
    if (arg === "--title") {
      args.title = argv[i + 1] || "";
      i += 1;
      continue;
    }
    if (!args.input) {
      args.input = arg;
      continue;
    }
    if (!args.output) {
      args.output = arg;
      continue;
    }
    throw new Error(`Unexpected argument: ${arg}`);
  }
  return args;
}

function printUsage(exitCode) {
  const usage = [
    "Usage:",
    '  node path/to/legalcode-tabular-review/scripts/generate-report.mjs <input.json> <output.html> [--title "Custom title"]',
    "",
    "Examples:",
    "  node path/to/legalcode-tabular-review/scripts/generate-report.mjs \\",
    "    path/to/legalcode-tabular-review/scripts/example-review-data.json \\",
    "    .tmp/tabular-review/example-report.html",
    '  node path/to/legalcode-tabular-review/scripts/generate-report.mjs review-data.json report.html --title "Supplier Review"',
  ].join("\n");
  if (exitCode === 0) {
    process.stdout.write(`${usage}\n`);
  } else {
    process.stderr.write(`${usage}\n`);
    process.exitCode = exitCode;
  }
}

function validateReportData(data) {
  if (!isPlainObject(data)) {
    throw new Error("review-data.json must be a JSON object");
  }
  if (!isPlainObject(data.meta)) {
    throw new Error("meta must be an object");
  }
  if (!Array.isArray(data.columns)) {
    throw new Error("columns must be an array");
  }
  if (!Array.isArray(data.rows)) {
    throw new Error("rows must be an array");
  }

  const columnKeys = new Set();
  for (const column of data.columns) {
    if (!isPlainObject(column)) {
      throw new Error("each column must be an object");
    }
    if (!isNonEmptyString(column.key)) {
      throw new Error("each column requires a non-empty key");
    }
    if (!isNonEmptyString(column.label)) {
      throw new Error(`column ${column.key} requires a non-empty label`);
    }
    if (columnKeys.has(column.key)) {
      throw new Error(`duplicate column key: ${column.key}`);
    }
    columnKeys.add(column.key);
  }

  for (const row of data.rows) {
    if (!isPlainObject(row)) {
      throw new Error("each row must be an object");
    }
    if (!isNonEmptyString(row.id)) {
      throw new Error("each row requires a non-empty id");
    }
    if (!isNonEmptyString(row.documentName)) {
      throw new Error(`row ${row.id} requires documentName`);
    }
    if (!STATUS_VALUES.has(row.overallStatus)) {
      throw new Error(`row ${row.id} has invalid overallStatus: ${row.overallStatus}`);
    }
    if (!isPlainObject(row.cells)) {
      throw new Error(`row ${row.id} requires cells object`);
    }

    for (const [columnKey, cell] of Object.entries(row.cells)) {
      if (!columnKeys.has(columnKey)) {
        throw new Error(`row ${row.id} references unknown column key: ${columnKey}`);
      }
      if (!isPlainObject(cell)) {
        throw new Error(`row ${row.id} column ${columnKey} must be an object`);
      }
      if (typeof cell.answer !== "string") {
        throw new Error(`row ${row.id} column ${columnKey} must have string answer`);
      }
      if (!STATUS_VALUES.has(cell.status)) {
        throw new Error(`row ${row.id} column ${columnKey} has invalid status: ${cell.status}`);
      }
      if (!CONFIDENCE_VALUES.has(cell.confidence)) {
        throw new Error(
          `row ${row.id} column ${columnKey} has invalid confidence: ${cell.confidence}`,
        );
      }
      if (cell.source !== undefined && !isPlainObject(cell.source)) {
        throw new Error(`row ${row.id} column ${columnKey} source must be an object`);
      }
      if (cell.notes !== undefined && typeof cell.notes !== "string") {
        throw new Error(`row ${row.id} column ${columnKey} notes must be a string`);
      }
    }
  }
}

function normalizeReportData(data, titleOverride) {
  const cloned = structuredClone(data);
  cloned.meta.reportTitle = titleOverride || cloned.meta.reportTitle || "Tabular Review";
  cloned.meta.generatedAt = cloned.meta.generatedAt || new Date().toISOString();
  cloned.meta.runId = cloned.meta.runId || "run-unknown";
  cloned.meta.corpusLabel = cloned.meta.corpusLabel || "";
  cloned.meta.executionPath = cloned.meta.executionPath || "manual";
  cloned.meta.documentCount = Number(cloned.meta.documentCount || cloned.rows.length);
  cloned.meta.columnCount = Number(cloned.meta.columnCount || cloned.columns.length);
  cloned.summary = isPlainObject(cloned.summary) ? cloned.summary : {};
  cloned.conflicts = Array.isArray(cloned.conflicts) ? cloned.conflicts : [];
  cloned.filters = isPlainObject(cloned.filters) ? cloned.filters : {};
  return cloned;
}

function safeJson(value) {
  return JSON.stringify(value, null, 2)
    .replace(/</g, "\\u003c")
    .replace(/>/g, "\\u003e")
    .replace(/&/g, "\\u0026");
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function isPlainObject(value) {
  return Boolean(value) && typeof value === "object" && !Array.isArray(value);
}

function isNonEmptyString(value) {
  return typeof value === "string" && value.trim().length > 0;
}

main().catch((error) => {
  process.stderr.write(`${error.message}\n`);
  process.exitCode = 1;
});
