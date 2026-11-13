# Pointer install and query/key-only training (2026-11-13)

Status: exploratory. One seed and one split per run. No independent read yet. Not entered in
`JOURNAL.md`, `GRAFT.md` or `SCOREBOARD.md`.

Code: `infra/aws_pg/jobs/bytegraft_ptr.py`. Metrics: `studies/bytegraft/results/ptr/*.json`
(copies of `s3://<s3-bucket>/results/bytegraft/ptr/<name>/out/metrics.json`).

## Question

The hosts fail word-edit tasks. Is the failure only that copy heads attend to the wrong source token,
and can the correct attention target be written into the host's own query and key weights with the
donor off?

## Setup

- Hosts: Pythia 1.4B, SmolLM2 1.7B, DeepSeek-Coder 1.3B. Own forward pass, checked against the
  Hugging Face forward (max logit gap 4e-5 on SmolLM2).
- Tasks: del_word, ins_word, sub_word, swap_word. 600 train and 200 test items per task, sentences
  disjoint. 800 test items in total.
- Score: number of test items whose text before the first `"` equals the gold after whitespace
  normalization. This is not the scoreboard's strict count; the two are not comparable.
- "Other" loss: cross-entropy on prompts of the bank's other tasks (2,400 items). "Neutral" loss:
  cross-entropy on Jeopardy question prompts. Neither is a standard corpus.
- Pointer: for each gold token, the source position it copies from, computed by a script from the
  gold alignment.

## Result 1: the attention target is the bottleneck

Right of 800. Overwriting the attention of 15 chosen heads with the script's pointer, weights
unchanged:

| | Pythia | SmolLM2 | DS-Coder |
|---|---|---|---|
| alone | 26 | 219 | 134 |
| 15 chosen heads pointed | 730 | 768 | 750 |
| 15 random heads pointed | 36 | 233 | 36 |

## Result 2: writing it into weights

Right of 800. Query/key deltas only, except the last row.

| | Pythia | SmolLM2 | DS-Coder |
|---|---|---|---|
| local fit, 15 heads, no gradient across layers | 451 | 536 | 519 |
| local fit, copy + helper heads | 577 | 564 | 533 |
| end-to-end, 15 copy heads | 542 | 553 | 608 |
| end-to-end, copy + helper heads (23 to 31) | 708 | 716 | 694 |
| end-to-end, query/key of all heads | 750 | 790 | 734 |
| end-to-end, value/output of all heads | 774 | 734 | 789 |

The local fit loses to end-to-end training of the same heads on all three hosts. It is not a win.
Pythia controls for the local fit: random heads 33, wrong pointer 0, no keep-KL term 166.
No method transferred to a held-out task (del_word held out: 5, 14, 3 of 200).

## Result 3: query/key-only against value/output-only

Loss on other prompts, base → query/key-only → value/output-only (all heads, 2,400 train items):

| | Pythia | SmolLM2 | DS-Coder |
|---|---|---|---|
| other | 1.783 → 2.693 → 4.340 | 1.533 → 1.525 → 1.696 | 1.370 → 1.695 → 2.754 |
| neutral | 2.594 → 3.314 → 5.604 | 2.112 → 2.115 → 2.211 | 2.615 → 2.924 → 3.553 |

Query/key-only raises loss on other text less than value/output-only on all three hosts. Only on
SmolLM2 is the change within noise of zero, and only there does query/key-only also score higher
(790 against 734).

Small data, SmolLM2 query/key-only: 128 items → 718 (other 1.528); 32 items → 483; 150 steps on
2,400 items → 747 in 113 s (other 1.532).

## Result 4: all 12 tasks, SmolLM2, no pointer

Artifact: `results/ptr/ptr_smollm2_all12b.json`. 600 train and 200 test items per task, 2,400 test
items. End-to-end on answer cross-entropy, all heads. Teacher-forced count, right of 2,400:

| | right | other loss | neutral loss |
|---|---|---|---|
| alone | 618 | 1.705 | 2.112 |
| query/key-only, 1,500 steps | 1,661 (decoded 1,709) | 1.926 | 2.149 |
| value/output-only, 1,500 steps | 1,653 | 1.923 | 2.216 |
| both, 1,500 steps | 1,643 | 2.186 | 2.274 |
| query/key-only, 4,000 steps | 1,668 (decoded 1,706) | 2.020 | 2.141 |

Per task, right of 200, alone → query/key-only → value/output-only (1,500 steps, teacher-forced):

| task | alone | query/key | value/output |
|---|---|---|---|
| spell | 172 | 178 | 153 |
| spell_inverse | 164 | 185 | 176 |
| contains_char | 0 | 161 | 164 |
| contains_word | 0 | 199 | 200 |
| ins_char | 13 | 26 | 31 |
| ins_word | 26 | 190 | 198 |
| del_char | 30 | 64 | 71 |
| del_word | 66 | 196 | 199 |
| sub_char | 20 | 49 | 53 |
| sub_word | 108 | 198 | 199 |
| swap_char | 0 | 17 | 11 |
| swap_word | 19 | 198 | 198 |

- Query/key-only and value/output-only tie at 12 tasks: 1,661 against 1,653 right, other loss 1.926
  against 1.923. The lower collateral cost of query/key-only seen on four tasks (Result 3) does not
  repeat here. Query/key-only is lower only on the neutral loss (2.149 against 2.216).
- Character edits stay low under every arm (11 to 81 of 200). More steps do not help (4,000 steps:
  1,668).
- The base count of 0 of 200 on both contains tasks is suspect: a Yes/No task should score near
  half. Base decode was not run. The gains on those two rows are not quotable until it is checked.
- The "other" set in this run has base loss 1.705, not the 1.533 of the four-task runs; it is a
  different item set and the two columns are not comparable across results.

## What is not shown

- No LoRA or full fine-tuning baseline, and no per-arm learning-rate tuning. Value/output-only is
  not a baseline anyone uses.
- No wikitext perplexity or standard benchmark for collateral change.
- One seed. One task family. Literature check was at snippet level only (nearest found:
  arXiv 2410.02247, not read in full). Novelty is not established.

## Deciding run, not yet done

Per host: query/key-only against LoRA (query and value) and full fine-tuning, three learning rates,
three seeds, scored on the task and on wikitext perplexity. About 3 to 4 GPU-hours per host.
Refuted if query/key-only does not match task score at lower perplexity cost on at least two of
three hosts.
