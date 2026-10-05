# Map from the manuscript to the repository

[Back to the collection](../README.md)

Page numbers below are the manuscript's **printed page numbers**. Add four to obtain the one-based PDF page number in the supplied 217-page file. This map covers all eight chapters; the catalog intentionally selects references rather than duplicating the entire bibliography.

| Manuscript location | Main ideas retained | Repository destination |
| --- | --- | --- |
| §1.1, pp. 4–17 | Information bottleneck; primary and secondary robustness; reliability, sensitivity, stability and resilience; accuracy–robustness tradeoffs | [Foundations](../README.md#foundations), [terminology](lifecycle.md#primary-and-secondary-robustness) |
| §§1.2–1.4, pp. 17–22 | Foundation models beyond LLMs; reuse and homogenization; a priori, a posteriori, post hoc and ad hoc | [Lifecycle guide](lifecycle.md), [survey citation](citation.md) |
| §§2.1–2.2, pp. 23–26 | SSL, pretext tasks, encoder/projector distinction, contrastive objectives | [SSL collection](../README.md#ssl) |
| §§2.3–2.4, pp. 26–31 | Dimensionality, effective rank, direct/indirect/targeted evaluation | [Representation evaluation](benchmarks.md#representation-and-fusion) |
| §2.5, pp. 31–37 | Training dynamics of representation entropy and encoder–projector information; AdaDim | [AdaDim case study](case-studies.md#adadim) |
| §§3.1–3.4, pp. 40–49 | Tokenization, position, self/cross-attention and normalization | [Architectures](../README.md#architecture) |
| §§3.5–3.6, pp. 49–62 | Fusion, feature versus modal collapse, multimodal information bottleneck, rank-targeted action anticipation | [R3D case study](case-studies.md#r3d), [fusion evaluation](benchmarks.md#representation-and-fusion) |
| §§4.1–4.3, pp. 63–69 | Linear/GP/transformer heads; SFT, PEFT, supervised contrastive learning; DA and DG | [Adaptation](../README.md#adaptation), [adaptation controls](benchmarks.md#adaptation-alignment-and-editing) |
| §4.4, pp. 69–71 | TTA and ICL; what can change when training data or weights are unavailable | [Stage boundaries](lifecycle.md#boundaries-worth-preserving) |
| §§4.5–4.7, pp. 71–78 | SAM prompting, clinical biomarker transfer, seismic preprocessing and domain shift | [SAM, OCT and seismic cases](case-studies.md#sam-oct-and-seismic-transfer) |
| §§5.1–5.2, pp. 80–86 | Preferences versus similarity; human representation alignment; RLHF and DPO | [Alignment](../README.md#alignment) |
| §5.3, pp. 86–90 | Hierarchical structure, cosine-similarity grouping and HEX | [HEX case study](case-studies.md#hex) |
| §§5.4–5.5.3, pp. 90–104 | Factual edits, steering, subspace edits, learned interventions, weight edits and support-set edits | [Editing collection](../README.md#editing), [intervention table](lifecycle.md#a-posteriori-what-changes-after-pretraining) |
| §5.5.4, pp. 104–106 | VOID, object effects, temporal locality and physical plausibility | [Visual editing case](case-studies.md#visual-editing-and-void) |
| §§6.1–6.2, pp. 108–116 | Failure types, access assumptions, capacity/purview, gradients versus activations, softmax baseline | [Failure detection](../README.md#detection), [access settings](lifecycle.md#post-hoc-what-should-be-questioned) |
| §6.3, pp. 116–124 | Misprediction detection, confidence ranking, AUAC/AUFC, GradTrust | [Gradient diagnostics](case-studies.md#gradient-diagnostics), [detection metrics](benchmarks.md#failure-detection-and-selective-prediction) |
| §§6.4–6.5, pp. 124–131 | Monitoring, policy actions, mitigation feedback, jailbreak evaluation and layered defenses | [Red teaming](../README.md#redteaming), [feedback loop](lifecycle.md#close-the-loop) |
| §§7.1–7.3, pp. 132–143 | Observed correlation, counterfactual and contrastive explanations; introspective learning | [Transparency](../README.md#transparency), [introspection case](case-studies.md#introspection) |
| §§7.4–7.7, pp. 143–153 | Uncertainty definitions, sources, calibration, dropout, geometric and gradient signals | [Uncertainty](../README.md#uncertainty) |
| §7.8, pp. 153–155 | Uncertainty in explanations and VOICE | [VOICE case](case-studies.md#voice) |
| §8.1, pp. 156–161 | Mechanistic interpretation, continual learning, antifragility and multimodal interaction | [Circuits](../README.md#circuits), [feedback](../README.md#feedback), [sequential evaluation](benchmarks.md#sequential-and-socio-technical-evaluation) |
| §8.2, pp. 161–162 | Historical roles of augmentation, dropout and residual architectures | [Foundations](../README.md#foundations); background for the lifecycle paths |
| §§8.3–8.4, pp. 162–169 | Reproducibility, fairness, accountability, privacy, monitoring and socio-technical interfaces | [Governance collection](../README.md#governance), [operational evidence](benchmarks.md#sequential-and-socio-technical-evaluation) |
| §8.5, pp. 169–174 | Adoption, education, public acceptance and appropriate trust | [Human/system evaluation](benchmarks.md#sequential-and-socio-technical-evaluation); adoption counts are not used as robustness scores |
| §8.6, pp. 174–181 | Collected terminology | [Lifecycle guide](lifecycle.md); definitions are paraphrased rather than reproduced |

## Deliberate additions

The repository adds data curation and deduplication, DINO/MAE/CLIP/ImageBind, practical PEFT baselines, TENT and retrieval, standardized cross-domain evaluation, over-refusal testing, explanation sanity checks, semantic uncertainty, dataset/model documentation, and maintenance literature. Each added paper carries an **Added** marker so it is not presented as a manuscript citation.

The [editorial notes](maintainer-notes.md) record boundaries and metadata changes that matter for this mapping.
