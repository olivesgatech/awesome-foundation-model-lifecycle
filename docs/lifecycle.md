# A lifecycle guide to foundation model robustness

[Back to the collection](../README.md)

The manuscript's central move is to organize robustness by its relationship to learning. That makes a deployment failure traceable to earlier choices and gives later monitoring a role in future development. The categories below are the manuscript's organizing vocabulary, not a claim that all cited authors use the same terms.

## Two questions before selecting a method

**What is allowed to change?** A model can encounter a nuisance perturbation that should leave the target unchanged, or a meaningful intervention that should change the target. The same numerical perturbation size can represent either case in different applications.

**What can the evaluator observe or modify?** An API consumer, a model developer, and an operator with access to training data have different options. Gradient diagnostics require a differentiable model and suitable access; output-only monitoring does not provide the same information.

## Primary and secondary robustness

| Manuscript concept | Desired behavior | Example | Evaluation implication |
| --- | --- | --- | --- |
| Primary robustness | Preserve an appropriate decision under label-preserving variation | A small brightness change should not change an object's class | Compare against the unchanged target within a justified perturbation set |
| Secondary robustness | Respond consistently when the correct target changes | Moving an object should move its segmentation mask; a meaningful measurement change may change a regression target | Compare against the target appropriate to the changed input |

For intuition, let `G(x)` be the target and `f(x)` the prediction. Comparing `f(x + delta)` with `G(x)` answers a different question from comparing it with `G(x + delta)`. If the two targets differ, invariance can be the wrong objective. This is a conceptual reading of Chapter 1, not a restatement or certification of its formal bounds.

The [excessive-invariance](../README.md#jacobsen), [accuracy–robustness tradeoff](../README.md#tsipras), and [TRADES](../README.md#trades) papers help make these distinctions concrete. A meaningful target transformation may be difficult to define for generated text or video; record the semantic or task-specific criterion rather than assuming a pixel norm transfers to every modality.

## A priori: what will be learned?

**Chapters 2–3.** Choose data, pretext tasks, architectures, and fusion mechanisms before or during representation learning. The encoder and its SSL projector have different jobs; an objective that improves one representation statistic need not improve all downstream tasks.

The manuscript's distinctive questions include:

- Does the representation collapse globally or within local semantic groups?
- Is effective rank changing because features decorrelate, samples spread out, or both?
- How do encoder representations and projector embeddings evolve together?
- Does a fused representation preserve complementary information from each modality?
- Does a high-rank fused representation still depend almost entirely on one sensor?

Useful evidence includes eigenspectra, effective rank, local/global comparisons, transfer across tasks, and missing-modality experiments. Pair these diagnostics with downstream performance. Rank can increase without improving the task, and improved average performance can hide modal collapse.

**Handoff:** checkpoint and dataset versions, pretraining objective, representation diagnostics, transfer settings, known missing concepts, and modality assumptions.

## A posteriori: what changes after pretraining?

**Chapters 4–5.** Adapt an existing representation using labels, preferences, interaction, or targeted corrections. This includes head training, fine-tuning, LoRA and adapters, domain adaptation, preference optimization, model editing, and conditioning through prompts or retrieval.

| Mechanism | Typical change | Preservation question |
| --- | --- | --- |
| Linear probe | Task head | Is the frozen representation useful under the actual domain shift? |
| Full fine-tuning | Many base-model parameters | Which previous capabilities or subgroups regress? |
| LoRA or adapters | Added parameters or low-rank updates | What changes when adapters are enabled, combined, or removed? |
| RLHF / DPO | Broad output preferences | Does alignment transfer to unseen prompts without excessive refusal or capability loss? |
| Factual/model editing | Selected weights, memories, or local behavior | Does the edit generalize correctly and leave unrelated behavior intact? |
| Activation steering / ReFT | Hidden states or learned representation interventions | Is the effect context-dependent, stable, and reversible? |
| In-context learning / retrieval | Context or external knowledge | Does evidence quality, prompt order, or retrieved content alter reliability? |
| Test-time adaptation | Selected parameters or statistics during deployment | Does a changing or contaminated test stream cause forgetting or confirmation bias? |

**Handoff:** adaptation data and version, changed components, intended scope, preservation set, prompt protocol, evaluation slices, and rollback option.

## Post hoc: what should be questioned?

**Chapters 6–7.** Assess a trained model, identify failures, and support a response policy. This includes misprediction detection, OOD detection, anomaly/novelty detection, adversarial testing, explanations, calibration, and uncertainty assessment.

| Access setting | Feasible examples | Constraints to record |
| --- | --- | --- |
| Input/output access | Prompt suites, semantic response consistency, external response scoring, human review | Query budget, sampling settings, model version and response stochasticity |
| Logits/probabilities | Softmax, entropy, margin, energy scores, temperature scaling | Logit availability; calibration labels when fitting or validating a calibrator |
| Representations | Feature-distance detectors, rank diagnostics, representation probes | Layer, extraction procedure, reference data and distance assumptions |
| Gradients | GradNorm, GradPurview, GradTrust, gradient explanations | Differentiable access, chosen loss, layers, counterfactual targets and compute cost |
| Training or calibration data | Class statistics, calibrated thresholds, conformal prediction, subgroup analysis | Provenance, split hygiene, representativeness and privacy constraints |

**Post hoc does not mean cost-free or universally training-free.** An auxiliary detector, calibrator, or introspective predictor may need its own fitting. Computing a gradient for a diagnostic does not require updating the base model. Deep ensembles and DUQ require suitable training even though uncertainty is read at inference. MC dropout presumes a suitable dropout configuration; inserting arbitrary dropout into any model is not equivalent to its Bayesian interpretation.

## Close the loop

1. **Detect and characterize:** distinguish bad input, missing knowledge, prompt mismatch, changed context, and integration failure.
2. **Respond:** accept, abstain, request better input, route to another model or human, or use a constrained fallback.
3. **Review evidence:** check labels, data provenance, affected populations, and whether the event is informative enough to justify learning.
4. **Choose the smallest suitable intervention:** change preprocessing, prompts, memory, thresholds, a head, an adapter, model weights, or the next pretraining dataset.
5. **Re-evaluate:** test the failure and a preservation suite; examine calibration, subgroup behavior, and sequential retention.
6. **Release and monitor:** record versions and measure recurrence, recovery, new failures, and rollback behavior.

This loop develops the operationalization in §6.4 and the continual-learning discussion in §8.1.2. The repository treats **antifragility as a research aspiration**, not a demonstrated property of all adaptive systems. Improvement on a repeated example is weaker evidence than transfer to future disturbances while retaining prior capabilities.

## Boundaries worth preserving

- **Ad hoc** describes a purpose-specific method, not a fourth chronological stage.
- **TTA and ICL** occur at inference but perform adaptation; time of execution alone does not make them detectors.
- **HEX** appears in the manuscript's alignment chapter but regularizes SSL training; its primary repository placement is a priori.
- **Alignment** is not equivalent to robustness, factual accuracy, or fairness.
- **Image/video editing** modifies generated content; model editing modifies reusable model behavior. These can share mechanisms without being interchangeable.
- **Concept erasure** and **machine unlearning** require different evidence. A suppressed response does not prove the influence of a training record has been removed.
- **An explanation** can be plausible and still unfaithful. Its stability and uncertainty need separate evaluation.
- **Governance** spans data collection through retirement or replacement; it is not only a final deployment step.

Continue with the [evaluation matrix](benchmarks.md) or [case studies](case-studies.md).
