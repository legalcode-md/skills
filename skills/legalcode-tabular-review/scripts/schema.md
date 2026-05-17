# Tabular Review Report Schema

The portable report generator consumes a single JSON file. The generator validates this input
and emits a self-contained `report.html`.

## Top-level shape

```json
{
  "meta": {},
  "columns": [],
  "rows": [],
  "summary": {},
  "conflicts": [],
  "filters": {}
}
```

## `meta`

```json
{
  "reportTitle": "Q2 Supplier Contract Review",
  "generatedAt": "2026-04-09T18:42:00.000Z",
  "runId": "run-2026-04-09-001",
  "corpusLabel": "Supplier agreements / April intake",
  "executionPath": "cli",
  "documentCount": 24,
  "columnCount": 6
}
```

Required:
- `reportTitle`
- `generatedAt`
- `runId`

Optional:
- `corpusLabel`
- `executionPath`
- `documentCount`
- `columnCount`

## `columns`

Each column defines a visible review dimension.

```json
[
  {
    "key": "governing_law",
    "label": "Governing Law",
    "type": "text",
    "sortable": true,
    "filterable": true
  }
]
```

Required per column:
- `key`
- `label`

Optional:
- `type`
- `sortable`
- `filterable`

Rules:
- column keys must be unique
- keys must be stable because rows reference them directly

## `rows`

```json
[
  {
    "id": "DOC-001",
    "documentName": "Acme MSA Final.pdf",
    "documentPath": "/abs/path/Acme MSA Final.pdf",
    "documentType": "MSA",
    "sourceGroup": "Supplier folder A",
    "overallStatus": "verified",
    "cells": {
      "governing_law": {
        "answer": "England and Wales",
        "status": "verified",
        "confidence": "high",
        "source": {
          "page": 17,
          "section": "18.7",
          "quote": "This Agreement is governed by the laws of England and Wales."
        },
        "notes": "Standard vendor position."
      }
    }
  }
]
```

Required per row:
- `id`
- `documentName`
- `overallStatus`
- `cells`

Optional:
- `documentPath`
- `documentType`
- `sourceGroup`

## Cell object

Required per cell:
- `answer`
- `status`
- `confidence`

Optional:
- `source`
- `notes`

### Valid `status` values

- `verified`
- `needs_review`
- `conflict`
- `not_found`
- `failed`

### Valid `confidence` values

- `definite`
- `high`
- `probable`
- `possible`
- `unlikely`

### `source`

All fields optional, but the generator expects an object if present.

```json
{
  "page": 17,
  "section": "18.7",
  "heading": "Governing Law",
  "quote": "This Agreement is governed by the laws of England and Wales."
}
```

## `summary`

Optional section for future expansion. Current generator computes the visible summary from rows
if not supplied.

## `conflicts`

Optional array reserved for future conflict register rendering.

## `filters`

Optional array collections for future precomputed filter metadata.

## Validation rules

The generator fails on:
- non-object top-level input
- missing `meta`, `columns`, or `rows`
- duplicate column keys
- missing row ids
- invalid row or cell status values
- invalid cell confidence values
- cell keys that do not match a defined column

## Output contract

The generator emits:
- a single portable `report.html`

The report is fully self-contained:
- CSS inlined
- JS inlined
- JSON payload inlined
- no external network requests
