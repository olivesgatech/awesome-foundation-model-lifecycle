# Figure insertion plan

[Back to the collection](../../README.md) · [Case studies](../../docs/case-studies.md)

The repository is readable without figure files. These TODOs identify useful additions from the supplied manuscript. Use the authors' original exports where possible; keep labels legible at GitHub's normal content width. Confirm the caption and attribution of any figure adapted from another publication.

| Priority | Figure | Printed page / PDF page | Suggested filename | Where to place it |
| --- | --- | --- | --- | --- |
| Essential | 1.2: three stages of application-specific training | 22 / 26 | `figure-1-2-training-stages.png` | Main README, after the lifecycle table |
| High | 2.4: representation/projector dynamics and trajectories | 32 / 36 | `figure-2-4-ssl-dynamics.png` | AdaDim case study |
| High | 3.2: feature and modal collapse | 49 / 53 | `figure-3-2-fusion-collapse.png` | R3D case study |
| Optional | 3.3: per-modality spectra before and after fusion | 60 / 64 | `figure-3-3-fusion-spectra.png` | R3D case study, after the conceptual figure |
| High | 4.1: clinical-label learning and biomarker-head training | 73 / 77 | `figure-4-1-clinical-transfer.png` | SAM/OCT/seismic case study |
| Optional | 5.2: HEX hierarchy-aware loss | 88 / 92 | `figure-5-2-hex.png` | HEX case study |
| Optional | 6.1: representational/effective capacity and purview | 111 / 115 | `figure-6-1-purview.png` | Gradient diagnostics case study |
| High | 6.2: activation versus gradient representations | 113 / 117 | `figure-6-2-gradient-diagnostics.png` | Gradient diagnostics case study |
| Optional | 6.4: GradTrust computation | 122 / 126 | `figure-6-4-gradtrust.png` | Gradient diagnostics case study |
| Optional | 7.1: three observed explanation paradigms | 137 / 141 | `figure-7-1-explanation-questions.png` | Introspection case study |
| High | 7.2: sensing and reflection | 139 / 143 | `figure-7-2-introspection.png` | Introspection case study |
| High | 7.3: explanation and VOICE uncertainty | 154 / 158 | `figure-7-3-voice.png` | VOICE case study; verify the source caption |

## Insertion snippets

After the first file exists, replace its TODO in the root README with:

```markdown
![Pretraining learns an encoder; task-head training and alignment adapt its use.](assets/figures/figure-1-2-training-stages.png)

*Figure 1.2 from AlRegib and Prabhushankar, supplied 2026 manuscript. This figure shows training stages; deployment monitoring is represented separately in the lifecycle schematic above.*
```

From `docs/case-studies.md`, use a parent-relative path:

```markdown
![Encoder and projector representations evolve differently during SSL training.](../assets/figures/figure-2-4-ssl-dynamics.png)

*Figure 2.4 from the companion manuscript, based on Kokilepersaud et al., AdaDim. Add the final source attribution here.*
```

Do not activate image links until their files are present. The repository validator checks that local image targets exist.
