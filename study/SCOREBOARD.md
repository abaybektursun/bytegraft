# BYTEGRAFT scoreboard: two levels of success

The study's owner, 2026-11-12: two levels of success, both measured and tracked. First, reusing one model's computation
in another with no training. Second, climbing benchmarks and scoring evaluations on specific tasks.




Every row says what runs at inference and which model does the computing. A row is entered only with its file and key.

## Level 1: a computation of one model reused by another, with no training

A case counts when a computation taken from a donor is used by a host it was never trained with, with no training of either, to
do something the host does not do alone, and both controls fail (the same connection fed from the donor without the skill; fed
with the donor's values from another input). Each row carries the host alone, the donor alone and the joined system together,
and how much of the donor ran. Three separate answers per row, in place of one grade (changed 20:03Z after the owner's
question, item 39: one word, "weak", had hidden that the reuse itself is shown): reuse shown (the host gains and both controls
fail); the joined system above its best part; the donor's part isolated (only a small part of the donor runs).

Strict right counts on the four word-edit tasks (160 test items, 80 fresh items). At inference the whole donor F
(`allenai/Bolmo-1B`) runs beside the host at every decoding step and works out where to look; the host writes the token from its
own content.

| donor (what is reused) | host | host alone | joined | donor alone | donor without the skill (S) | another input | how much of the donor ran | trained | reuse shown | above the best part | part isolated | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F: the attention weights of 8 heads, into 15 host heads | OLMo-2 1B checkpoint `stage1-step1907359`, separately trained | 12; 6 | 76; 44 | 101; 59 | 10; 8 | 0; 0 | all of F (measured on Pythia, step 40: no small part is enough) | no | yes | no | no | `AUDIT_2026-11-12i.md` |
| the same, with F's attention-output change through a map (the output part) | the same | 12; 6 | 98; 50 | 101; 59 | not read | not read | all of F and S | no; the map is a closed-form fit on token embeddings | yes for the gain; controls not read | no | no | `AUDIT_2026-11-12i.md` |
| F: the attention weights of 7 heads, into 15 host heads | Pythia 1.4B (GPT-NeoX; another family, tokenizer, training data) | 10; 3 | 70; 35 | 101; 59 | 8; 4 | 0; 0 | all of F | no | yes | no | no | `AUDIT_2026-11-12j.md` |
| the same, into 27 host heads | Pythia 1.4B | 10; 3 | 76; 36 | 101; 59 | 8; 5 | 0; 0 | all of F | no | yes | no | no | `JOURNAL.md`, the entry on the search through the closing quote; not yet read by an independent reader |
| the same 15, with the output part at a quarter of its size | Pythia 1.4B | 10; 3 | 77; 41 | 101; 59 | 23; 6 (the output part kept) | not read | all of F and S | no; the map as above | yes (S's weights with the output part kept give 23; 6; another input not read) | no | no | `GRAFT.md` step 34; not yet read by an independent reader (against its weights part alone +0.044, 0.000 to 0.094, and +0.075, 0.000 to 0.150; the scale was picked among several on the fit and select items; AUDIT k) |
| F: the attention weights of 7 heads, into 15 host heads | DeepSeek-Coder 1.3B (Llama type; trained on code) | 28; 12 | 70; 36 | 101; 59 | 26; 10 | 5; 0 | all of F | no | yes | no | no | `GRAFT.md` step 38; `results/wire_dscoder/`; not yet read by an independent reader |
| F: the attention weights of 5 heads, into 15 host heads | SmolLM2-1.7B (Llama type; a third family) | 38; 25 | 86; 42 | 101; 59 | 43; 20 | 12; 6 | all of F | no | yes | no | no | `GRAFT.md` step 38; `results/wire_smollm2/`; not yet read by an independent reader |


What these rows are, said both ways. As reuse: a network that shares no weights, tokenizer, training data or architecture
family with the donor does a task it could not do (Pythia 10 to 70 of 160), with no training and no fitted map, from the
attention weights of a few donor heads; research pass 10 found no published case across families. As a system: nothing is gained
over the donor alone (101 of 160), the whole donor runs, and for this task where to look is most of the answer.

Distinct cases so far: one donor, one skill (four tasks that are all copying with one change), four hosts. Not shown anywhere: a case where the joined system is above the donor
alone; the reused part isolated; a second skill; a second donor.

The control that sets how every row above is read (`GRAFT.md` step 41, Pythia, select list, counts): the same 15 host heads
pointed by a script that knows the answer, with no donor weights (F and S still parse the text to set the deciding rows, as in every wiring), read 76 of 90 delete, insert and substitute items against the
donor's weights' 43 (the read the rule names; with the swap items 93 of 120 against 50); alone 8. So what is reused in every row is a position; on these copying tasks the position of the
next word is the answer's content, and the host's heads copy the pointed token; the donor is one way, not the best, of computing
the position (AUDIT k: this does not show what else of the task the hosts hold). No row shows reuse of anything but a position.

The first reuse of something that is not a position (`GRAFT.md` step 42, `contains_word`, host H; not yet read by an
independent reader). What runs: the donor (F and S) beside H; the fine-tuning's change to the donor's residual at layer 15 goes
through a map fitted in closed form on ordinary prompts into H's final norm input. Test list (40, 20 Yes): H alone 22; joined 33
(right on Yes 18, on No 15); the same write with S in F's place 22; with another item's vectors 23; the donor alone about 39.
Fresh list (20): 8; 19; 8; 11. Reuse shown: yes, with both controls failing. Above the best part: no. Part isolated: no. It is a
write at the host's output end into a host of the donor's own family, chosen among 54 specs on 30 select items; on Pythia the
same grid moves nothing.

A task that is not copying (`GRAFT.md` step 36, `contains_word`, a Yes or No answer, host H, test list of 40 with 20 Yes): H
alone 22 right (it writes Yes 34 times); seven heads with the donor's attention weights 27 (Yes written 13; right on Yes 10, on
No 17); the same heads with the weights of the donor without the skill 18, with another item's weights 22; the donor alone
about 0.97 on this task. By the rule written before the read it is not moved: the wiring mostly turns the host's default answer
around. Reuse shown: no.

Spelling (`GRAFT.md` step 36, `spell` and `spell_inverse`, host H, test list of 80): H alone 46 right; ten heads with the
donor's attention weights 30 by count and 33 by decode; the same heads fed from the donor without the skill 33, from another
item 34. The wiring lowers the host and the controls lower it as much. Reuse shown: no.

Measured since (`GRAFT.md` step 40, Pythia, 40 items): the donor's part is not small. The heads of any one layer from 0 to 10,
or any one MLP from 0 to 10, replaced by a constant, cost the host a third to all of its count; only the layers above the heads
the wiring reads can be off. So "part isolated" stays no, and for this skill a small part attached alone is not available.

Named targets, not started: a second skill (step 36); a language model
joined to a robot policy through the instruction text they both read (the owner's example; it needs a simulator).

## Level 2: a joined system above its parts and above the ordinary method on a named benchmark

| benchmark, under its own rules | our system | our number | best single part | strongest ordinary method | source |
|---|---|---|---|---|---|
| none yet | | | | | |

Nothing of ours is above the best of its parts on any task. The ordinary method that would stand beside the level 1 rows, proxy
tuning in its byte-level form (2506.14123), has not been run.
