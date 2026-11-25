# Reading paths

[Back to the collection](../README.md)

Each route emphasizes a question rather than promising that one family of techniques solves every robustness problem.

## A 12-paper introduction

| Order | Read | Question to carry forward |
| --- | --- | --- |
| 1 | [On the Opportunities and Risks of Foundation Models](../README.md#bommasani2021) | How do shared foundations propagate capabilities and failures? |
| 2 | [Excessive Invariance](../README.md#jacobsen) | When should a model change its answer? |
| 3 | [SimCLR](../README.md#simclr) | What do the encoder and projector each learn? |
| 4 | [VICReg](../README.md#vicreg) | Which objectives prevent collapsed representations? |
| 5 | [AdaDim](../README.md#adadim) | How do those objectives interact over training time? |
| 6 | [CLIP](../README.md#clip) | How does a learned representation support cross-modal and zero-shot use? |
| 7 | [LoRA](../README.md#lora) | What can be adapted without updating the full backbone? |
| 8 | [DPO](../README.md#dpo) | What does preference optimization change after pretraining? |
| 9 | [GradTrust](../README.md#gradtrust) | What information is available for questioning a completed prediction? |
| 10 | [Calibration](../README.md#calibration) | Why is confidence different from correctness and calibration? |
| 11 | [HarmBench](../README.md#harmbench) | How should systematic failure discovery feed the next update? |
| 12 | [AI RMF 1.0](../README.md#nistrmf) | Who owns the decisions, evidence and follow-up across the lifecycle? |

Read Chapters 1 and 8 of the manuscript before and after this route to keep the model-level papers connected to the overall system.

## Representation geometry and training dynamics

[Information bottleneck](../README.md#informationbottleneck) → [alignment/uniformity](../README.md#alignmentuniformity) → [dimensional collapse](../README.md#collapse) → [RankMe](../README.md#rankme) → [AdaDim](../README.md#adadim) → [HEX](../README.md#hex) → [R3D](../README.md#r3d).

**Exercise:** design an evaluation where two checkpoints have similar probe accuracy but different local rank or sensor dependence. Specify what additional evidence determines which checkpoint to adapt.

## Vision and domain-specific foundation models

[ViT](../README.md#vit) → [DINOv2](../README.md#dinov2) → [SAM](../README.md#sam) → [PointPrompt](../README.md#pointprompt) → [prompt benchmarking](../README.md#promptbenchmark) → [clinical OCT](../README.md#clinicaloct) → [fault benchmark](../README.md#faultbenchmark).

**Exercise:** distinguish a failed prompt, an inadequate task head, and a missing representation in an out-of-domain segmentation example.

## Language-model adaptation and post-training

[Few-shot learning](../README.md#gpt3) → [retrieval](../README.md#rag) → [LoRA](../README.md#lora) → [InstructGPT](../README.md#instructgpt) → [DPO](../README.md#dpo) → [ROME](../README.md#rome) → [ReFT](../README.md#reft).

**Exercise:** for a factual update, compare changing the retrieval corpus, an adapter, a memory, and base weights. Define efficacy and preservation tests for each.

## Failure detection, explanations, and uncertainty

[Softmax baseline](../README.md#msp) → [calibration](../README.md#calibration) → [GradPurview](../README.md#gradpurview) → [GradTrust](../README.md#gradtrust) → [explanatory paradigms](../README.md#explanatoryparadigms) → [introspective learning](../README.md#introspective) → [VOICE](../README.md#voice) → [conformal prediction](../README.md#conformal).

**Exercise:** design a human-handoff policy. Separate score estimation, threshold fitting, decision cost and evaluation on held-out shifts.

## Deployment and continuous improvement

[WILDS](../README.md#wilds) → [HarmBench](../README.md#harmbench) → [XSTest](../README.md#xstest) → [CoTTA](../README.md#cotta) → [EWC](../README.md#ewc) → [machine unlearning](../README.md#unlearning) → [model cards](../README.md#modelcards) → [AI RMF](../README.md#nistrmf).

**Exercise:** write a release record for one model update, including which failures motivated it, which components changed, what regressed, and how it can be rolled back.

## Suggested seminar sequence

| Meeting | Manuscript | Focus |
| --- | --- | --- |
| 1 | Chapter 1 | The learning–robustness tradeoff and target-preserving versus target-changing interventions |
| 2 | Chapter 2 | Representation quality, collapse and training dynamics |
| 3 | Chapter 3 | Attention, modality complementarity and sensor failure |
| 4 | Chapter 4 | What changes in adaptation, and what does the evaluator know? |
| 5 | Chapter 5 | Preferences, targeted edits and preservation |
| 6 | Chapter 6 | Detection, red teaming and response policy |
| 7 | Chapter 7 | Explanation, uncertainty and introspection |
| 8 | Chapter 8 | Sequential improvement, human interaction and accountable maintenance |
