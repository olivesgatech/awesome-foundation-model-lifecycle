# Benchmarks, metrics, and lifecycle evidence

[Back to the collection](../README.md) · [Lifecycle guide](lifecycle.md)

A benchmark measures a specified failure mode under specified conditions. A high score on one suite does not certify the whole model lifecycle. Use this matrix to assemble complementary evidence, then record what changed between checkpoints or releases.

## Representation and fusion

| Question | Resources in this collection | Evidence to collect | Important control |
| --- | --- | --- | --- |
| Does representation geometry remain useful? | [RankMe](../README.md#rankme), [LiDAR](../README.md#lidar), [AdaDim](../README.md#adadim), [HEX](../README.md#hex) | Effective rank, eigenspectra, local and global structure, frozen-probe and fine-tuning results | Fix feature normalization, sample budget, layer, head and training budget; report multiple seeds |
| Are improvements maintained across realistic shifts? | [ImageNet-C/P](../README.md#imagenetc), [WILDS](../README.md#wilds), [DomainBed](../README.md#domainbed) | Clean and shifted performance, per-domain and worst-group results | Select hyperparameters without using target test labels |
| Do both modalities contribute? | [R3D](../README.md#r3d), [DARai](../README.md#darai), [ImageBind](../README.md#imagebind) | Unimodal baselines, fused performance, per-modality/fused spectra, missing/corrupted modality tests | Evaluate dominance and diversity separately; high fused rank does not establish balanced use |
| Does data curation change downstream reliability? | [DataComp](../README.md#datacomp), [deduplication](../README.md#dedup) | Transfer suite, duplicates/contamination, dataset composition, subgroup performance | Compare at matched model and compute budgets where practical |

**ImageNet-C** measures common corruptions; **ImageNet-P** measures perturbation sequences. **WILDS** supplies naturally occurring shifts. **RobustBench** evaluates specified adversarial threat models. These are different kinds of evidence, not interchangeable robustness scores.

## Adaptation, alignment, and editing

| Setting | Resources | Evaluation dimensions | Common confound |
| --- | --- | --- | --- |
| Domain/task transfer | [LoRA](../README.md#lora), [SAM](../README.md#sam), [MedSAM](../README.md#medsam), [clinical OCT](../README.md#clinicaloct) | Adapted task accuracy/IoU/Dice, new-domain performance, preserved capabilities, parameters and compute | Different supervision or adaptation budgets presented as a method gain |
| Medical representations | [OLIVES](../README.md#olives), [clinical OCT](../README.md#clinicaloct) | Per-biomarker performance, imbalance-aware metrics, patient-level generalization | Correlated scans or the same patient appearing across evaluation splits |
| Seismic interpretation | [fault benchmark](../README.md#faultbenchmark), [CRACKS](../README.md#cracks) | Cross-survey transfer, boundary and region metrics, uncertainty under annotation disagreement | Adjacent slices shared across splits; preprocessing mismatch hidden in aggregate scores |
| Human prompting | [PointPrompt](../README.md#pointprompt), [prompt benchmark](../README.md#promptbenchmark), [BALD-SAM](../README.md#baldsam) | Quality versus number of interactions, annotator variation, spatial/prompt perturbations | Giving an automated prompter test masks or a larger interaction budget than humans |
| TTA | [Tent](../README.md#tent), [CoTTA](../README.md#cotta), [RoTTA](../README.md#rotta) | Error over time, order sensitivity, recovery and forgetting | Independent test batches hiding correlated streams or class imbalance |
| LLM preferences | [RLHF](../README.md#instructgpt), [DPO](../README.md#dpo), [Constitutional AI](../README.md#constitutional) | Preference agreement, held-out capability, robust refusal and benign helpfulness | Treating preference win rate as factual correctness or universal safety |
| Factual model editing | [ROME](../README.md#rome), [MEMIT](../README.md#memit), [MEND](../README.md#mend), [SERAC](../README.md#serac) | Edit efficacy, paraphrase generalization, locality, repeated-edit interference, fluency | Measuring only the exact edit prompt |
| Image/video editing | [ObjectDrop](../README.md#objectdrop), [VOID](../README.md#void), [ViT editing](../README.md#vitedit) | Intended change, unaffected content, temporal coherence, physical plausibility where relevant | Confusing visually attractive output with a correct counterfactual or preserved model behavior |

For ROME-style factual editing, consult the original paper's **CounterFact** setup and neighborhood/paraphrase tests. For MEMIT, use its original multi-edit evaluation. These datasets and protocols should travel with the method; a shared name such as “edit success” does not guarantee equivalent scoring.

## Failure detection and selective prediction

| Task | What is positive? | Useful metrics | Baselines and requirements |
| --- | --- | --- | --- |
| Misprediction detection | Incorrect prediction, if that convention is chosen | AUROC, AUPRC, risk–coverage curves, AURC; manuscript AUAC/AUFC when reproduced with its precise convention | [Softmax](../README.md#msp), entropy, margin, [GradTrust](../README.md#gradtrust); labels are needed to evaluate correctness |
| OOD detection | OOD sample, if that convention is chosen | AUROC, AUPRC, FPR at a stated TPR, separately for near/far shifts | [ODIN](../README.md#odin), [energy](../README.md#energy), [Mahalanobis](../README.md#mahalanobis), [GradNorm](../README.md#gradnorm), [GradPurview](../README.md#gradpurview) |
| Anomaly/novelty detection | Anomaly or unseen class according to the protocol | Detection metrics plus prevalence-sensitive precision/recall | [Gradient anomaly](../README.md#gradanomaly), [gradient novelty](../README.md#gradnovelty); specify normal reference data and class assumptions |
| Adversarial robustness | Correct prediction under a defined attack | Clean accuracy and robust accuracy at fixed threat model and budget | [AutoAttack](../README.md#autoattack), [RobustBench](../README.md#robustbench); evaluate adaptive attacks where appropriate |

**Record score direction.** Some methods produce confidence, others uncertainty. Specify the positive class and which side of the threshold is accepted. AUROC measures ranking; it does not establish that a score is a calibrated probability. AUPRC depends on prevalence. A detector can reject failures without improving the base model itself.

The manuscript's **AUAC/AUFC** uses its own percentile/performance construction. State exactly whether a point describes a percentile bin or a retained subset before reproducing a curve. Do not relabel it as standard risk–coverage evaluation without matching the definitions.

## Jailbreak and application evaluation

| Resource | What it contributes | Pair with |
| --- | --- | --- |
| [HarmBench](../README.md#harmbench) | Standardized harmful-behavior testing and robust-refusal evaluation | Benign helpfulness, attack budget and explicit response-judging rules |
| [JailbreakBench](../README.md#jailbreakbench) | Reproducible prompts, artifacts and evaluation conditions | Adaptive attacks, model versions and system-prompt documentation |
| [XSTest](../README.md#xstest) | Exaggerated safety behavior / over-refusal on benign prompts | Harmful-request evaluation rather than refusal rate alone |
| [Indirect prompt injection](../README.md#indirectinjection) | Threats arriving through retrieved or external application content | End-to-end tests of retrieval, tools and trust boundaries |
| [HELM](../README.md#helm) | Broad scenario and multi-metric evaluation | Domain-specific stress tests and operational monitoring |

Report attack success rate together with false-refusal rate, benign task performance, sampling parameters, query budget, judge version, and human spot checks. Treat guard models such as [Llama Guard](../README.md#llamaguard) as evaluated components. A classifier's label is not itself proof that the surrounding application is safe.

## Uncertainty and explanations

| Question | Resources | Evidence |
| --- | --- | --- |
| Are probabilities calibrated? | [Calibration](../README.md#calibration), [deep ensembles](../README.md#deepensembles) | NLL, Brier score, reliability diagrams and a specified calibration-error estimator; evaluate under shift |
| Are uncertainty estimates useful for decisions? | [MC dropout](../README.md#mcdropout), [DUQ](../README.md#duq), [TULIP](../README.md#tulip), [semantic entropy](../README.md#semanticentropy) | Error detection, selective risk, subgroup behavior, latency and additional-model cost |
| Do prediction sets cover the target? | [Conformal prediction](../README.md#conformal) | Empirical coverage and set size; check calibration/test assumptions and subgroup coverage |
| Is an explanation faithful and stable? | [Grad-CAM](../README.md#gradcam), [Integrated Gradients](../README.md#integratedgradients), [sanity checks](../README.md#sanitychecks), [VOICE](../README.md#voice) | Parameter/label randomization, justified perturbations, stability, explanation uncertainty and task-specific human assessment |

NLL and Brier score require observed targets for evaluation. The negative log-probability of a predicted class at runtime is a different object from labeled predictive NLL. Standard conformal guarantees rely on assumptions such as exchangeability; they do not automatically survive arbitrary temporal or domain shift. Mechanistic circuit discovery and saliency maps also answer different questions and need different faithfulness tests.

## Sequential and socio-technical evaluation

The following is an editorial evaluation template motivated by Chapter 8 and the linked resources, not a benchmark result reported by the manuscript.

| Lifecycle claim | Evidence to record |
| --- | --- |
| An update fixes an observed failure | Held-out examples of the same failure family and related but unseen conditions |
| An update preserves previous competence | Protected regression suite, prior-domain performance, safety/utility and calibration checks |
| A system learns over time | Sequence-level performance, forgetting, forward/backward transfer, recovery time and cumulative error |
| Users can act on uncertainty | Handoff quality, appropriate reliance, override outcomes, time to identify and resolve an error |
| Aggregate performance is representative | Relevant subgroup/domain metrics and uncertainty estimates, with justified grouping and sufficient samples |
| A model or data version is accountable | [Model cards](../README.md#modelcards), [datasheets](../README.md#datasheets), change records and responsible owner |
| Privacy risks are addressed empirically | Threat-specific membership/extraction evaluation and a separately validated removal process where needed |

The [AI RMF 1.0](../README.md#nistrmf) and [Generative AI Profile](../README.md#nistgenai) are versioned governance references, not blanket compliance certificates. Adoption, popularity, investment, and user trust are contextual evidence; none substitutes for measured reliability.

## Minimal experiment record

For each evaluation, record model/checkpoint version; data and split version; task and permitted perturbations; observability and adaptation rights; baseline and compute budget; metrics with direction and prevalence; random seeds; slice/shift results; and the concrete decision the evidence supports. For an update, retain the old result so regressions remain visible.
