#!/usr/bin/env node

import { readFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const args = process.argv.slice(2);
const reportIndex = args.indexOf("--report");
const reportPath = reportIndex >= 0 ? args[reportIndex + 1] : undefined;

if (!reportPath) {
  console.error("Usage: check-report-boundary.mjs --report <report.md>");
  process.exit(2);
}

const absolute = path.resolve(reportPath);
const content = await readFile(absolute, "utf8");
const checks = [
  {
    label: "internal audit terminology",
    pattern:
      /glass[ -]?box|internal traceability|innri rekjanleiki|internal audit(?: record)?|audit appendix/iu,
  },
  {
    label: "product or repository defect material",
    pattern: /mcp[- ]defect|github issue|github\.com\/[^\s)]+\/issues\/\d+/iu,
  },
  {
    label: "internal source identifier",
    pattern: /sourceRef|internal source (?:id|identifier|reference)/u,
  },
  {
    label: "internal artifact name",
    pattern:
      /internal-audit-record|unresolved-evidence-register|mcp-defects|glass-box\.ya?ml/iu,
  },
  {
    label: "relative link to supporting workflow files",
    pattern: /\]\(\.\.\/(?:audit|evidence|findings|matrix|sources)\//u,
  },
  {
    label: "local workflow path",
    pattern: /(?:^|[\s`])\.\.\/(?:audit|evidence|findings|matrix|sources)\//mu,
  },
];

const violations = checks
  .filter(({ pattern }) => pattern.test(content))
  .map(({ label }) => label);

if (violations.length > 0) {
  console.error(`Report-boundary check failed for ${reportPath}:`);
  for (const violation of violations) console.error(`- ${violation}`);
  process.exit(1);
}

console.log(`Report-boundary check passed: ${reportPath}`);
