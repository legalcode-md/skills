import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const generator = path.join(scriptDir, "generate-report.mjs");
const exampleInput = path.join(scriptDir, "example-review-data.json");

test("generator renders a self-contained HTML report", async () => {
  const tmpDir = await fs.mkdtemp(path.join(os.tmpdir(), "tabular-report-test-"));
  const outPath = path.join(tmpDir, "report.html");

  const { code, stdout, stderr } = await runNode([generator, exampleInput, outPath]);
  assert.equal(code, 0, stderr || stdout);

  const html = await fs.readFile(outPath, "utf8");
  assert.match(html, /Supplier Agreement Portfolio Review/);
  assert.match(html, /<style>/);
  assert.match(html, /<script id="review-data" type="application\/json">/);
  assert.match(html, /Portable static HTML report generated locally from review-data\.json/);
});

test("generator fails on invalid status values", async () => {
  const tmpDir = await fs.mkdtemp(path.join(os.tmpdir(), "tabular-report-invalid-"));
  const badInput = path.join(tmpDir, "bad.json");
  const outPath = path.join(tmpDir, "report.html");
  const payload = JSON.parse(await fs.readFile(exampleInput, "utf8"));
  payload.rows[0].overallStatus = "bogus";
  await fs.writeFile(badInput, JSON.stringify(payload, null, 2), "utf8");

  const { code, stderr } = await runNode([generator, badInput, outPath]);
  assert.notEqual(code, 0);
  assert.match(stderr, /invalid overallStatus/i);
});

function runNode(args) {
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, args, { cwd: scriptDir });
    let stdout = "";
    let stderr = "";
    child.stdout.on("data", (chunk) => {
      stdout += String(chunk);
    });
    child.stderr.on("data", (chunk) => {
      stderr += String(chunk);
    });
    child.on("error", reject);
    child.on("close", (code) => resolve({ code, stdout, stderr }));
  });
}
