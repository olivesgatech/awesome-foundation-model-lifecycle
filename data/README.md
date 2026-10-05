# Catalog data

`papers.json` is the source of truth for the generated README entries and bibliography. `taxonomy.json` defines the ordered topics and their primary lifecycle placement.

| Field | Meaning |
| --- | --- |
| `id` | Stable identifier used for the README anchor and BibTeX key |
| `title`, `authors`, `year`, `venue` | Selected bibliographic version; a linked preprint may have an earlier date |
| `url` | Primary paper, publisher, author article or institutional report URL |
| `origin` | `survey` for a work cited in the supplied manuscript, otherwise `addition` |
| `survey_sections` | Manually mapped manuscript sections; empty for an addition |
| `stage`, `topic` | Primary editorial placement; this is not an exclusive claim about possible applications |
| `annotation` | Short original explanation of lifecycle relevance |
| `verification` | Date, primary source URL, source title, HTTP status and metadata-check method |
| `code_url` | Optional author/project implementation or resource link |
| `code_verification` | Optional reachability check and project-page title; does not mean the code was executed |
| `cross_stage_note` | Optional qualification for mechanisms that cross lifecycle boundaries |

Names follow primary-source metadata. A literal `others` in an author list denotes abbreviated authorship, not a person's name. Braces around an institutional author preserve its corporate identity in BibTeX.

Use `python3 scripts/build_catalog.py` from the repository root after edits. `python3 scripts/validate.py` checks the catalog, generated output, BibTeX keys and local Markdown navigation without network access. No third-party Python packages are needed.
