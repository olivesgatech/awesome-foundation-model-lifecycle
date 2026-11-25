# Contributing

This collection organizes resources by their role in the foundation model lifecycle. A contribution should help readers understand what changes, what is measured, and what evidence is passed to the next stage.

## Add a paper

1. Choose an existing topic in `data/taxonomy.json`.
2. Add a record to `data/papers.json` with a unique, stable lowercase ID, full title, authors, year, venue/source label and primary URL.
3. Write one short original sentence explaining lifecycle relevance. Avoid unsupported superlatives or leaderboard claims.
4. Set `origin` to `survey` only if the supplied manuscript actually cites the work, and include its section(s). Otherwise use `addition`.
5. Record a metadata check date and source. Add a code link only when it is attributable to the authors or project; label third-party reproductions explicitly if supported in a future schema.
6. Regenerate the README catalog and BibTeX, then validate:

```bash
python3 scripts/build_catalog.py
python3 scripts/validate.py
```

The scripts use Python's standard library and require Python 3.10 or later. No model downloads, GPU, credentials or external packages are required. Do not edit the generated README catalog block or `references.bib` directly; surrounding README prose is maintained by hand.

## Review questions

- Does the primary source match the title, authors and publication version?
- Does the work improve a representation, adapt behavior, measure failure, or support system maintenance?
- Is it a method, dataset, benchmark or broader framework? What can and cannot be concluded from its results?
- If it acts at inference, does it change the model/context or only diagnose the output?
- What access, labels, calibration data, auxiliary training or compute does it require?
- What must be preserved when it is applied?

## Corrections

Use the correction issue template for broken links, attribution, metadata, or lifecycle classification. Cite the primary record supporting the change. Avoid replacing an earlier version with a newer paper that has a different scope simply because the names are similar.

## Figures and reuse

Use original exports, descriptive alt text, and source attribution. Follow the [figure plan](assets/figures/README.md). Linked publications and code remain governed by their own terms; see [LICENSE.md](LICENSE.md) for the repository's license (CC BY-NC 4.0).
