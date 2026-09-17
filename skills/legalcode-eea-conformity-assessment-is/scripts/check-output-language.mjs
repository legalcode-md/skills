#!/usr/bin/env node

import { readdir, readFile, stat } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const args = process.argv.slice(2);

function valueFor(flag) {
  const index = args.indexOf(flag);
  return index >= 0 ? args[index + 1] : undefined;
}

const language = valueFor("--language");
const matterRoot = valueFor("--root");

if (!matterRoot || !["en", "is"].includes(language)) {
  console.error(
    "Usage: check-output-language.mjs --language <en|is> --root <matter-directory>",
  );
  process.exit(2);
}

const root = path.resolve(matterRoot);
const extensions = new Set([".csv", ".json", ".md", ".yaml", ".yml"]);

const icelandicTemplateLabels = [
  "Samræmisathugun",
  "Samantekt",
  "Umfang og forsendur",
  "EES-réttarlegur grunnur",
  "Tilkynningar til ESA",
  "Innlendar innleiðingarráðstafanir",
  "Heimildaskrá",
  "Samanburðartafla",
  "Niðurstöður",
  "Stjórnsýsla, úrræði og viðurlög",
  "Framkvæmd og háttsemi sem rekja má til ríkisins",
  "Málsmeðferð hjá ESA",
  "Úrbótaáætlun",
  "Óleyst atriði og gagnaóskir",
  "Tilvísanir",
  "Innri rekjanleiki",
  "| Atriði",
  "| Niðurstaða",
  "| Opinber heimild",
  "| Staðfest",
  "| Form 1 / gögn",
  "| Dagsetning",
  "| Innlend ráðstöfun",
  "| Forgangur",
  "| Aðgerð",
  "| Ábyrgð",
  "| Tími",
];

const englishTemplateLabels = [
  "Conformity Assessment",
  "Executive Summary",
  "Scope and Assumptions",
  "EEA Legal Basis",
  "Notifications to ESA",
  "National Implementing Measures",
  "Source Register",
  "Provision-by-Provision Conformity Matrix",
  "Findings",
  "Administration, Remedies, and Penalties",
  "Application and State Attribution",
  "ESA Procedure",
  "Remediation Plan",
  "Unresolved Issues and Evidence Requests",
  "Authorities",
  "Internal Traceability",
];

const forbiddenLabels =
  language === "en" ? icelandicTemplateLabels : englishTemplateLabels;
const forbiddenFilenameParts =
  language === "en"
    ? ["samraemisathugun", "samanburdartafla"]
    : ["conformity-assessment-report", "conformity-matrix"];

async function collect(directory) {
  const files = [];
  for (const entry of await readdir(directory)) {
    if (entry === "sources") continue;
    const absolute = path.join(directory, entry);
    const info = await stat(absolute);
    if (info.isDirectory()) {
      files.push(...(await collect(absolute)));
    } else if (extensions.has(path.extname(entry).toLowerCase())) {
      files.push(absolute);
    }
  }
  return files;
}

const violations = [];
const files = await collect(root);

for (const file of files) {
  const relative = path.relative(root, file);
  const lowerName = relative.toLowerCase();
  for (const part of forbiddenFilenameParts) {
    if (lowerName.includes(part)) {
      violations.push(`${relative}: filename contains '${part}'`);
    }
  }

  const content = await readFile(file, "utf8");
  for (const label of forbiddenLabels) {
    if (content.includes(label)) {
      violations.push(`${relative}: contains authored label '${label}'`);
    }
  }
}

if (violations.length > 0) {
  console.error(`Language consistency check failed (${language}):`);
  for (const violation of violations) console.error(`- ${violation}`);
  process.exit(1);
}

console.log(
  `Language consistency check passed (${language}): ${files.length} authored files checked.`,
);
