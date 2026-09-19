# Case Timeline Report Schema

The renderer accepts one JSON object with these optional top-level fields:

```json
{
  "matter": "Matter name",
  "summary": "Short narrative summary",
  "events": [],
  "contradictions": [],
  "gaps": [],
  "obligations": []
}
```

## Events

Each event may include:

- `date`: ISO date or display date.
- `title`: short event label.
- `description`: event details.
- `confidence`: `high`, `medium`, `low`, or a numeric score.
- `sources`: array of source labels, citations, or objects with `label`, `path`, `page`, or `quote`.
- `tags`: array of filter labels.

## Contradictions

Each contradiction may include `title`, `description`, `sources`, and `severity`.

## Gaps

Each gap may include `title`, `description`, `needed_evidence`, and `priority`.

## Obligations

Each obligation may include `title`, `owner`, `deadline`, `status`, `description`, and `sources`.

Unknown fields are ignored by the renderer and preserved in the JSON source.
