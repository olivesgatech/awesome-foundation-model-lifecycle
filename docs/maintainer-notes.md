# Editorial and maintenance notes

[Back to the collection](../README.md)

## Source and selection

The source was the 217-page file supplied as `NOW_FrontTrendsCG_V_Ghassan_Mohit_2025_Proposal (1).pdf`. Its cover and copyright year identify a 2026 manuscript despite the filename. All eight chapters, the glossary, and the bibliography informed this collection. The source PDF is not redistributed.

The initial catalog is selective. It prioritizes lifecycle mechanisms, the manuscript's case studies and established comparison baselines. It excludes many peripheral citations and adoption statistics. Every record declares whether it is cited in the source manuscript or added by the curator. Chapter positions are curated manually.

Primary links were checked on **2026-10-05 UTC**. For papers on arXiv or conference/journal pages, titles and author metadata were checked against those sources. Versioned NIST reports and the two Transformer Circuits articles were reviewed using their primary sources. Conference/journal labels use the manuscript or a confirmed publication record; links may point to an earlier author preprint. The per-entry check records distinguish a bibliographic check from a claim of experimental reproduction.

## Differences and boundaries to retain

| Item | Repository treatment |
| --- | --- |
| Draft survey publication fields | Omit placeholder DOI, volume, issue and pages; retain a clearly labeled unpublished citation until final metadata is available |
| Figure 1.2 versus the robustness taxonomy | Label it as pretraining, task-head training and alignment, with the latter two under a posteriori; do not relabel alignment as post hoc |
| HEX appears in Chapter 5 | Cross-reference its alignment motivation but place the training regularizer under a priori SSL |
| Information Router appears in architectural discussions | Its primary paper evaluates LoRA fine-tuning with MoIR; place it under a posteriori adaptation and retain the chapter cross-reference |
| R3D versus RTF | R3D is the action-anticipation framework; RTF names the Rank-enhancing Token Fuser component |
| PointPrompt venue | Use CVPR **Workshops** 2024, as specified by its primary conference page |
| Scaling Monosemanticity | Link the original 2024 Transformer Circuits article; the supplied bibliography lists a 2026 arXiv version |
| Duplicate versions in the bibliography | Use one record for a work such as HEX or the common-corruption benchmark; distinguish preprint and publication years in metadata rather than duplicating entries |
| VOICE | Keep its induced-contrastive-explanation formulation; do not present generic saliency perturbation variance as an implementation of VOICE |
| Figure 7.3 attribution | Ask the authors to reconcile the caption's GradTrust citation with the section's VOICE citation before inserting the figure |
| Confidence scores | Do not reproduce a universal increase/decrease rule from a mixed-method table; validate each method's score direction and threshold convention |
| MC dropout, DUQ and introspective learning | State their model/training requirements; inference-time use does not make them arbitrary training-free plug-ins |
| Representation rank and attention | Treat these as mechanisms/diagnostics, not unconditional robustness guarantees |
| Privacy and regulation | Link versioned primary technical/governance sources; omit broad legal claims and changing compliance summaries |
| Adoption and trust | Include human/system evaluation questions, without interpreting popularity as evidence of model correctness |

## Before public release

- [ ] **TODO:** add the survey's public URL in the README and draft citation page.
- [ ] **TODO:** replace draft citation fields with the final publication metadata in `CITATION.cff` and `docs/citation.md`.
- [ ] **TODO:** select a public reuse license for the repository's original text, metadata and scripts.
- [ ] **TODO:** insert the desired manuscript figures using the [figure plan](../assets/figures/README.md).
- [ ] Add the GitHub URL to the repository metadata and update the optional clone instructions after the repository exists.

The unresolved items require author-owned publication or release choices. The catalog, bibliography, navigation, contribution flow and validation scripts are complete without the optional images.

## What has and has not been verified

The supplied package includes a [build-time validation report](../validation-report.json). Local checks cover catalog fields, unique identifiers and paper links, generated-content consistency, citation keys, local Markdown links/anchors and archive contents. Bibliographic checks do not establish that every linked implementation reproduces its paper, nor that a method generalizes beyond the published experiments. External links can change after the recorded check date.

Do not add leaderboard values without recording the exact benchmark, model version, split, threat model, adaptation access and evaluation date. Prefer durable paper or project links over scraped rankings.

## Maintenance cycle

Review new entries by lifecycle relevance, verify primary metadata, record provenance, and run the generator and validator. Periodically review external URLs and publication-version changes. When the companion manuscript changes, update `docs/paper-map.md`, figure page numbers and survey section markers together.
