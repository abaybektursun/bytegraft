# BYTEGRAFT journal, the entries this page uses

Verbatim from the study's JOURNAL.md (private working repository), entry by entry, with the line range of each; private names replaced as listed in REDACTIONS.md. Entries refer to other study files (GRAFT.md, HANDOFF.md, NOTES_*.md, review files) that are not in this repository.

<!-- JOURNAL.md lines 1942 to 2082 -->
## 2026-11-11, `join_3`: under strict scoring the join holds on 480 of `join_2`'s items (token model 22.7% alone, 45.6% joined over the 12 tasks); a no-skill donor scaled per layer so that its change, summed over all carried rows, lands at F's size gives 19.0% (22.7%, O's level, when the text before the quote is compared; the last prompt row holds under 1% of the matched size, so its size there is not matched) [corrected 2026-11-11, AUDIT b §8.1]; with F's writes taken from another item the token model writes that other item's text (397 of 480 items by difflib ratio; 344 to 397 by three measures, 160 exact; O alone 42 by the same measure, 41 of them on the two Yes/No tasks) [corrected 2026-11-11, AUDIT b §8.2], so the joined text is F's content

- **Run:** `results/bytegraft/join/join_3` (STATUS `exit=0`; `out/metrics.json` `steps.{known_answers,items,results,summary}`,
  `out/decodes.jsonl` 3,840 rows: id, task, condition, generated, correct, correct_old), `bytegraft_join` at `87cbfadcd` (branch
  `research/bytegraft-tails`), instance `<instance>`, g6e.2xlarge, launched 04:03:11Z, results written 04:45:54Z. Reviewed
  before launch (`review_2026-11-11_join3.md` on the tails branch): one W finding, that the size match must be made on what lands
  after `post_attention_layernorm`, and C1 to C3; all fixed before launch (`NOTES_join.md`). Items (`steps.items`): 480, a seeded 40
  per task from `join_2`'s 600 published items; every other item was found inside the sample. Scoring (`results.scoring.rules`):
  every decode runs through the closing quote and is right only when its bytes equal the gold plus the quote; the old flag (the
  first len(gold) bytes) is stored beside it. Rows carried (`results.carried_share_mean`): 0.966 of O's rows for the F join, 0.859
  for the other-item join. Analysis of the stored rows: `results/join_3/other_follows.{py,json}`.
- **Conditions** (all 256 heads in every join): O alone; joined to F on the item's own run (`all`); joined to the no-skill donor S
  (`S`); `S_scaled`, the S join with S's correction scaled per item, layer and step so that the change that lands after
  `post_attention_layernorm` equals what F's correction lands in the same forward; `other`, F's writes from another item of the same
  task (never the same word or sentence and, for single words, not the same stem; 88 of the 200 word-task pairs share some word, 5
  share the operand word [corrected 2026-11-11, AUDIT b §8.3]; opposite gold on contains_char and contains_word; template rows map
  to themselves, the
  last line is aligned from its end); F alone; O + P0.
- **Known answers passed** (`known_answers.gates`, ten): `join_2`'s first seven (its two for the match connection do not apply);
  the old rule's flags and first len(gold) bytes reproduce `join_2`'s item by item (10); the scaled S join with k forced to 1 equals
  the plain S join exactly (11); the other-item join with the item as its own other equals the F join exactly (12). O's plain decode
  equals its step path on every item (`results.o_step_equals_plain`).
- **Whole items right, strict rule** (`results.accuracy.all.<condition>.<task>.mean`, equal to `results.scoring.strict.accuracy`;
  40 items per task):

| task | O alone | joined to F | joined to S (no skill) | S scaled to F's landed size | F's writes from another item | F alone | O + P0 |
|---|---|---|---|---|---|---|---|
| del_word | 0.03 | 0.57 | 0.03 | 0.03 | 0.00 | 0.60 | 0.42 |
| sub_word | 0.25 | 0.75 | 0.25 | 0.15 | 0.00 | 0.75 | 0.68 |
| ins_word | 0.12 | 0.70 | 0.12 | 0.12 | 0.00 | 0.78 | 0.28 |
| swap_word | 0.00 | 0.38 | 0.00 | 0.03 | 0.00 | 0.40 | 0.20 |
| contains_word | 0.47 | 0.75 | 0.53 | 0.65 | 0.17 | 0.97 | 0.72 |
| contains_char | 0.50 | 0.85 | 0.47 | 0.50 | 0.20 | 0.50 | 0.53 |
| spell | 0.62 | 0.50 | 0.57 | 0.57 | 0.00 | 0.78 | 0.15 |
| spell_inverse | 0.57 | 0.55 | 0.33 | 0.12 | 0.00 | 0.78 | 0.55 |
| del_char | 0.00 | 0.12 | 0.00 | 0.03 | 0.00 | 0.10 | 0.00 |
| ins_char | 0.15 | 0.10 | 0.05 | 0.07 | 0.00 | 0.25 | 0.00 |
| sub_char | 0.00 | 0.17 | 0.00 | 0.00 | 0.00 | 0.23 | 0.03 |
| swap_char | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| **mean, 12 tasks** | 0.227 (0.194 to 0.258) | 0.456 (0.419 to 0.494) | 0.196 (0.165 to 0.227) | 0.190 (0.160 to 0.219) | 0.031 (0.017 to 0.046) | 0.510 (0.473 to 0.548) | 0.296 (0.263 to 0.327) |
| **mean, five word tasks** | 0.175 (0.130 to 0.225) | 0.630 (0.565 to 0.690) | 0.185 (0.140 to 0.235) | 0.195 (0.150 to 0.240) | 0.035 (0.015 to 0.060) | 0.700 (0.640 to 0.760) | 0.460 (0.400 to 0.520) |

  Entries are counts out of 40 at two decimals as Python prints them (0.575 prints 0.57, 0.225 prints 0.23); the exact value is at
  the key. `O_plain` (plain `token_decode`) equals `O` on every task. By the old rule (`summary.means_old_rule`), 12 tasks then word
  tasks: O 0.246, 0.175; joined 0.479, 0.630; S 0.219, 0.185; S_scaled 0.206, 0.195; other 0.031, 0.035; F 0.531, 0.700; O + P0
  0.329, 0.470. `other_follows.json` recomputes every strict mean from the stored rows: equal to `metrics.json`.

  Paired differences, strict rule (`results.scoring.strict.controls.differences.{all,word}.<difference>.mean`; the first two also in
  `results.differences`):

| difference | 12 tasks | five word tasks |
|---|---|---|
| joined − O alone | +0.229 (0.190 to 0.269) | +0.455 (0.380 to 0.525) |
| joined − S | +0.260 (0.219 to 0.304) | +0.445 (0.365 to 0.515) |
| joined − S_scaled | +0.267 (0.227 to 0.306) | +0.435 (0.365 to 0.505) |
| joined − other | +0.425 (0.385 to 0.465) | +0.595 (0.525 to 0.660) |
| S_scaled − O alone | −0.0375 (−0.0625 to −0.0125) | +0.020 (−0.025 to +0.065) |
| other − O alone | −0.196 (−0.229 to −0.163) | −0.140 (−0.195 to −0.090) |

  Items fixed and broken against O alone (`results.paired.O`): joined 127 and 17; S 5 and 20; S_scaled 16 and 34; other 4 and 98.
  Against O + P0 (`results.paired.O+P0`): joined 113 and 36. Items whose tokens differ from O alone (`summary.tokens_differ_from_O`):
  F join 344, S 145, S_scaled 271, other 431.
- **The size match** (`results.scoring.landed.S_scaled`): 39,840 layer-steps, F lands something on every one; the achieved ratio
  (S_scaled's landed size over F's in the same forward) lies inside [0.8, 1.25] on 1.0 of them, saturated 0.0, 1.0000 to 1.0005 from
  the 5th to the 95th percentile. Median k per layer (`k_by_layer.median`): 7.28 at layer 0, 1.56 to 2.45 at layers 1 to 15.
  Against the F join's own run at the first step, where every join reads the same text (`landed.first_step_landed_over_F`, median
  and 5th to 95th percentile over items and layers): plain S 0.17 (0.02 to 0.33), S_scaled 1.26 (0.91 to 1.50), other 0.97 (0.93
  to 1.04).
- **Printed readings (frozen, strict rule;** `summary.strict_readings`**):** for both means "the gain is the donor's skill on this
  item". Share of the gain given by S_scaled: 0.04 (word tasks) and −0.16 (12 tasks); by other: −0.31 and −0.85. "A matched push
  without skill gives part of it" and "another item's writes give part of it" did not print (neither interval lies above 0); "the
  scaled no-skill donor could not be matched" did not print (`landed.S_scaled.matched` true). The old rule prints the same sentence
  (`results.scoring.old.controls.readings`). `join_1`'s per-task rule (`results.readings.all`, strict) prints "the joined token model
  does the task" for the five word tasks, contains_char, del_char, sub_char and both means, and "no" for spell, spell_inverse,
  ins_char and swap_char; by the old rule del_char reads "no".
- **Which item the text follows** (`results/join_3/other_follows.json` `follow_total`, `follow_by_task`; the text before the first
  quote compared with each gold by `difflib` ratio). Under the other-item join the text is closer to the other item's gold than to
  the item's own on 397 of 480 items (own 74, tie 9) and equals the other item's gold on 160. Per task, closer to the other item:
  contains_word 33, del_word 40, ins_word 40, sub_word 39, swap_word 40, contains_char 32, spell 38, spell_inverse 39, del_char 33,
  ins_char 20, sub_char 24, swap_char 19 of 40. The F join follows its own item on 461 of 480, S_scaled on 439. On the Yes/No tasks
  (`decodes.jsonl`): on contains_char O, F and S_scaled answer "No" on all 40; the other-item join answers "Yes" on 12 of the 20
  items whose other item's gold is "Yes" and on 0 of the 20 whose other item's gold is "No". On contains_word it answers "Yes" on 20
  of 20 and 7 of 20.
- **Samples** (`decodes.jsonl`, which stores no probabilities). `published:del_word:009539`, last prompt line `Delete every instance
  of " they " in " And they lived happily ever after. ". Answer: "`, gold ` And lived happily ever after.` then ` "`: O alone wrote
  ` And they lived happily ever after` (wrong); joined ` And lived happily ever after. "` (right); S_scaled ` And they lived ever
  after. "` (wrong: it deleted "happily"); with F's writes from `del_word:009954` (delete " Tim " in " Tim and Kim are scared. ") it
  wrote ` Kim and are scared. "` (wrong: the other item's sentence). `published:contains_char:002972`, `Is there a " c " in "
  administration "? Answer: "`, gold `No`: O, the join and S_scaled wrote `No"` (right); with F's writes from
  `contains_char:002391` (" a " in " sales ", gold Yes) it wrote `Yes` (wrong: the other item's answer).
- **Readings (the coordinator's; one run, 40 items per task, items already decoded in `join_2`):**
  1. Under strict scoring the join holds: +0.229 over O alone on the 12 tasks and +0.455 on the word tasks. Strict scoring lowers O
     and the join by about two points each (0.246 to 0.227; 0.479 to 0.456).
  2. The audit's finding on the unmatched control is answered for the total size of the change. A no-skill donor scaled per layer
     to F's landed size, summed over all carried rows, does not give the gain: 0.190 against O's 0.227 by the strict rule (16 fixed,
     34 broken), and 0.227 against 0.227 when the text before the quote is compared. In F's own run it lands a median 1.26 of F's
     size, so in total it was not too small; at the deciding rows its size was not matched. Its spell_inverse 0.125 is a loss of
     format: on 17 items it writes the right word without the leading space (0.550 by text) [corrected 2026-11-11, AUDIT b §8.4].
     Per task it also reads 0.650 against 0.475 on contains_word (S_scaled − O +0.175, −0.025 to +0.375), where it answers "Yes" on
     30 of 40 items, as the F join does.
  3. The other-item control shows more than it was built for. With F's writes from another item, the host's text follows that other
     item on 397 of 480 items (by difflib ratio; 344 to 397 by three measures; O alone 42 by the same measure, 41 of them on the two
     Yes/No tasks) and is the other item's gold exactly on 160 [corrected 2026-11-11, AUDIT b §8.2]. On the two Yes/No tasks it gives
     the other item's answer on 32 and 33 of 40, against 20 and 21 for O alone; on contains_char it answers "Yes" on 12 of the 20
     items whose other item's gold is "Yes" and on none of the other 20 [corrected 2026-11-11, AUDIT b §8.2]. So once F's attention
     writes replace the host's at the matched rows, the joined text is the donor's content; the host does not answer from its own reading of its prompt. In this join the host supplies its token interface, MLPs,
     norm and unembedding; which word, which edit and which answer come from the donor. This fits `tails_2` (carrying F's attention
     outputs gives 0.81 of F's advantage). It also means this join, as built, is not yet the mission's object, a host that computes
     with what it is given: it is F's attention stream decoded by O.
  4. contains_char: joined 0.850 on 40 items against O 0.500, F 0.500 and S_scaled 0.500 (right on 15 of 20 "Yes" items and 19 of
     20 "No" items); the other-item join 0.200, because it gives the other item's opposite answer on 32 of 40. F's writes for an
     item carry that item's Yes/No answer, although F's own output is "No" on all 40 items. On the 19 words of 1 to 3 letters the
     join is right on 18 (O 9). On words of 4 or more letters it is uncertain. The join is ahead of O on 20 rare dev words (16 against
     8, loose rule) and on these 21 (16 against 11), and not on `pair_1`'s 20 fresh words (10 against 11; `results/pair_1/readouts.json`).
     `join_3`'s and `pair_1`'s rates do not differ beyond chance (Fisher p = 0.11) [corrected 2026-11-11, pair_1]
     [corrected 2026-11-11, AUDIT b §8.5]. These 40 items are a subsample of
     `join_2`'s 50, so this is `join_2`'s reading under strict scoring with two new controls, not a fresh replication.
  5. No model here does character edits under strict scoring: F reads 0.100, 0.250, 0.225, 0.000 on del_char, ins_char, sub_char,
     swap_char; the join 0.125, 0.100, 0.175, 0.025.
  6. What follows: `GRAFT.md` first steps, 16 (`join_4`): F's writes carried only at the context rows or only at the deciding rows,
     and at the deciding rows only at layers 12 to 15 or only at layers 0 to 11, on these 480 items with strict scoring.
- **Limits:** one run; 40 items per task, all already decoded in `join_2`. The other-item alignment maps the template rows to
  themselves and aligns the last line from its end; it carries 0.859 of O's rows against the F join's 0.966. The size match is made
  inside the scaled join's own forward, and on the norm summed over all carried rows per layer, not per row; against the F join's
  own run the scaled join lands a median 1.26 of F's size at the first step [corrected 2026-11-11, AUDIT b §8.1]. "Follows"
  compares the text before the first quote with the two golds by `difflib` ratio.
- **Added 2026-11-11, after this entry was written: two counts from the stored rows** (`out/decodes.jsonl` fields `condition`,
  `correct`, `generated`; strict flags; a text is `generated` before its first double quote, stripped).
  - (a) Items that both O alone and F alone get wrong: 230 of 480 (swap_char 40, del_char 36, sub_char 31, ins_char 30, swap_word 24,
    contains_char 20, del_word 16, sub_word 9, spell 8, spell_inverse 8, ins_word 7, contains_word 1). Right on them: the F join 34,
    the plain S join 1, S_scaled 3, the other-item join 0, O + P0 35. O + P0's 35 include all 20 contains_char items whose gold is
    "Yes"; O + P0 answers "Yes" on 39 of the 40 contains_char items. The F join's 34 include 15 contains_char "Yes" items (it answers
    "Yes" on 16 of 40); its other 19 are spread over eight tasks (swap_word 5, del_char 3, del_word 3, sub_char 3, sub_word 2, ins_word
    1, spell 1, swap_char 1). 9 of the 15 contains_char items are words of 1 to 3 letters; on 20 fresh words of 4 or more letters
    the join reads 10 of 20 (`pair_1`; `results/pair_1/readouts.json`) [corrected 2026-11-11, pair_1]. The rule selects nothing: every item, both strict flags. This is the item-level count that research
    pass 7 (`research_pass_2026-11-11a.md` §8, item 4) says a reviewer will ask for.
  - (b) The F join's text against F's own text. Where F is right (245 items) the join writes the same text on 182, and it is right on
    exactly those 182. Where F is wrong (235 items) the join writes F's same wrong text on 51 (21 of these are also O's text), O's
    text and not F's on 24, and neither on 160; it is right on 37 of the 235. So the join tracks F's right answers and is not a copy
    of F's errors.

<!-- JOURNAL.md lines 2083 to 2213 -->
## 2026-11-11, `join_4`: F's attention writes carried only at the deciding rows (the last prompt row and every generated row, 3% of the carried rows) give 0.93 of the join's gain over the 12 tasks and 0.99 on the word tasks; only at the context rows, 0.15; at the deciding rows the last four layers alone give 0.66 and 0.71

- **Run:** `results/bytegraft/join/join_4` (STATUS `exit=0`, written 05:50:32Z; `out/metrics.json`
  `steps.{models,items,known_answers,plan,progress,reproduction,results,summary}`, `out/decodes.jsonl` 3,840 rows), `bytegraft_join`
  at `425fde913` (branch `research/bytegraft-tails`; `out/args.json` `PG_GIT_SHA` `425fde9133eb`), instance `<instance>`,
  g6e.2xlarge, launched 05:19:54Z (EC2, read-only), first heartbeat 05:20:24Z. Reviewed before launch with no W finding
  (`review_2026-11-11_join4.md`, in the coordinator's session folder, not in the repository); its C1 and C2 are answered by the rule fixed in `GRAFT.md` first steps, 16, and by
  `results/join_4/subset_shares.{py,json}`. Items (`steps.items`): `join_3`'s 480, 40 per task, read from `join_3`'s `decodes.jsonl`
  and asserted equal to its `steps.items.ids`. Strict scoring (`results.scoring.rules.strict`), the old flag stored beside it. F is
  not decoded in this job: its rows are `join_3`'s (text and flag equal on all 480). No O + P0. Main decodes 1,336.9 s
  (`progress.seconds`), 0.142 s per joined step (`known_answers.seconds_per_joined_step`), GPU peak 18.6 GB (`progress.memory`).
- **Conditions.** A row is carried, as in every join, only where it matches both F's and S's parses; a row set restricts which of
  those rows take F's attention outputs, and the rest keep O's own. O alone (`O_plain`, `O`); `all` (every carried row, all 16
  layers); `context` (carried rows before the last prompt row); `deciding` (the last prompt row and every generated row);
  `deciding_late` (deciding rows, the heads of layers 12 to 15); `deciding_early` (deciding rows, layers 0 to 11); F alone.
- **Known answers passed** (`known_answers.gates`, nine): `join_1`'s 1 to 6 on these items (O's step path and the published rows
  reproduce O; O's own heads as the donor give O's tokens; the joined log-odds at `heads_1`'s position equal `heads_1`'s; O + P0's
  state root equals `pointer_1`'s; the empty head set gives O's tokens and all heads in F's order give the all-heads tokens; the kept,
  extended parses give the from-scratch tokens and `_decide`'s masks); 10, the earlier run's records reproduce (O alone and `all`
  give `join_3`'s strict text and both flags, item by item; `reproduction.differ` empty); 13, `deciding_late` and `deciding_early`
  applied together equal `deciding` exactly (24 items; `13_late_plus_early_differ` empty); 14, the empty row set gives O's tokens
  (`14_rows_empty_differ` empty). O's plain decode equals its step path on every item (`results.o_step_equals_plain`).
- **Whole items right, strict rule** (`results.accuracy.all.<condition>.<task>.mean`; 40 items per task, exact values; F from
  `join_3`'s rows):

| task | O alone | `all` | `context` | `deciding` | `deciding_late` | `deciding_early` | F alone |
|---|---|---|---|---|---|---|---|
| del_word | 0.025 | 0.575 | 0.125 | 0.575 | 0.425 | 0.200 | 0.600 |
| sub_word | 0.250 | 0.750 | 0.350 | 0.725 | 0.600 | 0.375 | 0.750 |
| ins_word | 0.125 | 0.700 | 0.150 | 0.700 | 0.550 | 0.375 | 0.775 |
| swap_word | 0.000 | 0.375 | 0.050 | 0.375 | 0.300 | 0.050 | 0.400 |
| contains_word | 0.475 | 0.750 | 0.550 | 0.750 | 0.625 | 0.800 | 0.975 |
| contains_char | 0.500 | 0.850 | 0.625 | 0.850 | 0.800 | 0.550 | 0.500 |
| spell | 0.625 | 0.500 | 0.600 | 0.500 | 0.475 | 0.550 | 0.775 |
| spell_inverse | 0.575 | 0.550 | 0.550 | 0.525 | 0.550 | 0.600 | 0.775 |
| del_char | 0.000 | 0.125 | 0.000 | 0.100 | 0.075 | 0.000 | 0.100 |
| ins_char | 0.150 | 0.100 | 0.100 | 0.100 | 0.100 | 0.150 | 0.250 |
| sub_char | 0.000 | 0.175 | 0.025 | 0.050 | 0.025 | 0.000 | 0.225 |
| swap_char | 0.000 | 0.025 | 0.000 | 0.025 | 0.025 | 0.000 | 0.000 |
| **mean, 12 tasks** | 0.227 (0.194 to 0.258) | 0.456 (0.419 to 0.494) | 0.260 (0.229 to 0.290) | 0.440 (0.404 to 0.477) | 0.379 (0.344 to 0.419) | 0.304 (0.271 to 0.337) | 0.510 (0.473 to 0.548) |
| **mean, five word tasks** | 0.175 (0.130 to 0.225) | 0.630 (0.565 to 0.690) | 0.245 (0.195 to 0.295) | 0.625 (0.560 to 0.685) | 0.500 (0.435 to 0.570) | 0.360 (0.310 to 0.415) | 0.700 (0.640 to 0.760) |

  `O_plain` equals `O` on every task. By the old rule (`summary.means_old_rule`), 12 tasks: O 0.246, `all` 0.479, `context` 0.2875,
  `deciding` 0.469, `deciding_late` 0.406, `deciding_early` 0.321, F 0.531; the word-task means equal the strict ones.
  `subset_shares.py` recomputes every strict mean from the stored rows and asserts it equal to `metrics.json`.

  Shares of the gain, share(x) = (x − O) / (`all` − O), strict rule. Point values from the means; they are equal in
  `summary.strict_readings.<group>.shares` and in `results/join_4/subset_shares.json` `all_items.<group>.shares`. The intervals come
  from two separate bootstraps (2,000 draws within task) and differ in the second decimal; both are given.

| condition | 12 tasks | interval, `strict_readings` | interval, `subset_shares.json` | word tasks | interval, `strict_readings` | interval, `subset_shares.json` |
|---|---|---|---|---|---|---|
| `context` | 0.15 | −0.02 to 0.28 | −0.01 to 0.28 | 0.15 | 0.01 to 0.27 | 0.01 to 0.28 |
| `deciding` | 0.93 | 0.88 to 0.97 | 0.88 to 0.97 | 0.99 | 0.97 to 1.00 | 0.96 to 1.00 |
| `deciding_late` | 0.66 | 0.54 to 0.78 | 0.54 to 0.77 | 0.71 | 0.60 to 0.82 | 0.60 to 0.81 |
| `deciding_early` | 0.34 | 0.23 to 0.45 | 0.22 to 0.46 | 0.41 | 0.30 to 0.51 | 0.29 to 0.52 |

  The gain itself (`strict_readings.<group>.gain`): +0.229 (0.190 to 0.269) over the 12 tasks, +0.455 (0.380 to 0.525) on the word
  tasks. Share of `context` plus share of `deciding` (`localize.<group>.share_sum_context_deciding`): 1.07 and 1.14.

  Paired differences, strict rule (`results.scoring.strict.localize.<group>.differences.<condition>.{minus_O,minus_all}.mean`):

| difference | 12 tasks | five word tasks |
|---|---|---|
| `context` − O alone | +0.033 (−0.004 to +0.069) | +0.070 (+0.005 to +0.130) |
| `deciding` − O alone | +0.212 (+0.173 to +0.250) | +0.450 (+0.375 to +0.520) |
| `deciding_late` − O alone | +0.152 (+0.113 to +0.194) | +0.325 (+0.245 to +0.400) |
| `deciding_early` − O alone | +0.077 (+0.048 to +0.106) | +0.185 (+0.125 to +0.245) |
| `context` − `all` | −0.196 (−0.235 to −0.158) | −0.385 (−0.455 to −0.315) |
| `deciding` − `all` | −0.017 (−0.027 to −0.006) | −0.005 (−0.015 to 0.000) |
| `deciding_late` − `all` | −0.077 (−0.106 to −0.050) | −0.130 (−0.185 to −0.075) |
| `deciding_early` − `all` | −0.152 (−0.188 to −0.117) | −0.270 (−0.330 to −0.210) |

  Items fixed and broken against O alone (`results.paired.O`): `all` 127 and 17; `context` 48 and 32; `deciding` 119 and 17;
  `deciding_late` 97 and 24; `deciding_early` 51 and 14. Items whose tokens differ from O alone (`summary.tokens_differ_from_O`):
  `all` 344, `context` 313, `deciding` 325, `deciding_late` 305, `deciding_early` 249. Items whose text equals `all`'s
  (`results.scoring.equals_all`, equal to `subset_shares.json` `text_equals_all`): `deciding` 386, `deciding_late` 294,
  `deciding_early` 200, `context` 174 of 480.
- **The two checks fixed before the launch** (`GRAFT.md` first steps, 16; `results/join_4/subset_shares.json`). (1) At the first
  step, where every condition reads the same prompt, the carried-row share of `context` plus that of `deciding` equals `all`'s on
  every item (`first_step_partition_worst_gap` 1.0e-16), so the readings are made. (2) The last prompt row is carried at the first
  step on all 480 items (`items_last_prompt_row_carried_at_first_step`; 40 in every task, `by_task_last_row_carried`), so the reading
  on the items whose last prompt row is carried is the reading on all items, and the case of review finding C1 does not arise. Mean
  share of rows carried over all steps (`results.carried_share_mean`): `all` 0.966, `context` 0.937, `deciding` 0.032,
  `deciding_late` 0.031, `deciding_early` 0.031. After the first step the newest row is carried less often on the character tasks:
  under `all` on 0.39 to 0.45 of steps for del_char, ins_char, sub_char and swap_char, 0.80 for spell_inverse, 0.96 to 1.00 for the
  other seven tasks (`summary.accuracy_and_newest_token_carried_by_task`, second number; over all tasks
  `results.last_row_carried_share` 0.853).
- **Printed readings (frozen, strict rule;** `summary.strict_readings`**):** for both means "the deciding rows suffice: the donor's
  writes at the rows that write the answer carry it"; for the 12 tasks "the deciding rows need both layer ranges"; for the word
  tasks "the last four layers suffice". The rule reads the shares on all items and on the items whose last prompt row is carried at
  the first step; these are the same 480 items, so the two readings agree. `summary.readings` and `results.readings` are null in
  this run.
- **contains_char** (`decodes.jsonl`; the gold is "Yes" on 20 items, the 20 on which O alone, which answers "No" on all 40, is
  wrong). `deciding` 0.850: "Yes" on 16 of 40, right on 15 of the 20 "Yes" items and 19 of the 20 "No" items; `all` the same counts.
  `deciding_late` 0.800: "Yes" on 18; 15 and 17. `context` 0.625: "Yes" on 23; 14 and 11. `deciding_early` 0.550: "Yes" on 2; 2 and
  20. O and F (`join_3`'s rows) answer "No" on all 40.
- **Samples** (`decodes.jsonl`, which stores no probabilities; prompts from `bank/smoke_7/season_1/published.jsonl`).
  `published:del_word:009539`, last prompt line `Delete every instance of " they " in " And they lived happily ever after. ". Answer:
  "`, gold ` And lived happily ever after.`: `all`, `deciding` and `deciding_late` wrote ` And lived happily ever after. "` (right);
  O alone, `context` and `deciding_early` wrote ` And they lived happily ever after` (wrong: the sentence copied).
  `published:contains_char:002391`, `Is there a " a " in " sales "? Answer: "`, gold `Yes`: `all`, `context`, `deciding` and
  `deciding_late` wrote `Yes"` (right); O alone, F alone and `deciding_early` wrote `No"` (wrong).
  `published:contains_char:002972` (" c " in " administration ", gold `No`): every condition wrote `No"` except `context`, which
  wrote `Yes` (wrong).
- **Readings (the coordinator's; one run, 40 items per task, the items of `join_2` and `join_3`):**
  1. The fork of step 16 is decided. The context rows alone give 0.15 of the gain; the deciding rows alone give 0.93 (12 tasks) and
     0.99 (word tasks). The host does not compute the answer from the donor's writes on the prompt. F's attention outputs at about
     3% of the carried rows, the rows that write the answer, carry the join.
  2. The frozen 2/3 line does not settle the layer question. The last four layers alone give 0.66 on the 12 tasks (just under the
     line: "need both layer ranges") and 0.71 on the word tasks (over it: "the last four layers suffice"); both intervals cross the
     line. Layers 0 to 11 alone give 0.34 and 0.41. About two thirds of the gain can be carried by the last four layers alone.
  3. contains_char: 0.850 with the deciding rows alone, 0.800 with their last four layers alone, 0.550 with layers 0 to 11 (which
     answer "Yes" on 2 of 40, close to the constant "No" rate), 0.625 with the context rows; O and F 0.500 each. For the first answer
     token the deciding rows are the last prompt row alone, so F's late attention writes at that row carry the item's answer,
     although F's own output is "No" on all 40 items. These are `join_3`'s 40 items, 19 of them words of 1 to 3 letters (`all` right
     on 18, O on 9). On words of 4 or more letters it is uncertain. The all-heads join is ahead of O on 20 rare dev words (16 against
     8, loose rule) and on `join_3`'s 21 (16 against 11), and not on `pair_1`'s 20 fresh words (10 against 11;
     `results/pair_1/readouts.json`). `join_3`'s and `pair_1`'s rates do not differ beyond chance (Fisher p = 0.11)
     [corrected 2026-11-11, pair_1] [corrected 2026-11-11, AUDIT b §8.5].
  4. With `join_3`'s other-item control this gives one picture: the join is F's attention stream at the answer rows, mostly its late
     layers, turned into tokens by O. Step 16's rule sends the wholesale join at 1B no further when the deciding rows suffice and the
     last four layers suffice; that printed for the word tasks, while the 12-task mean printed "need both layer ranges", the branch
     whose next question is what O's MLPs add. The coordinator does not build on the wholesale join at 1B: the next run must be one
     in which the host has something to contribute.
  5. What follows: `GRAFT.md` first steps, 17 (`pair_1`).
- **Limits:** one run; 40 items per task, the same items as `join_2` and `join_3`; the layer split was read at one boundary (layer
  12), chosen before the run. F's column is `join_3`'s rows, not a new decode. After the first step the newest row is carried on
  0.39 to 0.45 of steps on the four character tasks, so there the deciding rows carry less than on the word tasks. The share
  intervals in `metrics.json` and in `subset_shares.json` come from separate bootstraps.

<!-- JOURNAL.md lines 2214 to 2390 -->
## 2026-11-11, `pair_1`: on 400 Jeopardy questions in free generation the token model leads the byte model (0.4575 against 0.3825); the all-heads join is not above both parents (two-set mean 0.389 against F's 0.460) and sits between them on the questions, where its answer is mostly the host's; on 20 fresh contains_char items, all words of 4 or more letters, the join reads 0.50, which corrects `join_2` to `join_4`

- **Items job:** `results/bytegraft/bank/jeopardy_1` (STATUS `exit=0`; `out/metrics.json` `steps.items_only`,
  `out/items_report.json`), `bytegraft_join --items-only` at `145efcd7b` (`out/args.json` `PG_GIT_SHA` `145efcd7b5ac`), CPU instance
  `<instance>`, m7i.large, launched 06:31:43Z (EC2, read-only), first heartbeat 06:32:18Z, STATUS 06:36:55Z. Source
  `soldni/jeopardy` at revision `aebec90f5249`, config `mosaicml_gauntlet` (`source`): 2,116 rows (`rows`); 82 dropped for a double
  quote in the answer and 1 for an answer over 40 bytes (`dropped`); 2,033 usable; 400 items in seeded order, the shots drawn from
  the other 1,633 rows (`shot_pool`); five categories (science 100, literature 83, American history 78, word origins 70, world
  history 69; the items' `stratum`). Gold median 9 bytes and 3 of O's tokens (`gold_bytes`, `gold_tokens_O`). Two prompt variants
  with identical items and order, `jeopardy_items_5shot.jsonl` and `jeopardy_items_3shot.jsonl` (the 3-shot prompt is the first
  three shots of the 5-shot one); O's rows per prompt, median 207 with 5 shots and 137 with 3 (`variants.<v>.prompt_rows_O`). The
  coordinator read both files in full offline, and this entry's author recounted from the files: no prompt repeats a shot's answer
  and no shot shares the item's normalized answer; the gold stands inside its own question on 2 items (`jeopardy:02027` "500",
  `jeopardy:01712` "iron"); 22 prompts hold non-ASCII characters; 388 distinct normalized golds.
- **Main run:** `results/bytegraft/pair/pair_1` (STATUS `exit=0`; `out/metrics.json`
  `steps.{models,items,known_answers,plan,progress,results,summary}`, `out/decodes.jsonl` 3,200 rows; question rows carry `answer`,
  `strict`, `normalized`, `closed`), `bytegraft_join` at `9737895c4` (branch `research/bytegraft-tails`; `out/args.json`
  `PG_GIT_SHA` `9737895c490e`), instance `<instance>`, g6e.2xlarge, launched 06:52:55Z (EC2, read-only), first heartbeat
  06:53:40Z, STATUS 07:23:32Z. Reviewed before launch (`review_2026-11-11_pair1.md` on the tails branch): W1 (both G2 sentences can
  hold by their rules and the code printed one) and W2 (an answer with no closing quote could be scored right) fixed before launch,
  with C1 (the time stop now scales a question step by the prompt's rows); C2 open (the closed-row share is recorded, not gated;
  known answers 15 and 16 have no registered failing input). Items (`steps.items`): 240 fresh CUTE items, 20 per task in
  `published_sample`'s seeded order under the dev rule, none of `join_2`'s 600 (`earlier_items`); the 400 questions of the 5-shot
  file. Main decodes 1,293.2 s (`progress.seconds`); 0.172 s per joined step on the known-answer items
  (`known_answers.seconds_per_joined_step`); the plan's estimate 32.1 minutes (`plan.minutes_at_measured_joined_step`, question step
  scale 2.80); GPU peak 17.95 GB (`progress.memory`).
- **Conditions** on both sets: O alone (`O_plain`, `O`); F alone; `all`, O joined to F with all 256 heads at the rows that match both
  F's and S's parses; `S`, O joined to the no-skill donor S in the same way. Carried rows on the CUTE side
  (`results.carried_share_mean`): 0.934 for both joins.
- **Scoring.** CUTE: strict, as `join_3`. Questions (`results.pair.scoring.questions`): every condition decodes to its first closing
  double quote or 48 bytes; the headline is normalized exact match (SQuAD's rule: lower case; punctuation, the articles a, an, the and
  extra spaces removed, on both sides) of the text before the quote; strict exact match beside it; an answer with no closing quote is
  wrong under both. The published Jeopardy numbers, 76.4 against 69.6 (Bolmo v2 Table 2; `results.pair.published_rank_choice`), are
  rank choice by likelihood on `allenai/jeopardy-gen2mc`, a different measure; they are not compared with these.
- **Known answers passed** (`known_answers.gates`, nine): 1, the step path and the published rows reproduce O; 2, O's own heads as
  the donor give O's tokens; 3, the joined log-odds at `heads_1`'s position equal `heads_1`'s (48 items, largest gap 0.0,
  `3_summary`); 4, O + P0's state root equals `pointer_1`'s; 5, the empty set gives O's tokens and all heads in F's order give the
  all-heads tokens; 6, the kept, extended parses give the from-scratch tokens and `_decide`'s masks; 7, F's decodes equal its stored
  published rows (24 items, `7_f_stored`); 15, on the questions O's own heads as the donor give O's tokens (24 items); 16, on the
  questions the empty head set gives O's tokens (24 items). O's plain decode equals its step path on CUTE
  (`results.o_step_equals_plain`) and gives the same normalized answer on all 400 questions (`results/pair_1/readouts.json`).
- **Questions** (`results.pair.questions`, normalized exact match; strict from `results.pair.questions_strict`; 400 items):

| | O alone | F alone | joined to F | joined to S (no skill) |
|---|---|---|---|---|
| normalized exact match | 0.4575 (0.4075 to 0.505) | 0.3825 (0.335 to 0.428) | 0.4275 (0.3775 to 0.4775) | 0.400 (0.350 to 0.4475) |
| strict exact match | 0.315 (0.27 to 0.36) | 0.255 (0.2125 to 0.2975) | 0.2825 (0.24 to 0.3275) | 0.2675 (0.225 to 0.3125) |
| fixed / broken against O alone, normalized (strict) | | 28 / 58 (27 / 51) | 26 / 38 (20 / 33) | 17 / 40 (13 / 32) |

| difference (`differences.<name>.mean`) | normalized | strict |
|---|---|---|
| O − F | +0.075 (0.0325 to 0.12) | +0.060 (0.015 to 0.1025) |
| joined − F | +0.045 (−0.0025 to 0.09) | +0.0275 (−0.015 to 0.0675) |
| joined − O | −0.030 (−0.07 to 0.01) | −0.0325 (−0.07 to 0.0) |
| S − O | −0.0575 (−0.0925 to −0.0225) | −0.0475 (−0.08 to −0.0175) |
| S − F | +0.0175 (−0.03 to 0.063) | +0.0125 (−0.033 to 0.0575) |

  Closed answers (`results.pair.closed_share`): 1.0 in every condition but F, 0.9975 (one F decode reached 48 bytes with no quote);
  the closing-quote rule changed 0 flags in every condition (`unclosed_flag_changed`). The last prompt row is closed in both parses
  on every question prompt and every CUTE prompt (`last_prompt_row_closed` 1.0 and 1.0), so the join writes at the first answer
  token on every item. Items whose tokens differ from O alone (`tokens_differ_from_O.questions`): F join 397, S join 158; this
  count includes the closing token, since the F join closes with the token `"\n\n` on 399 items where O closes with `"` on 396; of
  the 207 items whose answer text equals O's exactly, 204 differ in tokens (`readouts.json` `text_after_first_quote`,
  `of_these_tokens_differ`).
- **CUTE, strict, fresh items** (`results.accuracy.all.<condition>.<task>.mean`; 20 items per task):

| task | O alone | joined to F | joined to S (no skill) | F alone |
|---|---|---|---|---|
| del_word | 0.05 | 0.60 | 0.05 | 0.75 |
| sub_word | 0.20 | 0.60 | 0.15 | 0.90 |
| ins_word | 0.10 | 0.60 | 0.10 | 0.75 |
| swap_word | 0.00 | 0.40 | 0.00 | 0.55 |
| contains_word | 0.55 | 0.60 | 0.60 | 1.00 |
| contains_char | 0.55 | 0.50 | 0.60 | 0.50 |
| spell | 0.35 | 0.35 | 0.35 | 0.70 |
| spell_inverse | 0.40 | 0.40 | 0.25 | 0.80 |
| del_char | 0.00 | 0.00 | 0.00 | 0.20 |
| ins_char | 0.00 | 0.05 | 0.00 | 0.10 |
| sub_char | 0.00 | 0.10 | 0.00 | 0.15 |
| swap_char | 0.00 | 0.00 | 0.00 | 0.05 |
| **mean, 12 tasks** | 0.183 (0.146 to 0.225) | 0.350 (0.296 to 0.400) | 0.175 (0.1375 to 0.217) | 0.5375 (0.492 to 0.583) |
| **mean, five word tasks** | 0.18 (0.12 to 0.24) | 0.56 (0.46 to 0.65) | 0.18 (0.12 to 0.24) | 0.79 (0.72 to 0.86) |

  `O_plain` equals `O` on every task. Joined − O +0.167 (0.104 to 0.225) over the 12 tasks and +0.38 (0.28 to 0.49) on the word
  tasks (`results.differences.{all,word}.all_minus_O.mean`); joined − F −0.1875 (−0.25 to −0.125); S − O −0.008 (−0.029 to 0.013)
  (`results.pair.cute.differences.<name>.mean`). Fixed and broken against O alone (`results.pair.cute.fixed_broken_vs_O`): join 57
  and 17; S 3 and 5; F 87 and 2. By the old rule (`summary.means_old_rule.all`): O 0.1875, joined 0.358, S 0.179, F 0.55.
  `join_1`'s per-task rule (`results.readings.all`) prints "the joined token model does the task" for del_word, sub_word, ins_word,
  swap_word and both means, and "no" for the other eight tasks, contains_char among them.
- **Two-set mean** (`results.pair.two_set_mean`, the mean of the CUTE 12-task mean and the questions' normalized exact match): O
  0.320, joined 0.389, S 0.2875, F 0.460; the better parent per set (F on CUTE, O on the questions) 0.4975
  (`better_parent_two_set_mean`).
- **Printed readings (frozen;** `results.pair.readings`**):** G1 "the token model leads on the questions in this format". For the
  join only "the byte model's skill carries on fresh items (control moved)" (G3, marked by G4). Neither G2 sentence printed: joined −
  F reaches −0.0025, so "the join keeps the host's lead" does not hold (nor does its second condition: joined − O's lower end is
  −0.07, below −0.04) [corrected 2026-11-11, AUDIT b §8.8], and joined − O reaches 0.01, so "the join gives the host's
  lead away" does not hold. `control_within` false: S − O is −0.0575 on the questions, outside ±0.04, and −0.008 on CUTE.
- **Two readouts from the stored rows** (`results/pair_1/readouts.{py,json}`; no model run; every recomputed question flag and
  pair_1's accuracies asserted equal to the stored ones).
  - (a) Questions, normalized answers (the stored `answer` under SQuAD's rule; `a_questions_normalized_answers`). The join's answer
    equals both parents' on 141 items, O's only on 82, F's only on 33, neither on 144. On the 218 items where O and F answer
    differently it equals O's on 82, F's on 33, neither on 103. The no-skill join's answer equals O's on 256 of 400 (the F join's on
    223). Right and wrong, O and F (`right_wrong_patterns_O_F`): both right 125 (the join right on 106), O only 58 (39), F only 28
    (11), both wrong 189 (15; the S join 10).
  - (b) contains_char by word length (`b_contains_char_by_word_length`; the word is `word_or_sentence` in the item file,
    stripped). `pair_1`'s 20 fresh items are all words of 4 or more letters: the join is right on 10 of 20 (it answers "Yes" on 14:
    7 right, 7 wrong), O on 11, F on 10 (F answers "No" on all 20, O on 19). In `join_3`'s 40 items: 19 words of 1 to 3 letters
    (join right on 18, O 9, F 9) and 21 of 4 or more (join 16, O 11, F 11). Pooled over words of 4 or more letters in the two:
    join 26 of 41, O 22, F 21. Why the samples differ: the published contains_char items hold 112 words of 1 to 3 letters in 1,000
    (`steps.items.cute_counts.contains_char.word_lengths.published`); `join_2` left out the words of the match connection's items,
    and the 179 items that each character task kept are about half short words (`join_2`, `summary.character_tasks`). Found while
    checking this: `join_1`'s 20 dev items are all words of 4 to 9 letters, rarer than the published words (for example "nomadism",
    "genista"), and there the join was right on 16 of 20 against O's 8 (scored on the first len(gold) bytes, not strict;
    `join_1_dev_first_len_gold_bytes`). Pooled over the three samples' words of 4 or more letters: join 42 of 61, O 30.
- **Samples** (`decodes.jsonl`, which stores no probabilities; prompts from `bank/jeopardy_1/out/jeopardy_items_5shot.jsonl` and
  `bank/smoke_7/season_1/published.jsonl`; the question's last block is shown).
  `jeopardy:01780`, `Category: LITERATURE\nQuestion: English poet who wrote Endymion,<br />Hyperion, and its unfinished revision,
  The Fall of Hyperion\nAnswer: "`, gold `John Keats`: O `John Keats"` (right); the join `John Keats"` then `\n\n` (right); S
  `william shakespeare"` (wrong); F `John Milton"` (wrong). The join kept the host's answer where F's was wrong.
  `jeopardy:01274`, `Category: LITERATURE\nQuestion: Chapters in this James Bond novel include Gem Quality & Hot Ice\nAnswer: "`,
  gold `Diamonds Are Forever`: O and S `Diamonds Are Forever"` (right); F and the join `Casino Royale"` (wrong). The join took the
  donor's answer.
  `jeopardy:00343`, `Category: SCIENCE\nQuestion: Next in the sequence: pentagon, hexagon, heptagon...\nAnswer: "`, gold `octogon`
  (so spelled in the dataset): the join `Octagon"`, scored wrong; O, S and F wrote heptagon. Exact match counts this answer wrong.
  `published:contains_char:002923`, `Is there a " t " in " environmental "? Answer: "`, gold `Yes`: the join `Yes"` (right); O, S
  and F `No"` (wrong). `published:contains_char:002907` (" p " in " brand ", gold `No`): the join `Yes` (wrong); O, S and F `No"`
  (right).
- **Readings (the coordinator's; one run):**
  1. The token model's lead on the questions exists in free generation: O − F +0.075 (0.0325 to 0.12). The pair has a gap in each
     direction (on CUTE F − O +0.354), so "above both parents" can be tested on it.
  2. The all-heads join is not above both parents: two-set mean 0.389 against F's 0.460 and 0.4975 for the better parent per set.
     In the token model's shell the join reaches 0.35 on CUTE against F's 0.54 (the character tasks do not come across), and it
     reads 3 points below O on the questions.
  3. The join does not give the host's lead away, as the coordinator expected it would. It sits between the parents on the
     questions (0.4275; O 0.4575, F 0.3825), and neither frozen G2 sentence holds. The no-skill donor lowers the host by 5.8
     points (interval −0.0925 to −0.0225), so the control moved: part of the join's cost on the questions is the byte model's
     reading of the prompt entering through the attention outputs, whatever the donor's skill. F's join costs less than S's
     (−0.030 against −0.0575).
  4. On the questions the joined answer is mostly the host's. Where the parents differ it equals O's answer on 82 items and F's on
     33 (neither on 103), with every attention output at matched rows replaced by F's. The no-skill join, which never saw F, equals
     F's on 18 of these 218. On the 132 items both parents miss with different answers it takes O's on 33 and F's on 15, so the
     preference for the host is not only a preference for the right answer. On CUTE, by the same measure, the F join takes F's text:
     123 against 38 in `join_3`, 58 against 20 here [corrected 2026-11-11, AUDIT b §8.6]. So in this join the editing procedure
     travels with the donor's attention writes, and the answer to a factual question stays with the host's shell (its embeddings,
     MLPs and unembedding). This is the first sign of a host contribution. (A sentence that set this beside a published picture of
     factual recall is dropped: no paper was read for it [corrected 2026-11-11, AUDIT b §8.6].)
  5. Correction to `join_2`, `join_3` and `join_4` on contains_char. On 20 fresh items, all words of 4 or more letters, the join
     reads 10 of 20. The earlier reads (0.78 to 0.85) came from a sample in which about half the words had 1 to 3 letters. On those
     the join is right on 18 of 19 (`join_3`); on longer words it is right on 16 of 21 in `join_3` and 10 of 20 here (26 of 41 pooled). The
     audit had flagged the short words (`AUDIT_2026-11-11.md` §8.16). For the sentence "F's late attention writes carry the item's
     answer although F's own output says No": on words of 1 to 3 letters the join is right on 18 of 19, O on 9. On words of 4 or
     more letters it is uncertain. The join is ahead of O on 20 rare dev words (16 against 8, loose rule) and on `join_3`'s 21 (16
     against 11), and not on `pair_1`'s 20 fresh words (10 against 11). `join_3`'s and `pair_1`'s rates do not differ beyond chance
     (Fisher p = 0.11) [corrected 2026-11-11, AUDIT b §8.5].
     One earlier sample does not fit this: `join_1`'s 20 dev words, all of 4 to 9 letters, gave 16 of 20 against O's 8 (loose rule,
     rarer words). So on words of 4 or more letters two earlier samples show a gain and the one fresh sample shows none; the effect
     is not quoted until read on more fresh words. The sentences that state it are corrected in place (tag
     `[corrected 2026-11-11, pair_1]`).
  6. What follows: `GRAFT.md` first steps, 18 (`q_token_rows`).
- **Limits:** one run; 20 CUTE items per task; the questions are 400 items of one dataset in five categories; question scoring is
  exact match after normalization, a lower bound on right answers (`jeopardy:00343`); the control moved (S − O −0.0575 on the
  questions). O's lead comes from literature (44 against 23 of 83) and word origins (27 against 16 of 70); F leads on American
  history. Exact match after normalization misses 29 to 37 right answers per condition (the audit's rulings: O 0.545, F 0.455,
  joined 0.520 in substance); no difference moves by more than 0.02 [corrected 2026-11-11, AUDIT b §8.7].
- **Added 2026-11-11, after this entry was written: contains_char by kind of word, the all-heads join against O alone**
  (recomputed from the stored rows: `out/decodes.jsonl` of `join_1`, `join_3` and `pair_1`, conditions `all` and `O`; the word,
  `stratum` and `word_rank` from `bank/smoke_7/season_1/{published,dev}.jsonl`; equal to `results/pair_1/readouts.json`
  `b_contains_char_by_word_length`).
  - Words of 1 to 3 letters (published; `join_3`; all 19 have 3 letters; strict): joined 18 of 19, O 9 of 19.
  - Rare words of 4 or more letters (`join_1`'s 20 dev items, stratum "fresh", `word_rank` 151,943 to 310,036, median 233,174;
    for example "nomadism", "genista", "forktail"): joined 16 of 20, O 8 of 20. Scored on the first len(gold) bytes: these decodes
    stop there when right, so the strict rule cannot be applied.
  - Published words of 4 or more letters (`join_3` 21 and `pair_1` 20; strict; the published items store no `word_rank`; for
    example "information", "brand", "committee"): joined 26 of 41, O 22 of 41.
  - The coordinator's reading, untested: a rare word is split into several rows, so its letters lie across rows; a common word
    sits in one row, where `letters_1` found the middle letters unreadable.

<!-- JOURNAL.md lines 2631 to 2762 -->
## 2026-11-11, `dist_1`: the no-map join does not reach stage 1's end, the nearest stage-1 checkpoint (the 24 public stage-2 checkpoints of ingredient 3, nearer to `main` by the model card's account, were not tried) [corrected 2026-11-11, AUDIT c §8.5]; with stage 1's end (0.988 of `main`'s steps, by the model card's account; `main` is not byte-equal to any public branch) [corrected 2026-11-11, AUDIT c §8.3] [by its weights H is not on `main`'s run as stored: every weight matrix has a cosine within ±0.002 with `main`'s, and no linear map relates the two models' embeddings (`diff_1`; AUDIT d §4); the step share is the branch name's] [corrected 2026-11-11, AUDIT d §8.4] as host, joined to F and joined to S both read 0.000 on the word tasks (the host alone 0.170) and write unrelated text, and so do the 50% and 10% checkpoints; on `main` the join reproduces `join_3` (0.175 alone, 0.630 joined to F)

- **Seeding the weights** (CPU): `infra/aws_pg/seed_launch_cpu.sh` with `SEED_TAG=dist_1` and the three revisions in `SEED_REPOS`
  (`NOTES_join.md` on the tails branch, "Seeding"); instance `<instance>`, m7g.medium. Launched about 09:36:35Z: the
  launcher sets its reaper `pg-reap-<instance>` at launch plus 6 h 10 min, for 15:46:35Z, and the schedule was created
  09:36:35Z (`aws scheduler get-schedule`, read-only, 11:00Z); EC2 no longer lists the instance at 11:00Z. DONE marker
  `s3://<s3-bucket>/seed/dist_1/DONE` at 09:40:28Z (its text "Wed Nov 11 09:40:27 UTC 2026"); `seed.log` there prints
  "SEEDED" for each revision and "SEED_OK", then the instance shuts itself down (`seed_weights_cpu.sh:20`; shutdown behaviour
  terminate). Under `s3://<s3-bucket>/weights/hf/hub/models--allenai--OLMo-2-0425-1B/snapshots/` (`aws s3 ls
  --summarize`, 11:00Z): `9d3e4365…`, `a2105044…` and `7439d5c4…`, 11 objects and 5,949,374,037 bytes each; `main`'s `a1847dff…`,
  12 objects and 5,949,386,929 bytes.
- **Run:** `results/bytegraft/join/dist_1` (STATUS `exit=0`, S3 time 10:52:14Z; `out/metrics.json`
  `steps.{models,items,known_answers,plan,progress,reproduction,host_<revision>_known,host_<revision>,results,summary}`,
  `out/decodes.jsonl` 2,800 rows: `main`'s `O_plain`, `O`, `all`, `S` and F's stored record, then each earlier host's `O`, `all` and
  `S`, which carry `host`), `bytegraft_join` at `68bd16ab2` (`out/args.json` `PG_GIT_SHA` `68bd16ab2ce4`), instance
  `<instance>`, g6e.2xlarge, launched 09:42:31Z (EC2, read-only), first heartbeat 09:43:07Z. Reviewed before launch
  (`review_2026-11-11_dist1.md` on the tails branch): W1 fixed (the deciding sentence reads the skill part, joined to F − joined to
  S, against `main`'s skill part; the gain's sentence is printed beside it), C1 fixed (paired intervals of the skill part against
  half and a quarter of `main`'s). Items (`steps.items`): `join_3`'s 200 word-task items, strict. Decode seconds: `main` 673.7
  (`progress.seconds`); the earlier hosts 917.3, 972.5 and 984.4 (`host_<revision>.seconds`); GPU peak 24.85 GB
  (`summary.memory`).
- **Hosts** (`steps.summary.dist.<host>.{steps,fraction_of_main_steps,distance}`). The distance is sqrt(Σ‖W_host − W_main‖² /
  Σ‖W_main‖²) over the 176 body tensors (q, k, v, o, the two q/k norms, gate, up, down and the two layer norms of 16 layers), in
  float64.

| host | revision | commit | steps (`main`'s by the model card's account) [corrected 2026-11-11, AUDIT c §8.3] | share of `main`'s | distance from `main` |
|---|---|---|---|---|---|
| `main` | `main` | `a1847dff…` | 1,931,211 | 1.000 | 0 |
| stage 1's end | `stage1-step1907359-tokens4001B` | `9d3e4365…` | 1,907,359 | 0.988 | 1.106 |
| 50% | `stage1-step970000-tokens2035B` | `a2105044…` | 970,000 | 0.502 | 1.325 |
| 10% | `stage1-step190000-tokens399B` | `7439d5c4…` | 190,000 | 0.098 | 1.431 |

  The step shares in this table: [by its weights H is not on `main`'s run as stored: every weight matrix has a cosine within ±0.002
  with `main`'s, and no linear map relates the two models' embeddings (`diff_1`; AUDIT d §4); the step share is the branch name's]
  [corrected 2026-11-11, AUDIT d §8.4].

  Hub facts (`NOTES_join.md`, "Facts", the hub's API read 2026-11-11, metadata only): 268 branches, no tags: `main`, 195 stage-1
  branches and 3 × 24 stage-2 branches (ingredients 1 to 3). No branch equals `main` byte for byte (the safetensors' sha256 differ;
  names, shapes and offsets are equal). `main`'s step count rests on the model card, which says of the 1B: "only 1 version is
  trained on a 50B mix (ingredient 3), we did not merge" (README of `allenai/OLMo-2-0425-1B`, read for this entry). So `main` is
  taken as stage 1's 1,907,359 steps plus ingredient 3's 23,852; the card gives tokens, not steps.
- **Conditions per host:** alone (`O`, the step path); joined to F (`all`: every head, at every row matched by both F's and S's
  parses); joined to S (`S`). At an earlier host S's body is `main`'s, so the S join writes `main`'s attention outputs (on S's
  parse) in place of the host's; the skill part (joined to F − joined to S) reads F's skill over them (`NOTES_join.md`, "What assumed
  the host is main").
- **Known answers passed** (`known_answers.gates`, 19): `main`'s 1 to 6 (as in `srows_1`, the entry above) and 10 (`O_plain`, `O`,
  `all` and `S` reproduce `join_3`'s stored strict texts and both flags on the 200 items; `reproduction.differ` empty); for each
  earlier host (`host_<revision>_known`): 17, its tensor names and shapes equal `main`'s; 18, its state root differs from `main`'s;
  19, its own heads as the donor give its own tokens (`identity_differ` empty); 20, the empty head set gives its own tokens
  (`empty_differ` empty).
- **Results** (word-task mean, strict; `steps.summary.dist.<host>`; per task in `steps.results.dist.<host>.accuracy`; every value
  recomputed from the strict flags and re-scored from text and gold, equal, in `results/dist_1/recompute.json` `hosts`). The
  first-token accuracy is the host alone's top token after the prompt against the gold's first token, on the first 50 of
  `pair_1`'s questions (not gated; not in the rows, so not recomputed).

| host | alone | joined to F | joined to S | gain (joined to F − alone) | skill part (joined to F − joined to S) | S − alone | first-token, 50 questions |
|---|---|---|---|---|---|---|---|
| `main` | 0.175 | 0.630 | 0.185 | +0.455 (0.38 to 0.525) | +0.445 (0.365 to 0.515) | +0.010 (−0.015 to 0.035) | 0.34 |
| stage 1's end | 0.170 | 0.000 | 0.000 | −0.170 (−0.215 to −0.125) | 0.000 (0.0 to 0.0) | −0.170 | 0.26 |
| 50% | 0.140 | 0.000 | 0.000 | −0.140 (−0.175 to −0.105) | 0.000 (0.0 to 0.0) | −0.140 | 0.28 |
| 10% | 0.115 | 0.000 | 0.000 | −0.115 (−0.15 to −0.08) | 0.000 (0.0 to 0.0) | −0.115 | 0.12 |

  The host alone per task (`steps.results.dist.<host>.accuracy.O.<task>.mean`; contains_word, del_word, ins_word, sub_word,
  swap_word): `main` 0.475, 0.025, 0.125, 0.250, 0.000; stage 1's end 0.550, 0.025, 0.150, 0.125, 0.000; 50% 0.550, 0.000, 0.100,
  0.050, 0.000; 10% 0.475, 0.000, 0.075, 0.025, 0.000. Both joins read 0.000 on every task at every earlier host. Items whose tokens
  differ from the host alone (`tokens_differ_from_alone`): `main` 155 (F join) and 26 (S join); 200 and 200 at each earlier host.
  The earlier host alone writes a text other than `main` alone's on 138, 125 and 127 of 200 items (`recompute.json`
  `alone_text_differs_from_main_alone`). Each join's landed change after the host's norm over the host's own attention output, mean
  over layer-steps (`landed_relative_to_own`, measured inside each joined forward): `main` 0.60 (F join) and 0.06 (S join); stage
  1's end 2.17 and 2.18; 50% 2.21 and 2.22; 10% 1.94 and 1.87.
- **Unrelated text, counted** (`recompute.json` `hosts.<host>.joined_texts_holding_a_word_of_the_sentence`; the text before the
  first quote against the item's sentence, `word_or_sentence` in the bank, lower-case words of letters a to z). At stage 1's end,
  50% and 10%, joined to F holds any word of the sentence on 40, 66 and 29 of 200 texts, joined to S on 36, 59 and 29; the shared
  words are function words ("the", "a", "and", "to"; "the" on 18 of the stage-1-end F join's 40). A word of 4 or more letters:
  joined to F 1, 1 and 0; joined to S 3, 1 and 0. For reference, the host alone holds a word of 4 or more letters on 158, 157 and
  155 (any word on 160, 160 and 157, every edit-task item at the first two), and `main`'s F join on 158 (any word 160). On
  contains_word the right answer is Yes or No, so no right text holds a sentence word there. Against another item's sentence of the
  same task, the same counts at stage 1's end are 1 and 2 (a word of 4 or more letters) and 40 and 32 (any word): the joined texts
  follow the item no more than another item. 7 of 160 F-join edit texts start with a space (host alone 160)
  (`results/audit_2026-11-11c/audit_dist1.json` `follows`, `edit_texts_starting_with_space_of_160`) [corrected 2026-11-11, AUDIT c
  §8.8].
- **Printed readings (frozen;** `steps.summary.dist.<host>.reading`, `gain_reading`**):** `main` "the join carries F's skill at this
  distance", its gain "the join works at this distance"; each earlier host "it does not at this distance", its gain "the join fails
  at this distance". Skill part minus half and a quarter of `main`'s (`skill_minus_half_main`, `skill_minus_quarter_main`): `main`
  +0.2225 (0.1825 to 0.2575) and +0.334; each earlier host −0.2225 (−0.2575 to −0.1825) and −0.111 (−0.129 to −0.091).
- **Samples** (`recompute.json` `samples`: four items per host, the first of contains_word, del_word, ins_word and sub_word in item
  order, with prompt, gold and the three texts; `decodes.jsonl` stores no probabilities). `published:contains_word:003598`, `Is
  there a " into " in " John walked into his bedroom. "? Answer: "`, gold `Yes`: `main` alone and joined to F `Yes"` (right). Stage
  1's end: alone `Yes"` (right), joined to F `rial`, joined to S `locally`. 50%: alone `Yes"`, joined to F `saying`, joined to S
  `safety`. 10%: alone `No"` (wrong), joined to F `junk`, joined to S `BOYS`. `published:ins_word:007361`, `Add " unit " after
  every " does " in " It does not fit. ". Answer: "`, gold ` It does unit not fit.`: stage 1's end alone ` It does not unit does
  fit` (wrong), joined to F `rightness of just a few years`; 50% alone ` It does not fit unit does`, joined to F `broadly
  speakingpand the`, joined to S `broadly speaking plz`; 10% joined to F ` pack of theiiisticly" and`, joined to S `Charlotte
  rowton-lympho,`. `published:del_word:009539` (delete " they " in " And they lived happily ever after. "): `main` joined to F ` And
  lived happily ever after. "` (right); stage 1's end alone ` they lived happily. "` (wrong), joined to F `isses,isses,coma,
  whichsy, which`. The joined texts are not editing attempts.
- **Readings (the coordinator's; one run):**
  1. The no-map join does not reach stage 1's end, the nearest stage-1 checkpoint (the 24 public stage-2 checkpoints of ingredient
     3, nearer to `main` by the model card's account, were not tried) [corrected 2026-11-11, AUDIT c §8.5]. At 0.988 of `main`'s
     steps (by the model card's account; `main` is not byte-equal to any public branch) [corrected 2026-11-11, AUDIT c §8.3] [by its
     weights H is not on `main`'s run as stored: every weight matrix has a cosine within ±0.002 with `main`'s, and no linear map
     relates the two models' embeddings (`diff_1`; AUDIT d §4); the step share is the branch name's] [corrected 2026-11-11, AUDIT d
     §8.4] the joined text is unrelated strings for both donors (a word of 4 or more letters of the item's sentence in 1 and 3 of
     200 texts), and likewise at 0.502 and 0.098.
  2. The cause is not a weak host. Each earlier host works alone (word tasks 0.170, 0.140 and 0.115 against `main`'s 0.175;
     first-token 0.26, 0.28 and 0.12 against 0.34) (its own-heads and empty-set known answers pass for any model of this shape; that
     each host is the named checkpoint rests on the snapshot path, weight shards whose S3 ETags differ per revision, config and
     tokenizer files equal across the four, and each host's own accuracy) [corrected 2026-11-11, AUDIT c §8.7]. `main`'s body
     weights lie at a relative Frobenius distance of 1.106 from stage 1's end (1.431 for the 10% host). That measure counts changes
     of scale, and OLMo-2's q_norm, k_norm and post-sublayer norms make the overall scale of q_proj, k_proj, v_proj with o_proj and
     up_proj with down_proj irrelevant to the function; the two checkpoints' norms were not recorded, so it does not say how far the
     function moved. In activations the two are far apart: at the first step, at layer 0, on the same prompt tokens, `main`'s
     attention output (through S) lands a median 1.85 times the host's own write away from it after the host's norm (0.046 on
     `main`), and stage 1's end alone writes `main` alone's text on 62 of 200 items and the 50% host's on 94. That attention outputs
     computed in `main`'s body are not in the earlier hosts' coordinates is the reading that fits
     (`results/audit_2026-11-11c/audit_dist1.json` `first_step_landed_over_own_median_by_layer`,
     `joined_texts_equal_across_earlier_hosts`, `alone_text_differs_from_main_alone`) [corrected 2026-11-11, AUDIT c §8.6].
  3. So research pass 7's objection (`research_pass_2026-11-11a.md` §8 item 1) holds in its strong form: this is consistent with
     every join of this study working because F and S stayed in `main`'s coordinates (S by construction; F through Bolmo's stage 2,
     which started from S; F's distance from `main` was not measured) [corrected 2026-11-11, AUDIT c §8.8]. G4: the first measured
     point is all or none. [by its weights H is not on `main`'s run as stored: every weight matrix has a cosine within ±0.002 with
     `main`'s, and no linear map relates the two models' embeddings (`diff_1`; AUDIT d §4); the step share is the branch name's]
     [corrected 2026-11-11, AUDIT d §8.4]. A no-map join reaches distance 0 and nothing else that was tried.
  4. What follows: `GRAFT.md` first steps, 20 (`map_1`).
- **Limits:** one run; four hosts; word tasks only, on 200 items decoded before on `main`. The distance is over weights, not
  activations; its known answers are on fake models only (0 for an identical host, 0.436 for a permuted one; the dry run in
  `NOTES_join.md`), and no near pair of real checkpoints was measured. The steps between stage 1's end and `main` are confounded
  with stage 2's different data (Dolmino-Mix-1124, 50B tokens; the model card), which no public branch separates. [by its weights H
  is not on `main`'s run as stored: every weight matrix has a cosine within ±0.002 with `main`'s, and no linear map relates the two
  models' embeddings (`diff_1`; AUDIT d §4); the step share is the branch name's] [corrected 2026-11-11, AUDIT d §8.4]. The 24
  public stage-2 checkpoints of ingredient 3 (step 1,000 to 23,852) lie between stage 1's end and `main` and were not tried.

<!-- JOURNAL.md lines 2924 to 2989 -->
## 2026-11-11, the third independent audit (`srows_1`, `dist_1`, `map_1`): every headline number recomputes equal; `srows_1` holds as written; `dist_1`'s headline holds with two wrong sentences and a weight-distance reading that says more than the norm can; `map_1`'s skill verdicts do not count as a test of a linear map, because the maps fail their identity pair

- **Who and how:** Claude Opus 5.5 (the commit's attribution), a different model from the coordinator. No model run. Every number
  was recomputed from the stored per-item rows (local copies of S3 `results/bytegraft/join/{srows_1,dist_1,map_1,join_3,join_4}/out/`,
  each checked against S3 by ETag; the gold file `bank/smoke_7/season_1/published.jsonl`, MD5 equal to S3); every text was re-scored
  from text and gold, never from the stored flag; own bootstraps, 10,000 draws within task, seed 20261111; job code read at the
  launch commits `68bd16ab2` and `8729b1975`. Report `AUDIT_2026-11-11c.md`; scripts and outputs
  `results/audit_2026-11-11c/audit_<run>.{py,json}`; commit `e506bec05`, merged `2b2a7a521`. The 15 sentences of its §8 are
  corrected in place above, in `GRAFT.md` and in `HANDOFF.md`, each tagged `[corrected 2026-11-11, AUDIT c §8.<n>]`; before each
  was applied, its number was read from the evidence key it cites (all 15 matched). Not checked by the audit (its own list): the
  first-token accuracies; known answer 22; EC2 launch times; which tensors carry the weight distance; the S3 weight files against
  the hub's sha256; the papers cited in step 21.
- **Its first line, verbatim:** "Of the three runs, `srows_1` holds as written; `dist_1`'s headline holds, but "the nearest earlier
  public checkpoint" and "every earlier public checkpoint" are wrong (3 of 267 branches were tried) and the weight-distance reading
  says more than a Frobenius norm can; `map_1`'s skill verdicts do not count as a test of a linear map, because the map fails its
  identity pair (`main`'s own writes through it change 194 of 200 texts). Every headline number recomputes equal from the rows."
- **Re-scoring:** 0 of 800 `srows_1` strict flags differ from the re-scored ones; 0 at every `dist_1` host, where the strict and
  lenient reads agree everywhere; 0 of 1,400 `map_1` flags. `map_1`'s host-alone texts equal `dist_1`'s on 200 of 200.
- **WRONG** (a number or a sentence must change):
  - `dist_1`, title and reading 1: "the nearest earlier public checkpoint"; by the model card's account the 24 public stage-2
    checkpoints of ingredient 3 lie between stage 1's end and `main` (§8.5).
  - `GRAFT.md` "State of the evidence" (i): "unrelated text at every earlier public checkpoint"; three of the 267 branches other than
    `main` were tried (§8.4).
  - `map_1`, reading 1: "F's difference from S lies outside what they transmit at five layers". The qualifier measures coverage of
    `main`'s variance on the fit prompts, and at four of the five layers the map passes F's difference with 2.0 to 2.6 times its
    gain on `main`'s rows (§8.11).
  - `map_1`, title: the maps do not reproduce the host (`main`'s own writes through them change 194 of 200 texts), so "does not
    carry F's skill" says more than the run can (§8.9).
- **WEAKER** (the result carries less than the text said):
  - `srows_1`, reading 1: the +0.020 is contains_word alone (`S_rows` answers Yes on 35 of 40, O on 15, gold 20); on the four edit
    tasks `S_rows` and O are each right on 16 of 160. In size the control pushes harder than F did, not less: a median 1.21 of
    `deciding`'s landed size at the first step (layers 1 to 15), 1.45 summed over layers at every step (§8.1). Limits: the 0.0 gap at
    layer 0 is the target's; the landed sizes differ by up to 0.0005, the bisection's tolerance (§8.2).
  - `dist_1`: `main`'s step count, and so 0.988, 0.502 and 0.098, rests on one sentence of the model card (§8.3). The relative
    Frobenius distance counts changes of scale, which OLMo-2's norms make irrelevant to the function for q_proj, k_proj, v_proj with
    o_proj, and up_proj with down_proj; the activations say how far apart the two are (`main`'s attention output, through S, lands
    a median 1.85 times the host's own write away from it at layer 0 of the first step, against 0.046 on `main`), and so do the texts
    (stage 1's end alone writes `main` alone's text on 62 of 200) (§8.6). Known answers 17 to 20 pass for any loaded model of this
    shape; that each host is the named checkpoint rests on the snapshot path, shard ETags that differ per revision, equal config and
    tokenizer files, and each host's own accuracy (§8.7). Reading 3 is consistent with the run, not tested by it; the "unrelated
    text" counts hold against a null from another item's sentence (1 and 2, 40 and 32) (§8.8).
  - `map_1`: no positive control fired on the real models and the maps fail their identity pair, so by CLAUDE.md, Instruments 4,
    the skill readout does not count as a test of whether a linear map carries F's skill. On the four edit tasks F and S through the
    question-fitted maps are each right on 0 of 160 (the host alone 12), so the skill part sits at the instrument's floor, and the
    −0.120 is contains_word (§8.9). The fidelity failure after the host's norm is 1.00 and 0.42 of the host's own write, against
    0.60 for F's whole correction on `main`; the task-format maps' 0.21 is largely in-sample, because each word task's few-shot lines
    are in their fit text (§8.10, §8.12). The rule was frozen in the job code 86 s before the launch, and GRAFT step 20 held none
    (§8.13). Gate 23 cannot detect a transposed map, a map applied in the wrong direction or a fault in the byte-donor path (§8.14).
    The λ edge does not limit the fit; the matched rows are 96% of rows and `S_map` on them fails as `main_map` does (§8.15).
- **Controls that could not have failed, or could fail only one way** (its §5): `srows_1`'s band (fails only
  through saturation; the largest share at any layer is 7.4%); `dist_1`'s known answers 17 and 19 (no registered failing input) and
  17 to 20 together (they pass for any loaded model of this shape); `dist_1`'s skill part at the earlier hosts (both joins at 0,
  interval [0, 0]); `map_1`'s qualifier (r has a floor and no ceiling); `map_1`'s fidelity note (printed, not gated); `map_1`'s gate
  23 (the identity is symmetric). Quantities defined after the runs: the "unrelated text" counts (`dist_1`) and the "partly follows"
  counts (`map_1`, reading 5); the audit's nulls from another item's sentence support both. Read on different item sets:
  `F_shuffled` and `F_procrustes` (100 items) against the others (200), with H alone on the same 100 beside them.
- **What follows:**
  - (a) `GRAFT.md` G4 and "State of the evidence" (i) now say that `map_1` does not count as a test of whether a linear map carries
    the skill.
  - (b) Two rules added to `GRAFT.md` "How we size work": a known answer is listed with the input that makes it fail, and one that
    any loaded model passes is called a code check; a rule is written into `GRAFT.md` before launch, not only into the job code.
  - (c) `GRAFT.md` first steps, 21 (`diff_1`), amended before launch after the audit's §6 and the pre-launch review: a no-map
    baseline at H; a control per map from another item of the same task; a positive control per map on the real models
    (`transport_cosine`); R read on the same 200 items as the maps; the four edit tasks as the deciding quantity, contains_word
    printed apart; the fresh items named (`pair_1`'s 80 edit-task items).

<!-- JOURNAL.md lines 3207 to 3337 -->
## 2026-11-11, `diff_2`: `diff_1`'s gain holds on 80 fresh edit items (0.075 to 0.263, following the item), and it is an output-level effect: the same vectors written once to the final norm's input, with nothing written inside the host's body, give the same accuracy (0.294 against 0.281), and proxy tuning on the donors' body outputs through `main`'s readout reaches the same level (0.269); the same map carries the gain into two more separately trained networks (+0.225, +0.175), and a rotation fitted on activations carries part of it (+0.150)

- **Runs:** both from `bytegraft_join` at `988d97f76` (branch `research/bytegraft-tails`; `out/args.json` `PG_GIT_SHA`
  `988d97f7674d`). Run A: `results/bytegraft/join/diff_2a` (STATUS `exit=0`, S3 time 17:15:21Z), instance `<instance>`,
  g6e.2xlarge, launched 16:16:39Z (EC2, read-only), first heartbeat 16:17:35Z; decodes 2,634.6 s (`progress.seconds`), GPU peak 31.35
  GB. Run B: `results/bytegraft/join/diff_2b` (STATUS `exit=0`, 17:12:06Z), instance `<instance>`, g6e.4xlarge, launched
  16:18:30Z, first heartbeat 16:20:08Z; the 50% and 10% hosts 557.8 s and 570.1 s, the rotation fits 345.3 s, the rotation decodes
  949.7 s; GPU peak 36.59 GB. Plan and rules: `GRAFT.md` first steps, 22, with its two dated additions (the amendment after the
  pre-launch review, and the note on how the sentences are read, written before any number was opened). Reviewed before launch
  (`review_2026-11-11_diff2.md`, at `f1a51b89a`: W1, P1 is not `dF_U`'s matched direct-path control, so P1H was added; W2, the
  rotation maps' sentence built from `diff_1`'s amended rule; both fixed at `988d97f76`). The stored rows now carry their true
  condition and host, and in run A a `set` field ("fresh" or "diff_1 items"); no (host, set, condition, item) occurs twice. `dF_U` on
  `diff_1`'s 200 items is `diff_1`'s stored rows (known answer 32 re-decodes 20 of them and reproduces all 20 texts), as is `dF_idH`
  at H in run B (known answer 38). Recomputation: `results/diff_2/recompute.json`, from both runs' rows and `diff_1`'s.
- **Known answers passed:** run A 14 (`steps.summary.gates`): `main`'s 1 to 6; H's 17 and 18 (code checks); 27, H alone reproduces
  `map_1`'s stored texts; 32, `dF_U` reproduces `diff_1`'s stored texts (4 items per task); 33, 34, 36 and 37, P1, P2, P1H and P1H
  early with S as both donors give H alone's tokens. Run B 16: `main`'s 1 to 6; 38, `diff_1`'s stored `dF_idH` rows are the 200
  items; for each of the 50% host, the 10% host and H, 17 and 18 (code checks); 35, each earlier host alone reproduces `dist_1`'s
  stored texts; 27 for H.
- **Conditions.** Run A, host H (stage 1's end). Fresh set: `pair_1`'s fresh items of the five word tasks (100; 80 edit items decide,
  20 contains_word printed apart; none of `diff_1`'s 200): H alone, `dF_U`, `dF_U_late`, `dF_idH`, and `dF_U_other` with pairs drawn
  inside the fresh set by `join_3`'s rule (all 100 pairs from the fresh set, `steps.diff2_setup.fresh_pairs`). On `diff_1`'s 200: P1,
  `main`'s unembedding read of d (through `main`'s final-norm gain), summed over the 16 layers and added to H's logits at the
  deciding rows; P2, `main`'s final norm and unembedding applied to F's and to S's last body state at the deciding row, their
  difference added to H's logits; P1H, the same vectors `dF_U` writes (Σ over the 16 layers of ρ·T·d) added once to H's final-norm
  input at the deciding rows, with nothing written inside the body; P1H early, the same over layers 0 to 11; `dF_U_early` (`U` at
  layers 0 to 11) and `dF_U_15` (`U` at layer 15 only). Run B: `dF_U` and its other-item control (on the 100-item subset) at the 50%
  host (`stage1-step970000-tokens2035B`) and the 10% host (`stage1-step190000-tokens399B`), each with its own `U` fit and ρ; at H,
  `dF_proc` (per-layer orthogonal Procrustes between `main`'s and H's landed attention writes, task-format fit text) and `dF_Eproc`
  (orthogonal Procrustes with one scale between the token-embedding rows), each with its other-item control.
- **Fresh read** (run A, `steps.results.diff2.accuracy`, `differences`; right counts from `recompute.json` `conditions`; 80 edit
  items, 20 per task; strict equals lenient): H alone 6 of 80 (0, 3, 3, 0 per edit task; 0.075); `dF_U` 21 (2, 10, 8, 1; 0.263);
  `dF_U_late` 21 (2, 7, 9, 3; 0.263); `dF_idH` 4 (0.050); `dF_U_other` 7 (0.0875). `dF_U` − H alone +0.1875 (0.100 to 0.275), 16 fixed,
  1 broken; `dF_U` − `dF_U_other` +0.175 (0.0875 to 0.2625) (0.100 to 0.2625 with independent task draws, AUDIT h2); `dF_U_other` − H
  alone +0.0125 (−0.025 to +0.0625); `dF_U_late` − H alone
  +0.1875 (0.100 to 0.275); `dF_idH` − H alone −0.025 (−0.0875 to +0.0375).
- **The direct path** (run A, on `diff_1`'s 160 edit items; strict, lenient beside where it differs):

| condition | edit tasks, strict, right per task | edit mean, strict | edit mean, lenient | condition − H alone (interval), fixed and broken | stopped at end of text (of 200) |
|---|---|---|---|---|---|
| H alone | 1, 6, 5, 0 | 0.075 | 0.075 | | 0 |
| `dF_U` (`diff_1`'s rows) | 14, 13, 17, 1 | 0.281 | 0.281 | +0.206 (0.150 to 0.2625), 33 and 0 | 1 |
| P1H (the same vectors at the final norm's input) | 13, 14, 16, 4 | 0.294 | 0.294 | +0.219 (0.162 to 0.281), 36 and 1 | 18 |
| P2 (proxy tuning on body outputs) | 9, 16, 15, 3 | 0.269 | 0.275 | +0.194 (0.1125 to 0.269), 37 and 6 | 39 |
| P1 (`main`'s readout of d) | 7, 3, 11, 2 | 0.144 | 0.1625 | +0.069 (0.0 to 0.131), 20 and 9 | 33 |
| `dF_U_early` (layers 0 to 11) | 2, 8, 7, 0 | 0.106 | 0.106 | +0.031 (0.0 to 0.0625), 6 and 1 | 0 |
| P1H early | 3, 7, 5, 0 | 0.094 | 0.094 | +0.019 (−0.0125 to +0.050), 5 and 2 | 0 |
| `dF_U_15` (layer 15 only) | 2, 6, 9, 0 | 0.106 | 0.106 | +0.031 (0.0 to 0.069), 6 and 1 | 0 |

  `dF_U` − P1H −0.0125 (−0.075 to +0.050), 15 items right only with `dF_U` and 17 only with P1H; the two texts are equal on 58 of 200
  items and both are right on 30 edit items. Item by item the direct write's answer equals `dF_U`'s on 58 of the 160 edit items
  (`dF_U` and its late-layer part: 110), so the two reach the same accuracy through partly different outputs: the body adds no
  accuracy that is shown (room for about a quarter of the gain), and it changes what is written
  (`results/audit_2026-11-11e/audit_diff23.json` `differences` "A:dF_U - A:P1H", "A:dF_U - A:dF_U_late") [corrected 2026-11-11,
  AUDIT e §8.10]. `dF_U` − P2 +0.0125 (−0.056 to +0.081); over the 200 items P2 fixes 53 and breaks 14
  against H alone. `dF_U` − P1 +0.1375 (0.0625 to 0.2125) strict, +0.119 (0.0375 to 0.200) lenient. `dF_U_early` − P1H early
  +0.0125 (−0.019 to +0.044). The share P1H gives, (P1H − H alone) / (`dF_U` − H alone), is 1.06 (0.76 to 1.46, 2,000 paired draws
  within task; `recompute.json` `share_P1H`), so the body's share of the gain, beyond the direct write, is at most about a quarter by
  this interval. At the first step's deciding row the cosine between H's logit change under `dF_U` and P1's added logits has mean
  0.806 (quartiles 0.759, 0.903, 0.948; `dF_U_late` 0.801; `steps.summary.logit_account`).
- **Two more hosts** (run B, `steps.results.diff2.hosts`; 160 edit items; strict equals lenient). 50% host: alone 6 of 160 (0, 4, 2,
  0; 0.0375); `dF_U` 42 (10, 17, 13, 2; 0.263), +0.225 (0.169 to 0.281), 37 fixed, 1 broken; − its other-item control +0.2375 (0.150 to
  0.3375) on the subset's 80; the control − alone 0.000 (−0.0375 to +0.0375). 10% host: alone 4 (0, 3, 1, 0; 0.025); `dF_U` 32 (9, 9,
  11, 3; 0.200), +0.175 (0.119 to 0.231), 29 and 1; − other-item +0.175 (0.0875 to 0.250); the control − alone −0.0125 (−0.0625 to
  +0.025). Each host's own `U` fit (`u_map.tokens.U`): held-out error 0.562 and 0.566 against the mean row's 0.665 (H: 0.561); `E`
  0.851 and 0.853 against 0.984 and 0.992; ρ 0.808 and 0.874 (H 0.949). By their weights
  (`steps.diff2_host_<revision>.facts.tensors`, `recompute.json` `hosts_weights`): every one of the 112 weight matrices has a cosine
  with `main`'s between −0.0015 and +0.0025 (50%) and between −0.0013 and +0.0054 (10%), norm ratios 0.67 to 1.04 and 0.82 to 1.18;
  relative distances 1.325 and 1.431. So both are, like H, separately trained networks relative to `main` by their weights. How the
  three stage-1 checkpoints relate to each other was not measured.
- **Rotation maps at H** (run B, `steps.results.diff2.rotation`; 160 edit items; strict equals lenient). `dF_proc` 36 of 160 (11, 12,
  12, 1; 0.225): − H alone +0.150 (0.094 to 0.2125), 25 fixed, 1 broken; − its other-item control +0.175 (0.100 to 0.2625); − no map
  +0.181 (0.119 to 0.250); its control − H alone −0.0125 (−0.075 to +0.050). `dF_proc` − `dF_U` −0.056 (−0.1125 to 0.0, this file's
  draws, not in either job; 6 items right only with `dF_proc`, 15 only with `dF_U`). `dF_Eproc` 17 of 160 (0.106): − H alone +0.031
  (0.006 to 0.0625); − its control +0.0125 (−0.025 to +0.050). Fits (`steps.diff2_rotation_fit`): `proc` held-out relative error 0.62 to
  1.08 by layer against the identity's 1.21 to 1.90; `Eproc` 0.912 against the mean row's 0.984. Transport cosines
  (`steps.summary.transport_cosine`): `proc` 0.268, `Eproc` 0.057, identity 0.001.
- **Printed readings (frozen;** run A `steps.summary.sentences`, run B `distance_sentences`, `rotation_sentences`**):** fresh read
  "holds" (and the `dF_U_late` note "holds"); "a direct write to the final norm accounts for it"; "no use of the early writes beyond
  their direct effect is shown"; "proxy tuning in main's readout does not reach it"; "proxy tuning on body outputs reaches it"; both
  earlier hosts "reaches"; `dF_proc` "carries; above no map; follows the item"; `dF_Eproc` "not readable: this map does not carry
  main's own differences into H's" (its +0.031 is below 0.052, and its transport cosine below 0.5).
- **contains_word** (printed apart; Yes, No): fresh set, H alone 17, 3; `dF_U` 15, 5. On `diff_1`'s items, H alone 34, 6; P1 39, 1;
  P2 11, 28; P1H 37, 3. 50% host alone 32, 8, with `dF_U` 23, 17; 10% host alone 7, 33, with `dF_U` 4, 35.
- **Samples** (`recompute.json` `samples`; no probabilities stored). Fresh `published:del_word:009188` (delete " cat " in " The cat
  was very sad. "; gold ` The was very sad.`): H alone, `dF_U_other` and `dF_idH` ` The cat was very sad` (wrong); `dF_U` ` The was
  very sad. "` (right). Fresh `published:del_word:009106` (delete " say "): `dF_U` ` Sara and Tom say they are sorry` (wrong).
  `published:del_word:009821` (delete " The " in " The store is big and open. "): `dF_U`, P1H and P2 ` store is big and open. "`
  (right); P1 ` store is big and big. "`; H alone ` The store is open. "`. `published:del_word:009539`: `dF_U` right; P1H ` and lived.
  "`, P1 and P2 ` And lived. "` (wrong). At the 10% host the same item: alone ` And they lived happily ever after` (wrong), `dF_U` ` And
  lived happily ever after. "` (right). `published:del_word:009948`: `dF_proc` ` The brave little girl smiled herself. "` (right, as
  `dF_U`; H alone ` to herself. "`).
- **Readings (the coordinator's; one run each; with step 22's reading note applied):**
  1. `diff_1`'s gain was not selection among five maps: on 80 fresh edit items `dF_U` raises H by +0.1875 (0.100 to 0.275), about its
     first size (+0.206), 16 fixed and 1 broken, and it follows the item (+0.175 over the same map on another fresh item's
     difference, which leaves H where it was).
  2. It is an output-level effect. The same vectors written once to the final norm's input, with nothing written inside the body,
     give the same accuracy (P1H 0.294 against `dF_U`'s 0.281; difference −0.0125, −0.075 to +0.050). The body is not shown to take
     part: the share P1H gives is 1.06 (0.76 to 1.46), so a body share of about a quarter of the gain is not excluded. Proxy tuning on
     the donors' body outputs through `main`'s final norm and unembedding, which needs no map into H, reaches the same level (P2
     0.269; − `dF_U` −0.0125 through 0), though it ends the text before the closing quote on 39 of 200 items. So on this pair the
     join into a separately trained network is an output-level addition (P1H); a token-readout form of proxy tuning (`P2`) reaches
     the same accuracy, and the published byte-level form was not run [corrected 2026-11-11, AUDIT e §8.9]. Proxy tuning across
     tokenizers through a
     byte interface is published (2506.14123 §4.4: Llama-3.1-8B with Olmo2-1B-Instruct and Olmo2-1B as expert and anti-expert, GSM8K
     55.3 alone and 76.6 proxy-tuned; found by the owner's check after this run, missed by research passes 1 to 8). What `diff_2` adds
     is narrow: the expert pair is a byte-level model and its own earlier checkpoint (F and S), read through a token model's final
     norm and unembedding, on word editing; a new use of a published method, not a new method.
  3. P1, `main`'s unembedding read of the attention-write differences added straight to H's logits, does not reach it (0.144), while
     the same differences mapped by `U` and passed once through H's own final norm and unembedding (P1H) do. Its added logits point
     mostly the same way as `dF_U`'s logit change (cosine 0.806). What this shows: reading d through `main`'s unembedding and adding
     it at fixed scale is not enough here, while passing `U`'s mapped vectors through H's final norm, which scales them with H's own
     state, is; and P1 often ends the text early (33 of 200). What it does not show: which of the two differences (the scaling by H's
     norm or the direction, mean cosine 0.806) matters, or anything about H's body.
  4. Layer 15 alone gives +0.031 (0.0 to 0.069), though it holds about half of what `dF_U` writes (AUDIT d), and layers 0 to 11 give
     +0.031 as well, while the 16 layers give +0.206 and their summed vectors at the final norm +0.219. The gain is not proportional
     to the size written at one layer.
  5. The same map carries the gain into two more networks with the same tokenizer (+0.225 at the 50% host, +0.175 at the 10% host,
     each following the item), as a logit-level addition predicts: the host needs only the shared vocabulary. These are two more
     networks, not points on a distance axis (step 22's reading note).
  6. A rotation fitted on activations (`dF_proc`) also carries (+0.150, above no map, follows the item); it reads 0.056 below `U`, an
     interval reaching 0. Whether its gain is a direct write too was not tested; step 23's run at H, which would have tested it, is not
     run (the coordinator's decision after the owner's question, `GRAFT.md` first steps, 23).
  7. Never tested anywhere, `main` included: whether a host's body takes part in the original join (AUDIT §8.9 on `heads_1`; `join_4`
     put about two thirds of the gain in the deciding rows' last four layers). Step 23 tests it.
- **Limits:** one run each; 80 fresh items (20 per task); the direct-path test's power (its interval leaves room for a body share of
  about a quarter); P1 and P2 end the text early on 33 and 39 of 200 items, which the strict rule scores wrong; no direct-path control
  for layer 15 alone or for `dF_proc`; the three hosts are public checkpoints named as one stage-1 run, and their relation to each
  other was not measured; the fresh items share each word task's few-shot template with `diff_1`'s items, so they are fresh in items,
  not in format.

<!-- JOURNAL.md lines 3338 to 3416 -->
## 2026-11-11, `diff_3` Run M: on `main` the replace-form join at the deciding rows (0.594 on the edit tasks) is +0.331 above a direct write of the same landed changes to the final norm's input (0.263): about two thirds of the gain come through `main`'s own layers; the writes at layers 0 to 11 have no direct effect and still carry +0.156; the join is +0.3375 above proxy tuning on body outputs (0.256) on the same items and donors (a token-readout form, not the published byte-level form; the donor alone reads 0.631 against the join's 0.594) [corrected 2026-11-11, AUDIT e §8.4]

- **Run:** `results/bytegraft/join/diff_3m` (STATUS `exit=0`, S3 time 18:27:56Z; `out/metrics.json` `status` "ok"), `bytegraft_join`
  at `659f07276` (branch `research/bytegraft-tails`; `out/args.json` `PG_GIT_SHA` `659f0727655b`), instance `<instance>`,
  g6e.2xlarge, launched 17:52:22Z (EC2, read-only), first heartbeat 17:53:01Z; decodes 1,324.8 s (`progress.seconds`), GPU peak
  23.05 GB. Plan and rule: `GRAFT.md` first steps, 23 (rule (m), the `P2` addition, the fourth line, the two reading points settled
  before launch); Run H was not run then. Reviewed before launch (`review_2026-11-11_diff3m.md`: 0 W, 0 C, 5 N). The three joins
  (`deciding`, `deciding_early`, `deciding_late`) are `join_4`'s stored rows; known answer 40 re-decodes 20 items of each and
  reproduces all 20 texts. Recomputation: `results/diff_3/recompute.json` (diff_3m's rows and `join_4`'s).
- **Known answers passed** (`steps.summary.gates`, 16): `main`'s 1 to 6; 13, `deciding_late` and `deciding_early` together equal
  `deciding`; 14, the empty row set gives `main`'s tokens; 24, `main` alone reproduces `join_3`'s stored texts; 40, each join
  reproduces `join_4`'s stored texts; 41, PD, PD early and PD late with `main`'s own writes as the donor's give `main` alone's tokens;
  44, P2 with S as both donors gives `main` alone's tokens. 41 and 44 add exact zeros and check plumbing only (review N3).
- **Conditions** (host `main`, the 200 word-task items): `main` alone; the replace-form join at the deciding rows (F's attention
  writes at the last prompt row and every generated row; `join_4`'s `deciding`) and its parts at layers 0 to 11 and 12 to 15; their
  direct-write controls PD, PD early, PD late: the same landed changes, Σ over the layer set of n(F's write) − n(`main`'s own write) at
  the deciding rows, `main`'s own write taken from its unmodified forward, added once to the final norm's input with nothing written
  inside the body; P2, `main`'s logits plus `main`'s final norm and unembedding applied to F's last body state minus S's at the
  deciding rows. "The body" in (m) covers every change `main`'s layers make because of the writes, at carried rows every head's
  output is F's, so attention takes part only at uncarried deciding rows and, for the early and late parts, at the layers left
  untouched [corrected 2026-11-11, AUDIT e §8.13].
- **Whole items right** (`steps.results.diff3.accuracy`, `counts`; right counts from `recompute.json` `conditions`; edit tasks del,
  ins, sub, swap, 40 each; strict equals lenient for every condition):

| condition | edit tasks, right per task | edit mean | − `main` alone (interval), fixed and broken on the edit tasks | stopped at end of text (of 200) |
|---|---|---|---|---|
| `main` alone | 1, 5, 10, 0 | 0.100 | | 0 |
| join at the deciding rows | 23, 28, 29, 15 | 0.594 | +0.494 (0.406 to 0.575), 81 and 2 | 0 |
| its direct-write control PD | 13, 9, 14, 6 | 0.263 | +0.1625 (0.081 to 0.244), 36 and 10 | 38 |
| join at layers 0 to 11 | 8, 15, 15, 2 | 0.250 | +0.150 (0.0875 to 0.2125), 29 and 5 | 0 |
| its control PD early | 1, 7, 7, 0 | 0.094 | −0.006 (−0.044 to +0.031), 3 and 4 | 0 |
| join at layers 12 to 15 | 17, 22, 24, 12 | 0.469 | +0.369 (0.2875 to 0.456), 61 and 2 | 0 |
| its control PD late | 15, 7, 19, 4 | 0.281 | +0.181 (0.100 to 0.2625), 38 and 9 | 32 |
| P2 (proxy tuning on body outputs) | 9, 13, 14, 5 | 0.256 | +0.156 (0.0875 to 0.225), 32 and 7 | 62 |

  Join − control (`steps.results.diff3.differences`): all layers +0.331 (0.250 to 0.4125), 57 items right only with the join and 4
  only with PD; layers 0 to 11 +0.156 (0.0875 to 0.225), 31 and 6; layers 12 to 15 +0.1875 (0.106 to 0.275), 40 and 10. Join − P2
  +0.3375 (0.2625 to 0.4125), 58 and 4. Texts equal between the join and PD on 54 of 200 items, between `deciding_early` and PD early
  on 80 (`steps.results.diff3.sentences.<join>.texts_equal_join_control`).
- **End of text.** PD, PD late and P2 end the text before any closing quote on 38, 32 and 62 of 200 items, all of them edit items;
  the joins on none. Every one of those texts is wrong by the strict rule and also by the lenient rule (`recompute.json`
  `of_those_right_lenient` 0 for each), so the strict and lenient means are equal, and the end-of-text stops do not account for any
  of the gap to the join: a text that stops early here is not a right answer missing its quote.
- **Printed readings (frozen;** `steps.summary.sentences`**):** join at the deciding rows "the body takes part; share 0.329 (0.171 to
  0.481)"; layers 0 to 11 "the body takes part; share −0.042 (−0.353 to 0.211)" (−0.318 to 0.176); layers 12 to 15 "the body takes
  part; share 0.492 (0.292 to 0.689)" (0.303 to 0.683), both with independent task draws (AUDIT h2); P2 "the join on main is above
  proxy tuning on body outputs". The share is (control − alone) / (join − alone), an
  interval of per-draw ratios (review N1).
- **Samples** (`recompute.json` `samples`; no probabilities stored). `published:del_word:009539` (delete " they " in " And they lived
  happily ever after. "; gold ` And lived happily ever after.`): `main` alone ` And they lived happily ever after` (wrong); the join `
  And lived happily ever after. "` (right); PD ` And lived. lived. lived. lived.` (wrong); P2 ` And lived. "` and end of text (wrong).
  `published:del_word:009948` (delete " to " in " The brave little girl smiled to herself. "): `main` alone and PD early ` The brave
  little girl smiled to herself` (wrong); the join at layers 0 to 11 ` The brave little girl smiled herself. "` (right).
- **Readings (the coordinator's; one run, 160 edit items):**
  1. On shared coordinates the join is more than an output-level effect. A direct write of the same landed changes gives about a third
     of the gain (share 0.329, 0.171 to 0.481; 0.182 to 0.468 with independent task draws, AUDIT h2); the rest, +0.331, comes from
     `main`'s own layers acting on the writes. The writes at
     layers 0 to 11 have no direct effect (PD early −0.006 against `main` alone) and still carry +0.156 through the later layers.
  2. The join is above `P2`, a token readout of the donors' body states through `main`'s final norm and unembedding (0.594 against
     0.256); `P2` is not proxy tuning's published byte-level form (2506.14123 §4.4), which was not run. The donor alone reads 0.631
     (join − F −0.0375, −0.106 to +0.031; the join's answer equals F's on 104 of 160 edit items): the join brings `main` to the
     donor's level and is not shown above it [corrected 2026-11-11, AUDIT e §8.3]. Set beside it: proxy tuning's own tables use
     token-model experts and report no activation join (2401.08565, 2506.14123 Table 8); CMAP (2402.14811 §6) reaches the
     fine-tune's level by patching heads on a one-token answer and, as far as it was read (pass 6, §6 only), reports no comparison
     with a logit-level combination and no direct-path split. Not found in the passes; never "first".
  3. Five output-level levels lie between 0.256 and 0.294 (PD and P2 on `main`; `dF_U`, P1H and P2 at H); others of the same family
     read 0.200 (10% host) and 0.225 (`dF_proc`). As gains over each host alone, from different baselines (0.025 to 0.100) and
     different forms, they read +0.150 to +0.225 with intervals of about ±0.07, so equal sizes are not shown
     (`results/audit_2026-11-11e/audit_diff23.json` `output_level_side_by_side`) [corrected 2026-11-11, AUDIT e §8.11]. What does
     not cross into a separately trained network is the part that needs the host's layers.
  4. What follows: `GRAFT.md` first steps, 24 (`diff_3` Run H, run now as the first job of a new line).
- **Limits:** one run; the joins' rows come from `join_4` (re-decoded on 20 items each); the direct path is defined with `main`'s
  own writes from its unmodified forward; PD, PD late and P2 often end the text early (38, 32, 62 of 200), which both rules score
  wrong and which, here, is not a hidden right answer; 160 items; the share's interval is a percentile of ratios and is wide where
  the denominator is small (layers 0 to 11). Where the join is right and PD wrong (57 edit items), PD stops early on 15, loops on 2
  and writes another answer on 40 (18 shorter than the gold, 16 longer, 23 of its length; 19 begin like the join's answer); counting
  the 15 early stops as right would leave 42 against 4 (`results/audit_2026-11-11e/audit_diff23.json` `failure_kinds`,
  `control_lengths`) [corrected 2026-11-11, AUDIT e §8.14].

<!-- JOURNAL.md lines 3417 to 3462 -->
## 2026-11-11, the fifth independent audit (`diff_2` runs A and B, `diff_3` Run M): every number recomputes from the stored rows and every printed sentence follows from a rule frozen before its launch; "the join on `main` is above the published method" does not count anywhere it is written: the proxy tuning arm (`P2`) is a token-readout form, and the donor alone reads 101 of 160 against the join's 95

- **Who and how:** Claude Opus 5.5 (the commit's attribution), a different model from the coordinator. No model run. Every number was
  recomputed from per-item rows (local copies of S3 `results/bytegraft/join/{diff_2a,diff_2b,diff_3m}/out/`, each file equal to its
  ETag, plus the stored rows they read: `diff_1`, `map_1`, `join_3`, `join_4`); texts re-scored from text and gold; own bootstraps,
  10,000 draws within task, seed 20261111; code read at `988d97f76` and `659f07276`. Report `AUDIT_2026-11-11e.md`; script and output
  `results/audit_2026-11-11e/audit_diff23.{py,json}`; commit `980e6f5ea`, merged `73591d14f`. `diff_3h` was not read. The 14
  corrections of its §8 are applied in place above, in `GRAFT.md`, in `HANDOFF.md` and in `meta/META.md`, each tagged `[corrected
  2026-11-11, AUDIT e §8.<n>]`; before each was applied its number was read from the evidence it cites (all 14 matched). Not checked
  by the audit: EC2 launch times; the papers' full texts except 2506.14123 §4.3, §4.4 and B.3; whether `main`'s next-byte distribution
  is close to S's.
- **What held:** no stored strict flag differs from the re-scored one; every row of both entries' tables and every listed difference
  recomputes; every printed sentence came from a rule committed before its launch (its §5 table: rule and code commits before each
  launch; the step 22 reading note came after `diff_2`'s launch, as it says, and changed no threshold).
- **WRONG** (a sentence must change): the eight places that say the join on `main` is above the published method or more than proxy
  tuning (§8.1 to §8.8). What was measured: the join brings `main` to the donor's level (0.594 against F alone's 0.631; join − F
  −0.0375, −0.106 to +0.031; the join's answer equals F's on 104 of 160 edit items), and `P2` is `main`'s token head applied to the byte
  models' body states, not the published byte-level form (2506.14123 §4.4), which was not run. The split that holds is the direct-write
  one: at carried rows every head's output is F's, so the about two thirds of the gain that the direct write does not give come from
  `main`'s MLP blocks reading F's attention outputs (§8.1, §8.12, §8.13).
- **WEAKER:** "is proxy tuning" for `diff_2`'s output-level part (§8.9: the part is shown by P1H; a token-readout form reaches the same
  accuracy; the published form was not run); at H the direct write and `dF_U` agree item by item on 58 of 160 edit answers, so "the body
  adds no accuracy that is shown", not "takes no part" (§8.10); "the output-level part has the same size everywhere" is removed as a
  finding (§8.11: five levels between 0.256 and 0.294, others at 0.200 and 0.225, gains from different baselines with intervals of about
  ±0.07); the coordinator's own correction above (m) went too far once ("host + F − S is about F" assumes `main` and S agree at the
  output, which was not measured; §8.12); where the join is right and PD wrong, PD stops early on 15 of 57 items, so termination
  explains a part of that cell, not the gap (§8.14).
- **Readings made after the numbers** (its §5): `diff_1`'s `U` (chosen from five maps, then held on fresh items); `diff_2` reading 2's
  "is proxy tuning"; `diff_3` reading 2's "above the published output-level method"; reading 3's "same size everywhere"; the
  re-ordering of "State of the evidence" into published and not; G4's distance quantity. Across the three runs, 38 condition reads and
  21 frozen sentences.
- **Its advice (§7; advice on plans, not an audit result).** On rule (h) for Run H: quote (arm − its direct-write control) with its
  interval for every arm, also where the arm's sentence is "does not" (on `main` the early writes acted only through the body);
  `dF_proc`
  at layers 0 to 11 has no other-item control; a "does not" from a rotation that fits no better than the mean row says nothing about H's
  body; quote (control − H alone) beside any "the body takes part". The coordinator's reading note under step 24 takes these up, written
  while Run H was on a GPU and before its numbers were opened. On the planned arm `PT` (proxy tuning with the byte experts): it
  would be a
  token-candidate approximation of the published method, not the method; it needs five known answers, the last an expected value on
  `main` set before unblinding; its name should say "approximation" unless checked against an exact byte-level implementation. `PT` was
  not built: the coordinator's decision note under step 24 (`NOTES_join.md` on the tails branch, "PT, not built": the exact byte
  probability sums over 2^(n−1) boundary paths, and the single-parse approximation costs about 400 GPU-minutes at 32 candidates).
- **What follows:** (a) every sentence that called the join above proxy tuning now states what was measured; (b) one rule added to
  `GRAFT.md` "How we size work" and one line to `meta/META.md`'s research entry: a comparison sentence names the method's published form
  and the donor-alone number beside it; (c) the join line closes with Run H; the next line is step 25 (`chain_1`, the character edits).

<!-- JOURNAL.md lines 3548 to 3599 -->
## 2026-11-11, `select_1`: with the evidence table and 60 scored sets each, two agents chose 16 heads that read 0.394 and 0.363 on the 160 test edit items, level with the gradient ranking (0.356) and above random search and a ridge-surrogate sampler, which had no table, at the same number of scored sets (0.144, 0.138); all 256 heads read 0.594 [AUDIT f §8.4, §8.5]

- **Runs:** code `a50067c6d` on the tails branch (`out/args.json` `PG_GIT_SHA` `a50067c6d84b` in all three runs). Plan and rule:
  `GRAFT.md` step 27 (`dc1e3fb50`, before the launch). Review `review_2026-11-11_select1.md` (of `6f20cf554`; W1, W2, C1 and C2 fixed
  in `a50067c6d`). The scoring service `results/bytegraft/bench/select_1`: `<instance>`, g6e.2xlarge, launched 21:37:36Z
  (EC2), first heartbeat 21:38:14Z, references written 22:01:02Z, first request 22:01:51Z, `stop.json` 22:19:37Z, STATUS `exit=0`
  22:19:43Z (S3 times); requests and responses in `results/bytegraft/bench/select_1_requests/`. The final read in two parts,
  `results/bytegraft/select/select_1_final_a` and `select_1_final_b`: `<instance>` and `<instance>`, g6e.4xlarge,
  launched 22:25:18Z and 22:27:08Z, STATUS `exit=0` at 22:53:41Z and 22:50:14Z; the final sets
  `results/bytegraft/select/select_1_final_sets.json`; the parts combined on the laptop (`results/select_1/combined_metrics.json`).
  The agents' rounds and the scorer's responses, the baselines and the final sets are copied to `results/select_1/`. Recomputation:
  `results/select_1/recompute.json`.
- **Service** (`bench/select_1/out/metrics.json`): 80 fit items, 20 per edit task (79, 75, 82, 78 of 100 candidates qualified); three
  gates true (the same set twice gives the same value; all 256 heads read as the deciding join; no heads score exactly 0). On the fit
  items (mean gain in gold log-odds) all 256 heads score 3.904 and the best single head, (12, 6), 0.562 (`references.json`); the top
  16 by gradient attribution and the top 16 by single-head score are the same 16 heads. Scored sets (`serving.used`): 60 each for
  agent_a, agent_b, random and surrogate, and 258 reference sets scored in process. No `refused.jsonl` exists (the service writes it
  only when it refuses a request), and none of the 240 answered sets in the responses was refused.
- **Final sets** (`select_1_final_sets.json`; fit score): agent_a 1.960 (its round 3, set 20, its best), agent_b 1.798 (round 3, set
  14, its best), surrogate 1.218, random 0.782, so BB is surrogate. Best per round: agent_a 1.264, 1.566, 1.960; agent_b 1.450, 1.674,
  1.798.
- **Test** (160 published edit items, free-running, strict equals lenient; right per task del, ins, sub, swap; `combined_metrics.json`
  `steps.results.select.strict.accuracy`): none 16 (0.100, stored rows); random 22 (2, 8, 11, 1; 0.138); surrogate 23 (1, 11, 10, 1;
  0.144); direct-effect top 16 35 (6, 12, 14, 3; 0.219); gradient top 16 57 (7, 23, 20, 7; 0.356), its texts equal to the single-head
  top 16's on all 160; agent_b 58 (6, 19, 24, 9; 0.363); agent_a 63 (9, 20, 26, 8; 0.394); all 256 heads 95 (0.594, stored rows). A −
  BB +0.234 (0.175 to 0.294); A − gradient +0.022 (−0.031 to +0.078); A − direct +0.159 (0.100 to 0.222). The final job's five gates
  are true in both parts (all 256 heads reproduce `join_4`'s `deciding` texts; no heads reproduce `main` alone; only the registered
  requesters in the log; none above 60; each final set among its method's own scored sets).
- **Printed (frozen;** `steps.summary.sentences`**):** "agents are above black-box search at equal evaluations"; against the gradient
  ranking "level"; "agents are above the direct-effect ranking". The black-box arms were random search and a ridge-surrogate sampler
  with no prior over heads (best fits 0.782 and 1.218), not CMA-ES or TPE; the agents also had the evidence table, computed on the
  same 80 fit items. One line of that table with no scored set, the direct-effect top 16, reads 0.219 against the surrogate's 0.144,
  and its attention-shift top 16 scored 1.450 on the fit items, above the surrogate's best of 60 [AUDIT f §8.1, §8.5]. On "level": 21
  items favour the agents and 16 the gradient set; a difference of up to 0.08 for the agents or 0.03 against is not excluded; the
  gradient top 16 needs no agent and no scored set and shares 6 and 5 heads with the agents' sets [AUDIT f §8.2]. The direct-effect
  column's top head scores −0.009 alone; the attention-shift ranking, which scored higher on the fit items, was not decoded [AUDIT f
  §8.3].
- **What the agents could read** (the coordinator's check of their tool records, repeated in AUDIT f §1): agent_a 1 file
  read and 14 shell commands, agent_b 2 and 14; every command works on the evidence folder or the agent's own work folder; none
  touches the network, the bucket, the reference scores, the rankings, the baselines or the other agent's folder.
- **Reading:** agents given the evidence table and 60 scored sets chose sets that read 0.394 and 0.363 on items no method saw, level
  with the gradient ranking (0.356); random search and a ridge-surrogate sampler, which had no table, read 0.138 and 0.144 at the same
  number of scored sets; all 256 heads read 0.594. The table alone gives a set that scores 1.450 on the fit items, above the
  surrogate's best of 60, and its direct-effect ranking reads 0.219 on the test items. Whether the language model adds anything beyond
  the table and a fitted additive model is not tested: both agents fitted additive ridge models on their own scores [AUDIT f §8.4]. In
  their relayed accounts both agents say the table's direct-effect column ranked heads badly and the change in attention between the
  two models ranked them well.
- **Limits:** two agents, one task, one pair of models, one run. The search arms were random search and a ridge-surrogate sampler with
  no table, not the best possible search [AUDIT f §8.5]. No fixed rule on the attention columns was decoded on the test items. The
  agents tie the gradient ranking, so nothing here says an agent beats the conventional method where gradients are available. The
  agents' fit scores (1.960, 1.798) have no counterpart for the gradient set, which was not scored on the fit items.

<!-- JOURNAL.md lines 3600 to 3614 -->
## 2026-11-11, the sixth independent audit (`select_1`): the printed sentences hold as printed, with no leak and equal budgets; the comparison is agents holding the evidence table against search with none; 6 corrections; its advice is a table-only scripted search at equal evaluations

- **What held** (`AUDIT_2026-11-11f.md` §1 to §5; `results/audit_2026-11-11f/audit_select.json`): the agents touched only the two
  evidence files and their own folders (15 and 16 tool calls; no network, bucket, git or other folder); each method has 60 distinct
  scored sets and each final set is its own best of 60; every gate passes; the three sentences follow from the rule frozen at
  `dc1e3fb50` before the service started.
- **Corrections** (§8, applied to the `select_1` entry, GRAFT step 27, state item (n), G3 and HANDOFF §0): 1, the search arms had no
  table, and the table alone gives a set scoring 1.450 on the fit items; 2, "level" leaves +0.08 or −0.03 open; 3, the direct-effect
  column's top head scores −0.009 alone and the attention-shift ranking was not decoded (its clause "the table's weakest one-line
  ranking" is not applied: `rules` has the write-difference-norm top 16 at 0.608 on the fit items, below the direct effect's 1.264);
  4, "agents given the evidence table and 60 scored sets", with what the language model adds untested; 5, "random search and a
  ridge-surrogate sampler" for "black-box search"; 6, step 27's outcome names the table-only search as needed.
- **Advice** (§7): one more arm at 60 scored sets with the same table and no language model, plus CMA-ES or TPE without the table,
  read beside both agents and the gradient top 16 on `pair_1`'s 80 fresh items. The table-only arm is step 28 (`select_2`).

<!-- JOURNAL.md lines 3615 to 3657 -->
## 2026-11-11 to 12, `select_2`: a scripted search holding the same evidence table, with 60 scored sets and no language model, matches the agents on the 160 test items (A − S +0.003) and on 80 fresh edit items (−0.031); the gradient ranking matches them too; "agents add something beyond the table" is not printed

- **Runs:** code `3593dde11` on the tails branch (`out/args.json` `PG_GIT_SHA` `3593dde1106e` in both). Plan and rule: `GRAFT.md` step
  28 (`41af9fe68`, 23:10:14Z, before the launch). Review `review_2026-11-11_select2.md` (0 W, 1 C, 4 N). The scoring service
  `results/bytegraft/bench/select_2`, started from `select_1`'s files: `<instance>`, g6e.4xlarge, launched 23:35:19Z (EC2),
  first heartbeat 23:36:00Z, first request 23:46:22Z, `stop.json` 23:53:28Z, STATUS `exit=0` 23:53:34Z (S3 times); requests under
  `results/bytegraft/bench/select_2_requests/`. Final sets `results/bytegraft/select/select_2_final_sets.json`. The final read
  `results/bytegraft/select/select_2_final`: `<instance>`, g6e.2xlarge, launched 23:53:34Z, first heartbeat 23:54:11Z, STATUS
  `exit=0` 00:26:19Z on 2026-11-12. The scripts' output is copied to `results/select_2/scripts.json` (its sets and scores equal the
  service's log in order). Recomputation: `results/select_2/recompute.json`.
- **Gates:** the service's 1 to 3 and 6 to 8 true (`fit_items.json` and `evidence.csv` byte-equal to `select_1`'s; ten reference sets
  scored again equal `select_1`'s stored scores); the final read's 7 true (3 to 5 on the log; 9, the agents' and the gradient sets are
  `select_1`'s; 10 and 11, agent_a's and the gradient set's stored test texts reproduced on 20 items each; 12, `main` alone reproduces
  `pair_1`'s stored texts on 20 fresh items). Each script used 60 distinct scored sets; reference 10.
- **agent_b's stored rows** (no gate re-decodes them; review N1): A on the test items uses `select_1_final_a`'s `decodes.jsonl`, the
  path in `out/args.json`, whose S3 ETag equals the copy read for the `select_1` entry. From those rows agent_b's right counts per
  task (6, 19, 24, 9) equal the job's, and the recomputed A − S equals the job's mean to 1e-12.
- **Fit scores of the final sets** (60 scored sets each): `script_direct` 1.689 (its 51st scored set), `script_columns` 1.804 (its
  30th); from `select_1`: agent_a 1.960, agent_b 1.798. S is `script_columns`.
- **Test** (160 published edit items, free-running, strict equals lenient; `steps.results.select2.strict.test`): none 16;
  `script_direct` 49 (0.306); gradient top 16 57 (0.356); agent_b 58 (0.363); `script_columns` 60 (0.375; 7, 20, 21, 12); agent_a 63
  (0.394); all 256 heads 95. A − S +0.003 (−0.059 to +0.066); 23 items favour the agents' mean, 20 the script.
- **Fresh** (`pair_1`'s 80 edit items; `steps.results.select2.strict.fresh`): none 7 (0.0875); `script_direct` 22 (0.275); agent_b 24
  (0.300); `script_columns` 30 (0.375); agent_a 31 (0.3875); gradient top 16 31 (0.3875). A − S −0.031 (−0.125 to +0.0625); A −
  gradient −0.044 (−0.1125 to +0.0375) (−0.106 to +0.025 with independent task draws; "level" in 50 of 50 seeds; AUDIT h2).
- **Printed (frozen;** `steps.summary.sentences`**):** test and fresh both "a scripted search with the same table matches the agents";
  "agents add something beyond the table" is not printed; against the gradient set on the fresh items "level". Heads in common:
  `script_columns` with agent_a 7, agent_b 9, the gradient set 8; `script_direct` 7, 5, 6.
- **What was known when step 28 was written** (review C1): `select_1`'s results, the agents' chosen heads and scored sets among them,
  were in hand. It favours the script on both item sets, through its design: its round-1 menu holds agent_b's best round-1 set (the
  summed attention change, 1.450 in `select_1`) and the agents' whole-layer probes, and its later rounds are the agents' procedure.
  The fresh items guard only against hindsight from the test items. The final set has no head that comes only from agent_b's set;
  whether the script reaches 1.80 without it was not run [AUDIT g §8.1]. So the comparison is agents against a fixed script of their
  own kind of method, written by the coordinator after seeing what the agents did.
- **Reading:** a fixed script holding the same table, with the same number of scored sets and no language model, reads the same as the
  agents on both item sets, and so does the gradient ranking. By step 28's rule no part of the advantage reported in `select_1` is
  shown to come from the language model: a fixed script with the table and a fitted additive model reads the same (the agents up to
  0.066 above on the test items and 0.056 above on the fresh items are not excluded) [AUDIT g §8.2]. What the agents did do is reach
  that level from the table without the procedure being written for them, and without gradients. No accuracy advantage of an agent
  over a script or over the gradient ranking is shown in this study.
- **Limits:** two agents, one task, one model pair, one run each; 80 fresh items; the script written with hindsight; the agents'
  tokens and time not recorded.

<!-- JOURNAL.md lines 3658 to 3736 -->
## 2026-11-12, `select_3`: greedy forward selection with 1,048 scored sets chooses 16 heads that read 75 of 160 test items and 38 of 80 fresh items, above the agents' mean on both (+0.091, +0.131): the earlier tie was not a ceiling for 16 heads; a script without the attention-change rankings printed "mixed" from a bootstrap whose ins_word and sub_word draws coincide; with independent task draws the agents are narrowly above it (+0.059, +0.081) [AUDIT h §8.2]

- **Runs:** plan and rule `GRAFT.md` step 29 (`3a05a5f03`, 00:47:33Z) with its two amendments before launch (`7d4bc58ee`, 01:31:13Z;
  `630f732ab`, 01:35:56Z). Review `review_2026-11-12_select3.md` (first look: W1, C1, C2; second look: one C, two N), copied from
  `research/bytegraft-tails` at `3ba7f8f93`. The scoring service `results/bytegraft/bench/select_3`, started from `select_1`'s files,
  code `3e006e5c5` (`out/args.json` `PG_GIT_SHA` `3e006e5c56ca`): `<instance>`, g6e.2xlarge, launched 02:19:32Z (EC2), first
  heartbeat 02:20:20Z, 19 requests from 02:31:18Z, `stop.json` 03:30:52Z, STATUS `exit=0` 03:30:59Z (S3 times). The final read
  `results/bytegraft/select/select_3_final`, code `3ba7f8f93` (`3ba7f8f93f2c`): `<instance>`, g6e.2xlarge, launched
  03:31:12Z, first heartbeat 03:31:51Z, STATUS `exit=0` 03:55:20Z. The client's output and the final sets are copied to
  `results/select_3/` (`select3.json`: its sets and scores equal the service's log in order). Recomputation:
  `results/select_3/recompute.json`; its intervals use the job's method and seed and equal the job's to 1e-12.
- **Gates:** the service's 1 to 3 and 6 to 8 true (fit items and evidence table byte-equal to `select_1`'s; ten reference sets scored
  again equal); the final read's 7 true (3, 4: only greedy, script_raw and reference in the log, greedy's 1,048 rows match its pool
  and its step-1 heads are that pool, script_raw within 60; 14: greedy's step 1 is (12, 6) with its stored score; 15: greedy's final
  set is its best prefix; 16: script_raw's final set is its own, logged fit score; 10: agent_b's stored test texts reproduced on 20
  items; 12: script_columns' stored fresh texts reproduced on 20 items).
- **Budgets are unequal.** greedy used 1,048 scored sets (73, 72, … 58 per step), script_raw 60 (all distinct), every arm of
  `select_1` and `select_2` 60. Greedy is a reference for room, not an equal-budget comparison of methods: with 60 scored sets it has
  not finished its first step (73).
- **Greedy's path** (`steps.checks.greedy_path`; head added, fit score, scored sets so far): (12, 6) 0.562, 73; (12, 8) 0.918, 145;
  (12, 3) 1.152, 216; (11, 8) 1.295, 286; (12, 4) 1.412, 355; (14, 0) 1.511, 423; (15, 0) 1.609, 490; (12, 11) 1.693, 556; (13, 9)
  1.767, 621; (12, 1) 1.842, 685; (13, 2) 1.910, 748; (14, 7) 1.980, 810; (15, 8) 2.044, 871; (9, 2) 2.107, 931; (12, 15) 2.164, 990;
  (13, 13) 2.218, 1,048. The kept score rose at every step (`greedy_falls` empty); the chosen prefix is all 16 steps (fit 2.218). It
  passes agent_b's 1.798 and script_columns' 1.804 at step 10 (1.842, 685 sets) and agent_a's 1.960 at step 12 (1.980, 810 sets).
  script_raw's final set is its 45th scored set and its best, fit 1.725.
- **Two heads from the widened pool.** Greedy took two of the nine heads the second amendment added: (13, 9) at step 9 and (15, 8) at
  step 13. Alone (`bench/select_1/out/references.json` `singles`) (13, 9) ranks 193rd of 256 (−0.004) and is in both agents' sets;
  (15, 8) ranks 218th (−0.009) and is in both `select_2` scripts' sets and the direct-effect top 16. Neither is in the original
  64-head pool.
- **Test** (160 published edit items; strict; right per task del, ins, sub, swap): greedy 75 (10, 22, 28, 15; 0.469); script_raw 51
  (4, 15, 25, 7; 0.319); from the stored rows agent_a 63, script_columns 60, agent_b 58, gradient top 16 57, script_direct 49, none
  16, all 256 heads 95. greedy − A +0.091 (0.034 to 0.147); A − script_raw +0.059 (lower end 1.7e-18, upper 0.119). Lenient: greedy −
  A +0.097 (0.041 to 0.153); A − script_raw the same as strict.
- **Fresh** (`pair_1`'s 80 edit items; strict): greedy 38 (9, 12, 11, 6; 0.475); script_raw 21 (3, 6, 12, 0; 0.2625); agent_a 31,
  gradient top 16 31, script_columns 30, agent_b 24, script_direct 22, none 7. greedy − A +0.131 (0.050 to 0.2125); A − script_raw
  +0.081 (0.000 to 0.175). Lenient equals strict on both differences.
- **Printed (frozen;** `steps.summary.sentences`**):** room "there was room above the agents"; raw script "mixed". Both lower ends are
  0 in exact arithmetic (the test end prints as 1.7e-18 and was read as above 0, hence "mixed"). The job's bootstrap resamples
  ins_word and sub_word at the same positions: `bytegraft_join.task_draws` seeds each task by the byte sum of its name, 869 for both.
  With independent draws per task the lower ends are 1/320 to 1/160 at 10,000 draws, and the frozen rule prints "the agents are above
  a script without the attention-change rankings" (44 of 50 seeds at 2,000 draws with numpy's independent per-task seeds, the rest
  "mixed"; "matches" in none; AUDIT h2). A − `script_raw` is +0.059 (0.006 to 0.116) and +0.081 (0.006 to 0.163). agent_a carries it
  (+0.075 and +0.125, both above 0); agent_b's intervals hold 0. `script_columns`, which has those rankings, is +0.056 and +0.1125
  above `script_raw` (AUDIT h §2) [AUDIT h §8.1, AUDIT h2 §8.1].
- **Fit score orders the unseen reads.** Over the nine 16-head sets with both numbers (greedy 2.218, agent_a 1.960, script_columns
  1.804, agent_b 1.798, script_raw 1.725, script_direct 1.689, direct-effect top 16 1.264, surrogate 1.218, random 0.782) test items
  right are 75, 63, 60, 58, 51, 49, 35, 23, 22: the same order, Spearman 1.0. Over the six with fresh reads: 38, 31, 30, 24, 21, 22,
  Spearman 0.943. A rank correlation cannot show that there is no overfitting. On the test items greedy reads 0.469 where a line
  through the other eight sets puts 0.450; on the fresh items it reads 0.475 where a line through the other five puts 0.518 (3.5 of 80
  items short, extrapolated from fit scores of 1.69 to 1.96). No overfitting is visible on the test items; on the fresh items it is
  not excluded [AUDIT h §8.6].
- **Overlaps and items.** Heads in common with greedy's set: agent_a 8, agent_b 9, gradient top 16 9, script_columns 9, script_direct
  8, script_raw 7, direct-effect top 16 8, surrogate 4, random 2. At least one of the five earlier sets (agents, gradient, two
  `select_2` scripts) solves 85 of 160 test items and 41 of 80 fresh items; greedy solves 5 and 5 that none of them does.
- **Exploratory differences** (strict, the job's method; not in the frozen rule): test greedy − gradient +0.1125 (0.050 to 0.175),
  greedy − script_columns +0.094 (0.031 to 0.156), greedy − agent_a +0.075 (0.025 to 0.131), gradient − script_raw +0.0375 (−0.019 to
  +0.094), script_columns − script_raw +0.056 (−0.006 to +0.119); fresh +0.0875 (0.012 to 0.175), +0.100 (0.000 to 0.1875), +0.0875
  (0.000 to 0.175), +0.125 (0.050 to 0.200), +0.1125 (0.0375 to 0.1875).
- **Not measured:** the gradient ranking's set has no fit score (it was never sent to the service). All 256 heads (95 of 160) and none
  (16) stay the outer references.
- **Reading:** the tie of `select_1` and `select_2` (agents, a script and the gradient ranking at 0.36 to 0.39) was not a ceiling for
  16 heads: a plain greedy search reaches 0.47 on both unseen item sets. The agents and the table-holding script (60 scored sets each)
  and the gradient ranking (no scored sets) are together. Greedy, with 1,048 scored sets and a pool that holds the agents' and
  scripts' heads, is above all three on the 160 test items. On the 80 fresh items it is above the agents' mean, while its intervals
  against the table script and the gradient set reach 0. The agents are narrowly above a script without the attention-change rankings,
  and a script with them matches the agents. No accuracy of the language model beyond the table is shown [AUDIT h §8.4]. What the
  agents did show: in 60 scored sets they reached fit scores (agent_b 1.798, agent_a 1.960) that greedy passes after 685 and 810
  scored sets. Greedy's pool holds nine heads from the agents' and scripts' sets, and its prefixes at those steps contain one of them,
  (13, 9); at step 9 the next candidate, (12, 1), scored 0.0007 less. Both agents chose (13, 9), which is useless alone by fit score
  (193rd of 256) but 7th of 256 in the table's operand attention-change column; `script_columns` had it among its 54 candidates and
  did not keep it. A script with the same table reaches agent_b's 1.80 in 60 sets, not agent_a's 1.96 (best 1.804). On unseen items
  agent_a's lead over that script is 3 of 160 and 1 of 80, inside the intervals. The fit-score point is about the table and is not
  shown to be about the language model [AUDIT h §8.5].
- **Limits:** one task family (the four word-edit tasks), one host (`main`, shared coordinates), 16 heads, one greedy run, 80 fit
  items; the agents ran once each; "room" is shown against a search with 17 times the scored sets. The other intervals in this entry
  are the job's: `task_draws` gives ins_word and sub_word identical position draws (seeds `[20261105, 869]` for both), as in every
  interval from `task_draws` since `join_1` (`4c04a59da`) where the two tasks hold the same number of items. With independent draws, A
  − `script_raw` and the fresh greedy − gradient change side of 0; the room sentence does not (AUDIT h §2) [AUDIT h §8.3].

<!-- JOURNAL.md lines 3737 to 3747 -->
## 2026-11-12, the shared bootstrap drew ins_word and sub_word at the same positions (AUDIT h, AUDIT h2)

`bytegraft_join.task_draws` seeds each task's bootstrap by `[20261105, the byte sum of the task's name]`; ins_word and sub_word both
give 869 (ins_char and sub_char 839), so wherever the two tasks hold the same number of items they were resampled at identical
positions, in every interval from `task_draws` since `join_1` (`4c04a59da`; AUDIT h §8.3). AUDIT h2 reran the 17 jobs' interval code
from their stored rows: with the job's draws all 7,141 stored interval paths and 408 printed string paths reproduce exactly. It then
recomputed the 93 intervals the documents quote (57 rows) with independent draws per task: one row's frozen sentence changes
(`select_3`'s raw-script sentence, 2 intervals), 11 rows move (22 intervals), and 45 rows (69 intervals) are unchanged
(`AUDIT_2026-11-12h2.md` §1, `results/audit_2026-11-12h2/h2_table.json` `counts`, `rows`). The stored `metrics.json` files keep the
job's intervals; where the two differ, the documents now give both.

<!-- JOURNAL.md lines 3748 to 3772 -->
## 2026-11-12, `route_1`: on `main` the donor's attention weights alone, over the host's own values, give 77 of 160 and 38 of 80 (the join 95 and 42; the host alone 16 and 7)

Short entry, engineering stage (`GRAFT.md`, "How we work"): read as a go or no-go for one part of the build. Not audited.

- **Run:** `results/bytegraft/route/route_1` (STATUS `exit=0`; `out/metrics.json` `steps.results.route.all.strict`, copied to
  `results/route_1/metrics.json`), `bytegraft_route` at `d52840a29`, `<instance>`, g6e.2xlarge, launched 05:42:54Z,
  about 57 minutes. Plan `GRAFT.md` step 30; reviews `review_2026-11-12_route1.md` (two looks); literature pass 10.
- **Known answers, all seven true:** the host's weights and values through the new path equal the forward's own output (largest
  gap 1.2e-5) and the stored texts on 20 items; F's weights and values equal F's own output (3.6e-6) and the stored join's
  texts on 20 items; F's weights moved onto the host's rows sum to 1 (4e-7).
- **Right, strict** (160 test items; 80 fresh items; recounted from `out/decodes.jsonl`; `none` and the test `join` from stored
  rows): `join` (F's weights, F's values) 95, 42. `weights_only` (F's weights, the host's values) 77, 38. `values_only` (the
  host's weights, F's values) 37, 21. `none` 16, 7. `weights_other` (F's weights from another item) 0, 0.
- **Printed by the frozen rule:** re-routing "mixed" (above the host alone on both item sets; below the join on the test items,
  +0.1125, 0.050 to 0.181; on the fresh items +0.050, −0.050 to +0.150); "F's values alone give part of the join's gain".
- **One item:** `published:del_word:009539`: `weights_only` writes " And lived happily ever after." (right); `values_only`
  " And they lived happily ever after" (wrong); `weights_other` " They lived happily ever after." (wrong).
- **Reading for the build:** most of the join's gain is where F's heads attend, applied to what the host already holds; another
  item's weights give nothing. Attention weights are indexed by row, so they can be given to a separately trained host with no
  map between coordinate systems; what has to be found is which host head takes which F head's weights. The published prior
  (2604.08524 Table 1, for a steering vector) pointed to values.
- **Limits:** one host that shares coordinates with the donor; the control wrote at 0.78 of the deciding rows against 0.98 and
  moved 0.19 of its key weight by the last-byte rule against 0.003 (`steps.results.control_matched_on`, `moved_by_rule`), so it
  is a rough control; 85 of 160 test items have a row matched by the rule.

<!-- JOURNAL.md lines 3773 to 3806 -->
## 2026-11-12, `wire`: the donor's attention weights given to heads of the separately trained host H; six pairs alone decode at 35 of 120, with the output-level part 49 of 120 (H alone 8, the output-level part alone 34)

Short entry, engineering stage (`GRAFT.md`, "How we work"; step 31). Not audited; nothing here has been read on the held-out
test or fresh items. Numbers are on dev items; the boards are the artifacts.

- **The service** (`NOTES_wire.md`): a candidate join is a JSON spec; parts `weights` (host head takes an F head's attention
  weights over its own values), `out`, `direct`, `rot`; requests `score`, `decode`, `match`, `screen`; one board per session at
  `results/bytegraft/bench/<session>/out/board.jsonl`. Sessions: `wire_1_main` (out of GPU memory at start), `wire_1b_main`
  (`6e961d3d3`), `wire_2_h` (`c6428257c`), `wire_2b_h` (`65388281e`; used its 10,000-spec cap), `wire_2c_h` (`65388281e`),
  `wire_2d_h` (`4857386c5`; idled out unused), `wire_2f_h` (`4857386c5`), `wire_2e_h` (`8aae4b314`), `wire_2g_h` (`780f2de15`).
  Known answers at every start: the empty spec is the host alone; on `main` `select_1`'s reference scores and `route_1`'s
  `w_only` texts; on H `diff_1`'s and `diff_3h`'s stored texts; a crossed pair against an independent recomputation.
- **On `main`** (`wire_1b_main`; 40 check items): F's weights on every head 0.45, on layers 12 to 15 only 0.45, on the 4, 8,
  16, 32 heads with the largest single scores 0.275, 0.35, 0.375, 0.475. Single heads: (12, 6) 0.653, (12, 8) 0.477, (12, 3)
  0.329 on the fit score; layers 0 to 7 together 0.126 of 2.409.
- **On H, single pairs** (`wire_2b_h`, `wire_2c_h`; 13,000 of 65,536 pairs scored on the first-departure score): host (10, 7)
  taking F (13, 12) +0.560, (12, 8) +0.555, (12, 6) +0.517; (12, 7) taking (13, 12) +0.502; (10, 4) taking (12, 6) +0.488. The
  same-numbered heads give 0 of 40.
- **On H, decoded** (strict; 120 select items, `wire_2f_h`): H alone 8; `direct` proc 33; `out` U 34; `out` U + `rot` 11 41;
  five pairs 29; six pairs 35; five pairs + `out` U 49; six pairs + `out` U 49. The six pairs: (10, 7)←(13, 12), (12, 7)←(13, 12),
  (10, 4)←(12, 6), (12, 0)←(13, 12), (12, 6)←(12, 8), (14, 2)←(13, 12) (host head ← F head). On the 40 check items: H alone 3,
  five pairs 12, five pairs + `out` U 20, `out` U 13, `out` U + `rot` 11 19. Half strength, mixtures of F heads and one distinct
  F head per receiver gave 7 to 12 of 40 for pairs alone: no better than the plain form.
- **The first-departure score is not the target on H.** Greedy on it reached 3.40 with 32 pairs; decoded on the 40 check
  items: 4 pairs 9, 5 pairs 12, 6 pairs 3, 8 pairs 1, 32 pairs 2. The sixth pair, (13, 5)←(8, 1), breaks decoding. The scorer
  now also reads the whole gold answer under teacher forcing (`seq`, `exact`; `8aae4b314`). On seven specs with known decoded
  accuracy the rank correlation with decoding is 0.107 for the first-departure score, 0.964 for `seq`, 0.893 for `exact`
  (`results/bytegraft/bench/wire_2e_h/out/metrics.json` `steps.seq_readout`).
- **Speed:** 2.2 s per scored spec at first; 0.09 s batched with the prefix cache; 0.26 s with the whole-answer score; a
  decoded item 1.8 s; a start on H 22 minutes, 15 to 17 with stored maps.
- **Reading for the build:** attention weights cross into a separately trained network with no map: six host heads given the
  donor's weights take H from 8 to 35 of 120, level with the output-level wiring, and the two together give 49. The published
  comparison for the head assignment (attention-map cosine, 2507.11953 §3.4) and the read on the held-out items are still owed.

<!-- JOURNAL.md lines 3807 to 3843 -->
## 2026-11-12, `wire`, the read on the held-out items: on H, 15 `weights` pairs alone 76 of 160 test and 44 of 80 fresh; with `out` U 98 and 50; H alone 12 and 6; the donor alone 101 of 160

Engineering stage; one read, taken once, of a wiring fixed beforehand. Its two controls are running; nobody else has read the
artifacts; decoded texts were not stored (the service is being changed to store them and the read will be repeated).

- **The wiring** (`results/wire/chosen_pairs_15.json`; host head ← F head): (10, 7)←(12, 6), (12, 0)←(12, 8), (12, 7)←(12, 6),
  (12, 6)←(12, 8), (13, 2)←(13, 12), (14, 2)←(13, 12), (10, 4)←(12, 3), (10, 15)←(12, 8), (13, 5)←(10, 10), (12, 12)←(12, 11),
  (10, 8)←(11, 2), (11, 12)←(12, 11), (11, 8)←(10, 10), (13, 15)←(12, 6), (14, 10)←(13, 13). Each host head uses that F head's
  attention weights at the deciding rows over its own values and o_proj. No map, no training.
- **How it was chosen:** greedy forward selection by the whole-answer score `seq` on the 80 fit items of H, over the 335 single
  pairs that scored above 0.08 on the first-departure score and have an F head at layer 8 or later (`wire_2e_h`,
  `results/wire/seq_greedy.json`; 27 steps, these are the first 15). Decoded on the 120 select items before the held-out read
  (response 11:08:33Z; the held-out read was requested at 11:20:06Z): 57 alone, 71 with `out` U
  (`results/wire/pairs_15_select.json`). After the held-out request: the full 27 pairs 60 and 73 (11:26:05Z) and 15 pairs +
  `rot` 12 69 (11:35:41Z). No rule fixed the length 15: it was the greedy's length when the select decode was sent [AUDIT i §8.4].
- **The read** (`wire_2g_h` from `780f2de15`; strict; `results/wire/final1_test.json`, `final1_fresh.json`; board rows marked
  `final_read` in `results/bytegraft/bench/wire_2g_h/out/board.jsonl`):

  | wiring | test, of 160 | fresh, of 80 |
  |---|---|---|
  | H alone | 12 | 6 |
  | `out` U | 45 | 21 |
  | `direct` proc | 52 | 30 |
  | 15 pairs | 76 | 44 |
  | 15 pairs + `out` U | 98 | 50 |

  H alone, `out` U and `direct` proc equal the stored counts of `diff_1`, `diff_2` and `diff_3h` (12, 45, 52 on the test items;
  6 and 21 on the fresh items). F alone reads 101 of 160 on the test items (`join_3`) and 59 of 80 on the fresh items (`pair_1`'s F rows); with `out` U the
  joined system is below F alone on the fresh items (−0.1125, −0.2125 to −0.0125; AUDIT i). The join on `main` 95.
- **The published head match** (attention-map cosine, 2507.11953 §3.4; `results/wire/cosine_rule_select.json`; 120 select
  items, pairs alone): on the same 15 host heads 22 (17 on the last line only); each of the eight F heads to its best-matching
  host head 27; every host head 0; the search's pairs 57. The rule and the search agree on 2 of the 15 host heads.
- **Not shown:** above the donor (98 against 101); the two matched controls (S's weights; another item's weights), running on
  `wire_2h_h`; an independent recount (no decoded texts stored) [done 2026-11-12: `wire_2i_h` stored the rows; AUDIT i recounts every
  count, per task, from text and gold, equal to the first read]; the published byte-level form of proxy tuning (not run).
  `lenient` printed 0.0 on the two held-out lists (a defect; strict is the scored number).

<!-- JOURNAL.md lines 3844 to 3857 -->
## 2026-11-12, `wire`, the two matched controls of the 15-pair wiring on H: S's weights 8 of 120, 10 of 160, 8 of 80; another item's weights 0 on all three lists

Engineering stage; counts only (this session stored no decoded texts; the repeat with texts stored is `wire_2i_h`).

- **Run:** `wire_2h_h` from `3f31fee34` (`<instance>`), the same 15 pairs (`results/wire/chosen_pairs_15.json`) with
  `"donor": "S"` and with `"other": true`; `results/wire/controls_select.json`, `controls_test.json`, `controls_fresh.json`.
- **Right, strict** (select 120; test 160; fresh 80): F's weights 57, 76, 44 (earlier reads). S's weights (the donor without
  the skill) 8, 10, 8. F's weights from another item of the same task 0, 0, 0. H alone 8, 12, 6.
- **Reading:** the gain needs the fine-tuned donor's attention weights on the item's own text. S's weights leave H at its own
  level; with another item's weights the 15 heads read the host's own text at that item's positions: 0 of 160 and 0 of 80, below H
  alone's 12 and 6; the texts are the item's own words in the wrong places or in loops, never the other item's answer (AUDIT i
  §4). Known answer 6 checked a scaled crossed pair from S against an
  independent recomputation, and known answer 12 that no item is given itself as its other item.

<!-- JOURNAL.md lines 3858 to 3902 -->
## 2026-11-12, `wire` on Pythia 1.4B, a host of another model family: 15 `weights` pairs fixed by rule read 70 of 160 test and 35 of 80 fresh items; Pythia alone 10 and 3; S's weights 8 and 4; another item's weights 0 and 0; the donor alone 101 and 59

Engineering stage; counts. Recounted from the stored rows by an independent reader (`AUDIT_2026-11-12j.md`): every count, per
task; no shared id, prompt line or gold between the fit items and the three lists; the donors parse the prompt and the host's own
output, never the gold.

- **Host:** `EleutherAI/pythia-1.4b@fedc38a1` (GPT-NeoX, 24 layers of 16 heads, its own tokenizer and training data), through
  `NeoXHost`. Donor F; no training; no map between the two coordinate systems. A `weights` pair gives one Pythia head one F
  head's attention weights, moved onto Pythia's rows by byte span, over Pythia's own values.
- **Search** (`wire_3c_pythia`, `<instance>`, from `de77897d0`): 4,608 single pairs (12 F heads by 384 Pythia heads)
  scored on 80 fit items; greedy by `seq` over the 300 best (`results/wire_pythia/greedy_seq.json`). The best single pair is
  (10, 9)←(12, 8), `seq` +0.264. The 15 pairs use seven F heads, (12, 8), (12, 6), (12, 3), (13, 12), (10, 10), (11, 2) and
  (12, 11), all among the eight the search used on H; the sweep offered only 12 F heads, picked from H's results, so the
  overlap is partly by construction.
- **The wiring read** (`results/wire_pythia/chosen_pairs_15.json`): the first 15 pairs of that greedy, by the rule written in
  `GRAFT.md` step 32 at 15:04Z, before any wiring had been decoded on this host.
- **Read** (`wire_3d_pythia`, `<instance>`, from `36cde99db`; `results/wire_pythia/final_select.json`, `final_test.json`,
  `final_fresh.json`; rows `results/bytegraft/bench/wire_3d_pythia/out/decodes/`), strict right, per task in del, ins, sub, swap
  order:

  | wiring | select 120 | test 160 | fresh 80 |
  |---|---|---|---|
  | Pythia alone | 8 (1, 4, 3, 0) | 10 (0, 8, 2, 0) | 3 (1, 2, 0, 0) |
  | 15 pairs, F's weights | 50 (9, 20, 14, 7) | 70 (13, 25, 24, 8) | 35 (9, 12, 13, 1) |
  | 15 pairs, S's weights | 11 (3, 3, 5, 0) | 8 (0, 4, 4, 0) | 4 (2, 1, 1, 0) |
  | 15 pairs, F's weights from another item | 1 | 0 | 0 |

- **Samples** (test list). Right: `published:del_word:009539`, gold ` And lived happily ever after.`; Pythia alone
  ` And they lived happily ever after`; wired ` And lived happily ever after. "`; S's weights ` And they lived happily ever. "`.
  Wrong: `published:del_word:009948`, gold ` The brave little girl smiled herself.`; wired ` The brave little girl smiled. "`.
- **Known answers at start** (`wire_3d_pythia/out/metrics.json`): all 11 gates true; a crossed spec against a reference
  written from the definition agrees within the measured float32 allowance, and the reference with the pairs swapped gives
  infinity (known answer 15).
- **Reading:** the wiring that worked on a separately trained OLMo-2 checkpoint (12 to 76 of 160) works at about the same size
  on a model of another family. It is re-routing: the host's own values, moved along the donor's attention weights. The gain
  needs the fine-tuned donor's weights on the item's own text (both controls leave Pythia at or below its own level).
- **Not shown:** the donor's level (F alone 101 of 160 and 59 of 80; the 15 pairs are below it on both held-out lists); an
  output-level part on Pythia (no map is fitted for this host); the published byte-level output method (2506.14123, not
  run); more than one donor, skill or search run; the swap task (8 of 40, 1 of 20). The select read shares 54 words or
  sentences with the fit items, each under another task; the test and fresh reads share none (AUDIT j §2).
- **A defect found in the search score** (`GRAFT.md` step 33): the greedy went on to 35 pairs (`seq` 0.925, `exact` 0.5625)
  and that wiring decodes 3 of 120 select items; 61 of its texts begin with the gold and 58 of those do not close the quote.
  The fit items' gold had no closing, so the score could not see it. Fixed in `540a58da8` (`seq` and `exact` cover gold +
  closing; known answer 16 sets `exact` against a strict decode); `wire_3e_pythia` and `wire_2l_h` run from it.

<!-- JOURNAL.md lines 3903 to 3933 -->
## 2026-11-12, `wire` on Pythia, the search with its score through the closing quote: 27 pairs read 76 of 160 test and 36 of 80 fresh items (the 15 pairs 70 and 35); on H the new `exact` is 0 for every wiring and the session was stopped

Engineering stage; counts; not yet read by an independent reader.

- **The score** (`540a58da8`): `seq` and `exact` over gold + closing. On Pythia `exact` follows the decoded select counts along
  the old path (15 pairs 0.49 and 50 of 120; 21 pairs 0.29 and 21; 35 pairs 0.03 and 3; `results/wire_pythia/step33_sc1.jsonl`).
  Known answer 16 on the 35-pair path: exact 2, strict 2 of 10, no disagreement.
- **The search** (`wire_3e_pythia`, `<instance>`; `results/wire_pythia/step33_greedy2.json`): greedy by `seq` from the 15
  pairs over the same 300 candidates; 12 pairs added, then no candidate raised `seq`. Added, host head ← F head: (13,6)←(12,11),
  (11,11)←(12,4), (12,14)←(13,12), (8,11)←(10,10), (21,5)←(12,6), (13,15)←(12,11), (7,3)←(12,11), (4,9)←(12,6),
  (9,15)←(11,2), (14,6)←(12,8), (16,3)←(12,8), (12,8)←(12,11).
- **Read** (rule written in `GRAFT.md` step 33 before the session; rows under
  `results/bytegraft/bench/wire_3e_pythia/out/decodes/`), strict right, per task in del, ins, sub, swap order:

  | wiring | select 120 | test 160 | fresh 80 |
  |---|---|---|---|
  | 15 pairs (earlier read) | 50 | 70 | 35 |
  | 15 + 6 pairs | 57 (13, 19, 17, 8) | not read | not read |
  | 27 pairs | 60 (12, 19, 18, 11) | 76 (13, 27, 26, 10) | 36 (7, 12, 16, 1) |
  | 27 pairs, S's weights | not read | 8 | 5 |
  | 27 pairs, F's weights from another item | not read | 0 | 0 |

- **Scales** (`results/wire_pythia/step33_scales.jsonl`, fit items): every pair of the 15 at 1.25 gives `exact` 0.39, at 0.75
  0.38, against 0.49 at 1; one pair at 1.5 or 2 gives at most 0.51; leaving out one pair lowers it by at most 0.09.
- **H** (`wire_2l_h`, `<instance>`, stopped at 17:02Z before its search): `exact` 0.0 for every wiring, including
  the 15 pairs with `out` U, which decode 71 of 120 select items. H writes the closing and the newline after it; read by
  tokens, the gold's last token is then never the argmax. Known answer 16 ran there on the host alone and saw only items
  wrong under both rules. Being fixed (`GRAFT.md` step 35: `exact` by bytes; the check must see a right item).
- **Reading:** the search no longer trades the closing away, and more pairs of this kind add little on Pythia (6 test items,
  1 fresh item; not shown: +0.0375, −0.0125 to +0.0875; +0.0125, −0.0625 to +0.0875; AUDIT k). The joined system is at 76 of 160 against the donor's 101.

<!-- JOURNAL.md lines 3934 to 3962 -->
## 2026-11-12, `wire` on DeepSeek-Coder 1.3B, a model trained on code: the first 15 pairs read 70 of 160 test and 36 of 80 fresh items; the host alone 28 and 12; S's weights 26 and 10; another item's weights 5 and 0; the donor alone 101 and 59

Engineering stage; counts; not yet read by an independent reader. At inference the whole donor F runs beside the host at every
decoding step and works out where to look; the host writes the token from its own content; no training, no map.

- **Host:** `deepseek-ai/deepseek-coder-1.3b-base` at snapshot `5c35001666790ef534566439e4976b0c275eeb48` (the repository's
  `refs/pr/3`, the conversion bot's safetensors file; `main` holds only a `.bin`), `LlamaForCausalLM`, 24 layers of 16 heads,
  through `LlamaHost` (`af94c9a4a`; reviews `review_2026-11-12_wire_llama.md`).
- **Start** (`wire_5_dscoder`, `<instance>`): every gate true; known answers 8 and 9 exact (gap 0.0 and 1e-4); alone
  the host decodes 4 of 40 check and 23 of 120 select items; 80 fit items.
- **Search:** 4,608 single pairs (the 12 F heads offered on Pythia against 384 host heads); best `seq` +0.096; greedy by `seq`
  over the 300 best; the wiring read is its first 15 pairs by the rule in `GRAFT.md` step 38
  (`results/wire_dscoder/chosen_pairs.json`); at 15 pairs `seq` 0.375 and `exact` 0.45 on the fit items. Its F heads: (12, 6),
  (12, 8), (13, 12), (11, 2), (12, 4), (12, 11), (12, 3).
- **Read** by count (`results/wire_dscoder/final_count_*.json`), per task in del, ins, sub, swap order:

  | wiring | select 120 | test 160 | fresh 80 |
  |---|---|---|---|
  | the host alone | 23 (8, 7, 7, 1) | 28 (11, 9, 8, 0) | 12 (6, 4, 2, 0) |
  | 15 pairs, F's weights | 53 (12, 13, 20, 8) | 70 (23, 15, 23, 9) | 36 (10, 6, 15, 5) |
  | 15 pairs, S's weights | 22 | 26 | 10 |
  | 15 pairs, F's weights from another item | 5 | 5 | 0 |

  One decode of the 15 pairs on the test list: 70 of 160, the same per task (`final_decode_test.json`; rows under
  `results/bytegraft/bench/wire_5_dscoder/out/decodes/`).
- **Reading:** a third network that shares nothing with the donor uses its attention weights, on the same four copying
  tasks. This host does more of the task alone than H or Pythia (28 of 160 against 12 and 10), and single pairs move it
  less (+0.096 against +0.264 on Pythia). Nothing here is above the donor alone.

<!-- JOURNAL.md lines 3963 to 3988 -->
## 2026-11-12, `wire` on SmolLM2-1.7B, a third model family: the first 15 pairs read 86 of 160 test and 42 of 80 fresh items; the host alone 38 and 25; S's weights 43 and 20; another item's weights 12 and 6; the donor alone 101 and 59

Engineering stage; counts; not yet read by an independent reader. At inference the whole donor F runs beside the host at every
decoding step and works out where to look; the host writes the token from its own content; no training, no map.

- **Host:** `HuggingFaceTB/SmolLM2-1.7B@effd688a`, `LlamaForCausalLM`, 24 layers of 32 heads, through `LlamaHost`.
- **Start:** `wire_4_smollm2` (from `af94c9a4a`) stopped at known answers 8 and 9 on a float32 allowance taken from 8 items
  (gap 0.0017 against 0.0002; float64 agreed to 1e-13). `wire_4b_smollm2` (`<instance>`, from `55b416c84`, where the
  float32 gates hold a fixed ceiling of 0.01): all 21 gates true, known answer 8's gap 0.0005. Alone the host decodes 9 of 40
  check and 36 of 120 select items.
- **Search:** 9,216 single pairs (12 F heads against 768 host heads), best `seq` +0.063; greedy by `seq` over the 300 best; the
  first 15 pairs by the rule of `GRAFT.md` step 38 (`results/wire_smollm2/chosen_pairs.json`); `seq` 0.272, `exact` 0.5875.
- **Read** by count (`results/wire_smollm2/final_count_*.json`), per task in del, ins, sub, swap order:

  | wiring | select 120 | test 160 | fresh 80 |
  |---|---|---|---|
  | the host alone | 36 (9, 5, 19, 3) | 38 (7, 10, 19, 2) | 25 (7, 5, 11, 2) |
  | 15 pairs, F's weights | 58 (13, 15, 23, 7) | 86 (20, 23, 32, 11) | 42 (12, 7, 17, 6) |
  | 15 pairs, S's weights | 27 | 43 | 20 |
  | 15 pairs, F's weights from another item | 8 | 12 | 6 |

  One decode of the 15 pairs on the test list: 86 of 160, the same per task (`final_decode_test.json`).
- **Reading:** a fourth network uses the donor's attention weights on the same four copying tasks: H 12 to 76, Pythia 10 to 70,
  DeepSeek-Coder 28 to 70, SmolLM2 38 to 86 of 160. The hosts that do more alone are moved less by a single pair (best `seq`
  +0.264, +0.096, +0.063) and end higher. Nothing is above the donor alone.

<!-- JOURNAL.md lines 3989 to 4007 -->
## 2026-11-12, parts of the donor switched off under Pythia's wiring: no small part of F is enough

Counts by bytes on 40 check items (a change under about 3 items is not resolved); not yet read by an independent reader. The
whole donor F runs beside Pythia with named parts of its body replaced; Pythia's 15 pairs read their weights from that forward
(`wire_3h_pythia`, from `604df2046`; `results/wire_pythia/step40_*`; `GRAFT.md` step 40 holds every number).

- Clean: 14 of 40 check, 50 of 120 select (the stored count).
- The heads of one layer that the wiring does not read, replaced by their mean over the prompt's rows: layers 0 to 10 give
  0 to 9; layers 11 and 12 give 12 and 13; layers 13 to 15 give 14. One MLP replaced by its mean: layers 0 to 10 give 3 to 10;
  layer 11 12; layers 12 to 15 14.
- The same parts replaced by S's value at the same row: heads 7 to 14, MLPs 9 to 14: a loss of 3 or more of 14 items at the heads
  of layers 3, 4, 7, 8, 9 and 11 and the MLPs of layers 1 to 6 and 8 to 10; the other layers lose 1 or 2, under what 40 items
  resolve (AUDIT k).
- Single heads in six layers: most leave 13 to 15; the largest fall is head 4.1 (7).
- The pass that switched off "everything that did not matter" at once did not follow its rule (the coordinator's script
  treated five layers that mattered as not mattering); it gives no number.
- **Reading:** the compute that produces the pointer runs through the donor's first eleven layers, heads and MLPs both, and
  the fine-tuning's changes are spread over them. Nothing small can be cut out and attached for this skill.

<!-- JOURNAL.md lines 4008 to 4038 -->
## 2026-11-12, the boring explanation holds: a hand-made pointer with no donor weights reads 76 of 90 delete, insert and substitute select items on Pythia's 15 heads, where the donor's attention weights read 43 (with the swap items 93 of 120 against 50; Pythia alone 8) [title corrected by AUDIT k]

Counts by bytes; a control that uses the gold; not yet read by an independent reader. What runs: Pythia, with the same host
heads either reading F's attention weights (the donor running beside it at every step) or a hand-made pattern with no donor weights (F and S still parse the text to set the deciding rows, as in every wiring): at
each answer row, all weight on the host row of the source token the next gold piece is copied from (`GRAFT.md` step 41).

- **Run:** `wire_3i_pythia` (`<instance>`, from `f2cb45be1`); `results/wire_pythia/step41_oracle_select.json`. All 26
  gates true. The pointer is set at every deciding row of the start-up items (38 of 38). On 20 check items the pointer built
  from the true golds counts 12 and from the next item's golds 2.
- **The review's defect** (`review_2026-11-12_wire_oracle.md`): on swap items this version's pointer can land on a wrong token
  (3 of 25 in the reviewer's simulation), which makes it too weak there. By the rule written before launch the read is delete,
  insert and substitute (90 items); swap is printed.
- **Read** (select list; per task del, ins, sub, swap):

  | wiring | all 120 | del, ins, sub (90) | swap (30) |
  |---|---|---|---|
  | Pythia alone | 8 (1, 4, 3, 0) | 8 | 0 |
  | 15 heads, F's weights | 50 (9, 20, 14, 7) | 43 | 7 |
  | 15 heads, hand-made pointer | 93 (21, 28, 27, 17) | 76 | 17 |
  | 27 heads, F's weights | 60 (12, 19, 18, 11) | 49 | 11 |
  | 27 heads, hand-made pointer | 91 (18, 28, 27, 18) | 73 | 18 |

- **Reading** (corrected by AUDIT k): on these copying tasks the position of the next word is the answer's content: pointed at
  it, Pythia's heads copy it (76 of 90 items). This shows the heads can copy a pointed token; it does not show what else of the
  task the hosts hold. What crossed from the donor in every result of this study is a position, and the donor computes it worse
  than a script that knows the answer. The results on four hosts are a fact about hosts' copy heads being pointable from
  outside, with another network's attention weights as one way to point them. Nothing here or before shows reuse of anything
  other than a position.
- **Not shown:** the same control on H, DeepSeek-Coder and SmolLM2; swap with the fixed pointer (`2828f39cb`); any task that is
  not copying.

<!-- JOURNAL.md lines 4039 to 4067 -->
## 2026-11-13, `contains_word` on H, the first task that is not copying: seven pairs read 27 of 40 test items against H alone's 22, mostly by turning H's default answer from Yes to No; by the rule written before the read, not moved

Counts by bytes (the test list also decoded: the same 27); not yet read by an independent reader. What runs: the whole donor F
beside H at the prompt's last row; seven H heads read F's attention weights; H writes Yes or No.

- **Run:** `wire_2s_h` (from `a0724b3f8`; `results/wire_h_contains_word/`), after `wire_2q_h` exited on its first batched sweep
  (`KeyError: 'kv_batch'`; `meta/FAILURES.md`). Every gate true. Fit items: 10 Yes and 10 No golds on which F writes the gold;
  F is right on 26 of 30 Yes and 30 of 30 No candidates; H alone is right on 11 of the 20.
- **Search:** the first-order screen's 1,500 pairs over all of F's heads, scored: best `seq` +0.034, 54 above 0.02, none above
  0.05. The greedy by `seq` stopped after 7 pairs (`seq` 0.113, `exact` 0.75; H alone 0.55):
  (10,13)←(12,6), (9,4)←(1,12), (10,5)←(11,3), (9,2)←(12,6), (11,0)←(7,14), (11,5)←(12,6), (9,15)←(12,11).
- **Read** (right; Yes written; right on Yes golds; right on No golds):

  | wiring | select 30 (18 Yes) | test 40 (20 Yes) | fresh 20 (9 Yes) |
  |---|---|---|---|
  | H alone | 19; 27; 17; 2 | 22; 34; 18; 4 | 8; 17; 7; 1 |
  | 7 pairs, F's weights | 23; 11; 11; 12 | 27; 13; 10; 17 | 13; 4; 3; 10 |
  | 7 pairs, S's weights | 16; 6; 5; 11 | 18; 4; 1; 17 | 11; 2; 1; 10 |
  | 7 pairs, F's weights from another item | 17; 11; 8; 9 | 22; 10; 6; 16 | 13; 4; 3; 10 |

- **The rule** (`GRAFT.md` step 36, written before launch): moved only if the pairs are at least 8 items above H alone on the
  test list and neither answer's right count falls by more than 2. Here: 5 above, and right-on-Yes falls from 18 to 10. Not
  moved; the prediction (a Yes or No is not a position, so weights pairs do not carry it) held.
- **Reading:** H alone says Yes to almost everything. The wiring turns that around, and so do the same heads fed from S or
  from another item. F's own-item weights keep somewhat more Yes golds right than the controls on the test and select lists
  and not on the fresh list: not shown at 40 items (pairs minus another item's weights +0.125, −0.025 to +0.275; AUDIT k). The donor alone reads about 0.97 on this task (`join_3`), so nearly all of its skill here stays
  behind. With step 41: through attention weights a position crosses, and on a task where the answer is not at a position,
  close to nothing does.

<!-- JOURNAL.md lines 4068 to 4088 -->
## 2026-11-13, the pointer read again with the fixed pointer, and each Pythia head alone: 94 of 120 against F's weights' 50; the 11 heads that copy best from a pointed token are 11 of the 15 the search on the donor's weights chose

Counts by bytes; a control that uses the gold; not yet read by an independent reader. What runs: Pythia with host heads reading
either F's attention weights (the donor beside it) or the hand-made pointer (no donor weights; F and S still parse the text to
set the deciding rows).

- **Run:** `wire_3l_pythia` (`<instance>`, from `a0724b3f8`, the pointer on whole host tokens;
  `results/wire_pythia/step41b_*`).
- **Select list** (del, ins, sub, swap): alone 8 (1, 4, 3, 0); 15 heads, F's weights 50 (9, 20, 14, 7); 15 heads, pointer 94
  (21, 28, 27, 18); 27 heads, F's weights 60 (12, 19, 18, 11); 27 heads, pointer 92 (18, 28, 27, 19). The earlier read with
  the weaker pointer gave 93 and 91.
- **Each of the 384 heads alone with the pointer** (`seq` on the 80 fit items, `step41b_oracle_heads.jsonl`): head 10.9
  +0.501, 10.0 +0.390, 12.15 +0.353, 10.8 +0.276; 15 heads above 0.1; 60 above 0.02; of the 40 best, 15 are in layers 10
  and 11.
- **Against the search on the donor's weights:** of its 15 heads, 11 are the 11 best of 384 by the pointer; the other four
  rank 39, 93, 311 and 374. Of the 12 it added later, 11 rank 12 to 61. Rank correlation over the 384 heads between the best
  single-pair `seq` with F's weights and the `seq` with the pointer: 0.70; 16 heads in both top twenties.
- **Reading:** the wiring that a search on the donor's weights finds is, for the most part, the host's own set of heads that
  copy from where they are pointed, and that set can be read from the host with no donor weights in one sweep of 384 specs
  (about four minutes).

<!-- JOURNAL.md lines 4089 to 4108 -->
## 2026-11-13, `spell` and `spell_inverse` on H: ten pairs lower H from 46 to 33 of 80 test items (decoded), and the two controls lower it as much; not moved

Not yet read by an independent reader. What runs: the whole donor F beside H; ten H heads read F's attention weights; H writes
the spaced letters (`spell`) or the word (`spell_inverse`).

- **Runs:** `wire_2t_h` stopped at known answer 7, rightly (a `spell` fit item inside the select list; `meta/FAILURES.md`).
  `wire_2u_h` (from `a794c53f2`; `results/wire_h_spell/`): every gate true; fit items 19 and 20, all items H gets wrong; H
  alone decodes 8 of 20 check and 25 of 60 select items.
- **Search:** 1,500 screened pairs; best `seq` +0.096; greedy by `seq` stopped after 10 pairs (`seq` +0.396, `exact` 0.28).
- **Read** by count (per task `spell`, `spell_inverse`): select 60: alone 25 (22, 3), pairs 15 (9, 6), S's weights 20, another
  item's 16. Test 80: alone 46 (26, 20), pairs 30 (16, 14), S's weights 33, another item's 34. Fresh 40: 12, 11, 11, 11. The
  decode of the pairs on the test list: 33 of 80 (16, 17). The count is below the decode because 25 test items are right by
  bytes in other tokens; on spaced letters the decode is the number.
- **By the rule** written before launch (`GRAFT.md` step 36): not moved; the prediction held.
- **Reading:** the wiring breaks items H had right and gains none that the controls do not gain. The search climbed anyway
  because its fit items are only items H gets wrong. With `contains_word`, both tasks that are not copying a word from the
  prompt show nothing crossing through attention weights.
- **For the next search on any task where the host is right on a good share of items:** the fit set must hold items the host
  has right, so that breaking them costs score (done for the Yes/No tasks in `1c0af8c3c`; not for the others).

<!-- JOURNAL.md lines 4109 to 4148 -->
## 2026-11-13, a map fitted between the two models' residuals: on H the fine-tuning's change to the donor's late residual carries `contains_word` (33 of 40 test, 19 of 20 fresh; alone 22 and 8; another item's vectors 23 and 11); on Pythia the same grid moves nothing

Counts by bytes; not yet read by an independent reader. What runs: the whole donor (F and S) beside the host; at the answer row
a donor residual goes through a linear map and is added to the host's residual; the host writes Yes or No. The map is fitted in
closed form (ridge with a bias) on ordinary prompts without answers, rows matched by byte span; for F minus S it is fitted
from S's site and the difference goes through its linear part (`GRAFT.md` step 42; `1d1f69405`; review
`review_2026-11-13_wire_site.md`, no blocking defects).

- **Runs:** `wire_2w_h` (H) and `wire_3p_pythia`; every gate true on both. The grid: the donor's residual at layers 4, 8, 12, 15
  and 16, as F minus S and as F, into the host's residual at the proportional layer and at the final norm's input, scales 0.25,
  0.5 and 1; each spec beside S in F's place and another item's vectors (54 specs, 163 with controls and the host alone).
- **The maps** on held-out ordinary rows: about half the mean predictor's error on both hosts (H, layer 15 into the final
  input: 0.468 against 0.901; Pythia, layer 15 into 24: 0.392 against 0.809). A map fitted on randomly paired rows is at the
  mean predictor's level. F minus S through the fitted map moves the fit score more than through the random map at equal
  energy on H (0.233 against 0.057) and not on Pythia (0.244 against 0.262).
- **H, select** (30 items; alone 19): one spec passes the rule written before launch (3 above the host alone and above both
  controls): F minus S at residual 15 into the final norm input, scale 1: 24; S in F's place 19; another item 17. Its
  neighbours: residual 16 into the final input 18, 20, 15 at the three scales; residual 12 into the final input 20 at 0.5;
  every F spec (not the difference) 17 to 19.
- **H, the held-out read** (right; Yes written; right on Yes golds; right on No golds):

  | wiring | test 40 (20 Yes) | fresh 20 (9 Yes) |
  |---|---|---|
  | H alone | 22; 34; 18; 4 | 8; 17; 7; 1 |
  | residual 15, F minus S, into the final norm input, scale 1 | 33; 22; 18; 15 | 19; 8; 8; 11 |
  | with S in F's place | 22; 34; 18; 4 | 8; 17; 7; 1 |
  | with another item's vectors | 23; 22; 13; 10 | 11; 12; 6; 5 |

  Moved, by the rule: 11 above H alone and the zero write, 10 above another item's vectors, right-on-Yes kept and right-on-No
  from 4 to 15.
- **Pythia, select** (30; alone 12, it writes No every time): 51 of 54 specs stay at 12; the largest is 18 (residual 8 as F into
  residual 12, scale 1) with controls 16 and 17. No spec passes; no held-out read.
- **Reading:** the first thing that is not a position to cross with its controls failing. It is the donor's decision, late in
  the donor, written at the host's output end through a fitted map: the host reads it out and computes nothing further with
  it. It crosses into a host of the donor's own family and not into Pythia, although the maps predict ordinary text equally
  well on both. Nothing at an inner layer moved either host.
- **Not shown:** above the donor alone (about 0.97); an inner-layer write that the host builds on; a host of another family;
  the edit tasks through this part (Pythia's grid is running as `wire_3o_pythia`).
