(function () {
  "use strict";

  var STATUS_ORDER = ["verified", "needs_review", "conflict", "not_found", "failed"];
  var CONFIDENCE_ORDER = ["definite", "high", "probable", "possible", "unlikely"];
  var state = {
    data: null,
    visibleColumnKeys: [],
    selectedRowId: null,
    selectedColumnKey: null,
    sort: { key: "documentName", direction: "asc" },
    filters: { q: "", status: "", sourceGroup: "", documentType: "" },
  };

  function boot() {
    var dataNode = document.getElementById("review-data");
    if (!dataNode) {
      throw new Error("Missing review-data script tag");
    }
    state.data = JSON.parse(dataNode.textContent || "{}");
    state.visibleColumnKeys = state.data.columns.slice(0, 8).map(function (column) {
      return column.key;
    });
    if (state.data.rows.length > 0) {
      state.selectedRowId = state.data.rows[0].id;
    }
    render();
  }

  function render() {
    var app = document.getElementById("app");
    if (!app) return;
    app.innerHTML = "";

    var filteredRows = getFilteredRows();
    var selectedRow = getSelectedRow();

    var shell = h("div", { className: "shell" }, [
      renderHeader(),
      h("div", { className: "content-grid" }, [
        h("div", { className: "left-column" }, [
          renderReviewPanel(filteredRows),
          renderPriorityPanel(filteredRows),
          h(
            "div",
            { className: "footer-note" },
            "Portable static HTML report generated locally from review-data.json. No network requests required.",
          ),
        ]),
        renderDrawer(selectedRow),
      ]),
    ]);

    app.appendChild(shell);
  }

  function renderHeader() {
    var meta = state.data.meta;
    var summary = buildSummary(state.data.rows);
    return h("section", { className: "header" }, [
      h("div", { className: "header-top" }, [
        h("div", {}, [
          h("p", { className: "eyebrow" }, "Legalcode review report"),
          h("h1", { className: "title" }, meta.reportTitle || "Tabular Review"),
          h(
            "p",
            { className: "subtitle" },
            "Portable report surface for folder-based legal review with citation-backed cells, verification states, and follow-up triage.",
          ),
        ]),
      ]),
      h("div", { className: "meta-grid" }, [
        metaCard("Run", meta.runId || "N/A"),
        metaCard("Generated", formatDateTime(meta.generatedAt)),
        metaCard("Corpus", meta.corpusLabel || "Unlabeled corpus"),
        metaCard("Execution", meta.executionPath || "manual"),
      ]),
      h("div", { className: "metrics-grid" }, [
        metricCard("Documents", String(meta.documentCount || state.data.rows.length)),
        metricCard("Columns", String(meta.columnCount || state.data.columns.length)),
        metricCard("Verified", String(summary.verified)),
        metricCard("Needs Review", String(summary.needs_review)),
        metricCard("Conflicts", String(summary.conflict)),
        metricCard("Failures", String(summary.failed)),
      ]),
    ]);
  }

  function renderReviewPanel(rows) {
    return h("section", { className: "panel" }, [
      h("div", { className: "panel-head" }, [
        h("div", {}, [
          h("div", { className: "section-label" }, "Main review"),
          h("h2", { className: "panel-title" }, "Review grid"),
        ]),
        h("div", { className: "meta-label" }, rows.length + " visible rows"),
      ]),
      renderToolbar(),
      renderTable(rows),
    ]);
  }

  function renderToolbar() {
    var filters = state.filters;
    var sourceGroups = uniqueValues(
      state.data.rows.map(function (row) {
        return row.sourceGroup;
      }),
    );
    var documentTypes = uniqueValues(
      state.data.rows.map(function (row) {
        return row.documentType;
      }),
    );

    return h("div", { className: "toolbar" }, [
      h("div", { className: "toolbar-row grow" }, [
        input({
          value: filters.q,
          placeholder: "Search documents and answers",
          onInput: function (event) {
            state.filters.q = event.target.value;
            render();
          },
        }),
        select({
          value: filters.status,
          options: [{ label: "All statuses", value: "" }].concat(
            STATUS_ORDER.map(function (value) {
              return { label: prettifyStatus(value), value: value };
            }),
          ),
          onChange: function (event) {
            state.filters.status = event.target.value;
            render();
          },
        }),
        select({
          value: filters.sourceGroup,
          options: [{ label: "All source groups", value: "" }].concat(
            sourceGroups.map(function (value) {
              return { label: value, value: value };
            }),
          ),
          onChange: function (event) {
            state.filters.sourceGroup = event.target.value;
            render();
          },
        }),
        select({
          value: filters.documentType,
          options: [{ label: "All document types", value: "" }].concat(
            documentTypes.map(function (value) {
              return { label: value, value: value };
            }),
          ),
          onChange: function (event) {
            state.filters.documentType = event.target.value;
            render();
          },
        }),
      ]),
      h("div", { className: "toolbar-row" }, [
        h(
          "button",
          {
            className: "button secondary",
            type: "button",
            onclick: function () {
              state.filters = { q: "", status: "", sourceGroup: "", documentType: "" };
              render();
            },
          },
          "Reset filters",
        ),
      ]),
      h("div", { className: "toolbar-row" }, [
        h("div", { className: "section-label" }, "Visible columns"),
        h(
          "div",
          { className: "column-toggle" },
          state.data.columns.map(function (column) {
            var checked = state.visibleColumnKeys.indexOf(column.key) !== -1;
            return h("label", { className: "column-chip" }, [
              checkbox({
                checked: checked,
                onChange: function (event) {
                  toggleColumn(column.key, event.target.checked);
                },
              }),
              h("span", {}, column.label),
            ]);
          }),
        ),
      ]),
    ]);
  }

  function renderTable(rows) {
    var columns = getVisibleColumns();
    if (rows.length === 0) {
      return h("div", { className: "empty-state" }, "No rows match the current filters.");
    }

    return h("div", { className: "table-wrap" }, [
      h("table", { className: "review-table" }, [
        h("thead", {}, [
          h(
            "tr",
            {},
            [sortHeader("Document", "documentName"), sortHeader("Status", "overallStatus")].concat(
              columns.map(function (column) {
                return sortHeader(column.label, "cell:" + column.key);
              }),
            ),
          ),
        ]),
        h(
          "tbody",
          {},
          rows.map(function (row) {
            return h(
              "tr",
              {},
              [
                h("td", { className: "doc-cell" }, [
                  h(
                    "button",
                    {
                      className: "cell-button",
                      type: "button",
                      onclick: function () {
                        state.selectedRowId = row.id;
                        state.selectedColumnKey = null;
                        render();
                      },
                    },
                    [
                      h("div", { className: "doc-name" }, row.documentName || row.id),
                      h(
                        "div",
                        { className: "doc-meta" },
                        [row.documentType, row.sourceGroup].filter(Boolean).join(" • "),
                      ),
                    ],
                  ),
                ]),
                h("td", {}, [
                  h("div", { className: "cell-meta" }, [statusBadge(row.overallStatus)]),
                ]),
              ].concat(
                columns.map(function (column) {
                  return renderCell(row, column.key);
                }),
              ),
            );
          }),
        ),
      ]),
    ]);
  }

  function renderCell(row, columnKey) {
    var cell = (row.cells && row.cells[columnKey]) || null;
    if (!cell) {
      return h("td", {}, [h("div", { className: "cell-empty" }, "Not available")]);
    }

    return h("td", {}, [
      h(
        "button",
        {
          className: "cell-button",
          type: "button",
          onclick: function () {
            state.selectedRowId = row.id;
            state.selectedColumnKey = columnKey;
            render();
          },
        },
        [
          h(
            "div",
            { className: cell.answer ? "cell-answer" : "cell-empty" },
            cell.answer || prettifyStatus(cell.status),
          ),
          h("div", { className: "cell-meta" }, [
            statusBadge(cell.status),
            confidenceBadge(cell.confidence),
          ]),
        ],
      ),
    ]);
  }

  function renderPriorityPanel(filteredRows) {
    var items = buildPriorityItems(filteredRows).slice(0, 10);
    return h("section", { className: "panel" }, [
      h("div", { className: "panel-head" }, [
        h("div", {}, [
          h("div", { className: "section-label" }, "Triage"),
          h("h2", { className: "panel-title" }, "Priority follow-ups"),
        ]),
      ]),
      h(
        "div",
        { className: "priority-list" },
        items.length === 0
          ? [h("div", { className: "empty-state" }, "No follow-up items in the current view.")]
          : items.map(function (item) {
              return h("div", { className: "priority-item" }, [
                h("div", { className: "priority-top" }, [
                  h("span", { className: "priority-doc" }, item.documentName),
                  statusBadge(item.status),
                ]),
                h("div", {}, item.label),
                h("div", { className: "priority-copy" }, item.copy),
              ]);
            }),
      ),
    ]);
  }

  function renderDrawer(row) {
    var selected = getSelectedCell(row);
    var body = row
      ? renderDrawerBody(row, selected)
      : [
          h(
            "div",
            { className: "drawer-body" },
            "Select a document or cell to inspect its evidence.",
          ),
        ];

    return h(
      "aside",
      {
        className: "drawer",
        "data-empty": row ? "false" : "true",
      },
      [
        h(
          "div",
          { className: "drawer-card" },
          [
            h("div", { className: "drawer-head" }, [
              h("div", { className: "section-label" }, selected ? "Selected cell" : "Selected row"),
              h("h2", { className: "drawer-title" }, row ? row.documentName : "Nothing selected"),
              h(
                "p",
                { className: "drawer-subtitle" },
                row
                  ? [row.documentType, row.sourceGroup, row.documentPath]
                      .filter(Boolean)
                      .join(" • ")
                  : "",
              ),
            ]),
          ].concat(body),
        ),
      ],
    );
  }

  function renderDrawerBody(row, selected) {
    var blocks = [
      h("div", { className: "drawer-body" }, [
        h("div", { className: "drawer-block" }, [
          h("h4", {}, "Document status"),
          h("div", { className: "cell-meta" }, [statusBadge(row.overallStatus)]),
        ]),
        h("div", { className: "drawer-block" }, [
          h("h4", {}, "Document metadata"),
          h("div", { className: "kv-list" }, [
            kvRow("Path", row.documentPath || "Not provided"),
            kvRow("Type", row.documentType || "Unknown"),
            kvRow("Source group", row.sourceGroup || "Unlabeled"),
          ]),
        ]),
      ]),
    ];

    if (selected) {
      blocks[0].appendChild(
        h(
          "div",
          { className: "drawer-block" },
          [
            h("h4", {}, selected.column.label),
            h("div", { className: "cell-meta" }, [
              statusBadge(selected.cell.status),
              confidenceBadge(selected.cell.confidence),
            ]),
            kvRow("Answer", selected.cell.answer || prettifyStatus(selected.cell.status)),
            kvRow(
              "Source anchor",
              formatSourceAnchor(selected.cell.source || {}) || "No source anchor provided",
            ),
            selected.cell.notes ? kvRow("Notes", selected.cell.notes) : null,
            selected.cell.source && selected.cell.source.quote
              ? h("div", { className: "source-quote" }, selected.cell.source.quote)
              : h("div", { className: "source-quote" }, "No supporting quote provided."),
          ].filter(Boolean),
        ),
      );
    }

    return blocks;
  }

  function getFilteredRows() {
    var rows = state.data.rows.slice();
    var filters = state.filters;
    if (filters.q) {
      const query = filters.q.toLowerCase();
      rows = rows.filter(function (row) {
        if ((row.documentName || "").toLowerCase().indexOf(query) !== -1) return true;
        return getVisibleColumns().some(function (column) {
          var cell = row.cells && row.cells[column.key];
          return cell && (cell.answer || "").toLowerCase().indexOf(query) !== -1;
        });
      });
    }
    if (filters.status) {
      rows = rows.filter(function (row) {
        return row.overallStatus === filters.status;
      });
    }
    if (filters.sourceGroup) {
      rows = rows.filter(function (row) {
        return row.sourceGroup === filters.sourceGroup;
      });
    }
    if (filters.documentType) {
      rows = rows.filter(function (row) {
        return row.documentType === filters.documentType;
      });
    }
    return sortRows(rows);
  }

  function sortRows(rows) {
    var sort = state.sort;
    var direction = sort.direction === "asc" ? 1 : -1;
    return rows.sort(function (left, right) {
      var leftValue = getSortValue(left, sort.key);
      var rightValue = getSortValue(right, sort.key);
      if (leftValue < rightValue) return -1 * direction;
      if (leftValue > rightValue) return 1 * direction;
      return 0;
    });
  }

  function getSortValue(row, sortKey) {
    if (sortKey === "documentName") return (row.documentName || "").toLowerCase();
    if (sortKey === "overallStatus") return STATUS_ORDER.indexOf(row.overallStatus);
    if (sortKey.indexOf("cell:") === 0) {
      const key = sortKey.slice(5);
      const cell = row.cells && row.cells[key];
      if (!cell) return "";
      if (cell.answer) return String(cell.answer).toLowerCase();
      return STATUS_ORDER.indexOf(cell.status);
    }
    return "";
  }

  function getVisibleColumns() {
    return state.data.columns.filter(function (column) {
      return state.visibleColumnKeys.indexOf(column.key) !== -1;
    });
  }

  function toggleColumn(columnKey, isVisible) {
    if (isVisible && state.visibleColumnKeys.indexOf(columnKey) === -1) {
      state.visibleColumnKeys = state.visibleColumnKeys.concat([columnKey]);
    }
    if (!isVisible) {
      state.visibleColumnKeys = state.visibleColumnKeys.filter(function (key) {
        return key !== columnKey;
      });
      if (state.selectedColumnKey === columnKey) {
        state.selectedColumnKey = null;
      }
    }
    render();
  }

  function getSelectedRow() {
    return (
      state.data.rows.find(function (row) {
        return row.id === state.selectedRowId;
      }) || null
    );
  }

  function getSelectedCell(row) {
    if (!row || !state.selectedColumnKey) return null;
    var cell = row.cells && row.cells[state.selectedColumnKey];
    if (!cell) return null;
    var column = state.data.columns.find(function (item) {
      return item.key === state.selectedColumnKey;
    });
    return {
      cell: cell,
      column: column || { key: state.selectedColumnKey, label: state.selectedColumnKey },
    };
  }

  function buildPriorityItems(rows) {
    var items = [];
    rows.forEach(function (row) {
      Object.keys(row.cells || {}).forEach(function (columnKey) {
        var cell = row.cells[columnKey];
        if (!cell) return;
        if (["needs_review", "conflict", "failed"].indexOf(cell.status) === -1) return;
        var column = state.data.columns.find(function (item) {
          return item.key === columnKey;
        });
        items.push({
          status: cell.status,
          documentName: row.documentName || row.id,
          label: column ? column.label : columnKey,
          copy:
            cell.notes ||
            cell.answer ||
            formatSourceAnchor(cell.source || {}) ||
            "Requires review.",
        });
      });
    });
    return items.sort(function (left, right) {
      return STATUS_ORDER.indexOf(left.status) - STATUS_ORDER.indexOf(right.status);
    });
  }

  function buildSummary(rows) {
    return rows.reduce(
      function (acc, row) {
        var status = row.overallStatus || "not_found";
        acc[status] = (acc[status] || 0) + 1;
        return acc;
      },
      { verified: 0, needs_review: 0, conflict: 0, not_found: 0, failed: 0 },
    );
  }

  function sortHeader(label, key) {
    var active = state.sort.key === key;
    var marker = active ? (state.sort.direction === "asc" ? "↑" : "↓") : "↕";
    return h("th", {}, [
      h(
        "button",
        {
          type: "button",
          onclick: function () {
            if (state.sort.key === key) {
              state.sort.direction = state.sort.direction === "asc" ? "desc" : "asc";
            } else {
              state.sort.key = key;
              state.sort.direction = "asc";
            }
            render();
          },
        },
        [h("span", {}, label), h("span", { className: "meta-label" }, marker)],
      ),
    ]);
  }

  function metaCard(label, value) {
    return h("div", { className: "meta-card" }, [
      h("div", { className: "meta-label" }, label),
      h("div", { className: "meta-value" }, value),
    ]);
  }

  function metricCard(label, value) {
    return h("div", { className: "metric-card" }, [
      h("div", { className: "metric-label" }, label),
      h("strong", {}, value),
    ]);
  }

  function statusBadge(status) {
    return h(
      "span",
      { className: "status-badge status-" + (status || "not_found") },
      prettifyStatus(status || "not_found"),
    );
  }

  function confidenceBadge(confidence) {
    var value = confidence || "unknown";
    return h("span", { className: "confidence-badge" }, value);
  }

  function kvRow(key, value) {
    return h("div", { className: "kv-row" }, [
      h("div", { className: "kv-key" }, key),
      h("div", { className: "kv-value" }, value),
    ]);
  }

  function input(options) {
    var node = document.createElement("input");
    node.className = "input";
    node.type = "search";
    node.value = options.value || "";
    node.placeholder = options.placeholder || "";
    node.addEventListener("input", options.onInput);
    return node;
  }

  function select(options) {
    var node = document.createElement("select");
    node.className = "select";
    (options.options || []).forEach(function (option) {
      var optionNode = document.createElement("option");
      optionNode.value = option.value;
      optionNode.textContent = option.label;
      if (option.value === options.value) optionNode.selected = true;
      node.appendChild(optionNode);
    });
    node.addEventListener("change", options.onChange);
    return node;
  }

  function checkbox(options) {
    var node = document.createElement("input");
    node.type = "checkbox";
    node.checked = Boolean(options.checked);
    node.addEventListener("change", options.onChange);
    return node;
  }

  function h(tagName, props, children) {
    var node = document.createElement(tagName);
    if (props) {
      Object.keys(props).forEach(function (key) {
        var value = props[key];
        if (value === null || value === undefined) return;
        if (key === "className") {
          node.className = value;
          return;
        }
        if (key === "onclick") {
          node.addEventListener("click", value);
          return;
        }
        node.setAttribute(key, value);
      });
    }
    var childList = Array.isArray(children) ? children : [children];
    childList.forEach(function (child) {
      if (child === null || child === undefined || child === false) return;
      if (typeof child === "string" || typeof child === "number") {
        node.appendChild(document.createTextNode(String(child)));
      } else {
        node.appendChild(child);
      }
    });
    return node;
  }

  function prettifyStatus(status) {
    return String(status || "unknown").replace(/_/g, " ");
  }

  function uniqueValues(values) {
    return Array.from(
      values.reduce(function (set, value) {
        if (value) set.add(value);
        return set;
      }, new Set()),
    ).sort();
  }

  function formatDateTime(value) {
    if (!value) return "Unknown";
    var date = new Date(value);
    if (Number.isNaN(date.getTime())) return String(value);
    return date.toLocaleString();
  }

  function formatSourceAnchor(source) {
    var bits = [];
    if (source.page !== undefined && source.page !== null && source.page !== "")
      bits.push("p. " + source.page);
    if (source.section) bits.push("§ " + source.section);
    if (source.heading) bits.push(source.heading);
    return bits.join(" • ");
  }

  boot();
})();
