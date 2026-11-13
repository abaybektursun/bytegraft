# ByteGraft: a byte model running beside other language models

An interactive page, with its data, about one study: what of a byte-level language model (allenai/Bolmo-1B) can be used by
token-level models it was never trained with, at run time, with no training. The attention-weight results need no map
between the models; the rows that add an "output part" or a "residual map" use maps fitted in closed form.

- **The page:** `docs/index.html` (on GitHub Pages: https://abaybektursun.github.io/bytegraft/). It runs offline; every
  number, text and token on it comes from the study's stored runs.
- **Snapshot:** the study at commit `1a55d3e8a` of its private working repository, 2026-11-13. The study continues; this
  copy does not follow it.
- **Added 2026-11-13:** section 14 of the page, `study/NOTES_ptr.md` and `results/ptr/`, from branch `research/ptr-install`
  at commit `76180a711` (result 6 below). Sections 1 to 13 and their data are unchanged.

## What runs at inference, in every result

The whole of Bolmo-1B runs on the same text beside the receiving model at every decoding step. Bolmo-1B-Stage1 (the same
model before its editing skill) also reads the text, to set which positions are paired; the output part and the residual map
use its activations too. Bolmo works out where to look;
the receiving model writes the token from its own computation. With Bolmo switched off, the receiving model is unchanged.
Bolmo alone gets 101 of 160 test items right on the four word-edit tasks used here, more than any joined system. By the
study's own definition this is not yet a graft: a graft is a small part of the donor attached so that neither part alone does
the task, or the receiving model doing the task with the donor switched off.

## Results, as counts of right answers (160 test items, 80 fresh items, strict scoring)

1. **Whole attention outputs** of Bolmo-1B copied into OLMo-2-0425-1B, the token model Bolmo was built from, at every layer:
   16 to 95 of 160. Into separately trained OLMo checkpoints: 0.
2. **Choosing 16 of the 256 heads.** Two Claude agents with a per-head evidence table, a fixed script with the same table,
   and a gradient ranking all land at 57 to 63 of 160; random search and a ridge-surrogate search without the table, 22 and 23;
   greedy forward selection with 1,048 scored sets, 75. No advantage of the language model over the script is shown.
3. **Attention weights alone.** Bolmo's attention weights over OLMo's own values: 77 of 160; OLMo's weights over Bolmo's
   values: 37.
4. **Attention weights into four models that share no weights with Bolmo**, 15 receiving heads each, no map, no training:
   OLMo-2 1B stage1-step1907359 12 to 76; Pythia 1.4B 10 to 70; DeepSeek-Coder 1.3B 28 to 70; SmolLM2-1.7B 38 to 86. Bolmo-1B-Stage1's
   weights (the same model without the editing skill) and Bolmo's weights from another item give little or nothing.
5. **Through attention weights, what crosses is a position** (measured on Pythia, selection list). A hand-made pointer that
   uses the answer, with no Bolmo weights, reads 94 of 120 selection items where Bolmo's weights read 50. Eleven of the 15 heads the search on Bolmo's weights chose are Pythia's
   eleven best heads under that pointer. No small part of Bolmo is known to be enough to compute the position. Two kinds of task whose
   answer is not a position (contains_word; spell and spell_inverse) do not move through attention weights. A residual map
   fitted in closed form carries contains_word into the OLMo checkpoint: 33 of 40 test and 19 of 20 fresh items, against 22
   and 8 for the checkpoint alone (not yet read by an independent reader).
6. **The pointer in the receiving model's own weights, Bolmo off** (page section 14; this result trains weights, and uses
   800 test items with a whitespace-normalized match, so its counts cannot be compared with those above). Giving 15 chosen
   heads a script-made pointer, with no weight changed, takes Pythia 1.4B, SmolLM2-1.7B and DeepSeek-Coder 1.3B from 26, 219
   and 134 of 800 to 730, 768 and 750; 15 random heads give 36, 233 and 36. Fitting each head's query and key weights to the
   pointer without a gradient across layers reaches 451 to 577, below end-to-end training of the same heads (542 to 720).
   Query/key-only training of every head reaches 750, 790 and 734; value/output-only training 774, 734 and 789, at a higher
   loss on other prompts. With all 12 tasks on SmolLM2 the two tie (1,661 and 1,653 of 2,400) and the character-edit tasks
   stay at 11 to 81 of 200. No LoRA or full fine-tuning baseline was run; no practical win over ordinary fine-tuning is
   shown. One seed; not read by an independent reader.
7. **Not shown:** a joined system above Bolmo alone; the byte-level form of proxy tuning (arXiv 2506.14123), the published
   method closest to these results, has not been run beside them.

The study calls these engineering-stage counts. Independent recounts from the stored rows: `study/AUDIT_2026-11-12i.md`
(the OLMo checkpoint), `AUDIT_2026-11-12j.md` (Pythia's 15 pairs), `AUDIT_2026-11-12k.md` (Pythia's 27 pairs and output
part, DeepSeek-Coder, SmolLM2, the parts of Bolmo switched off, the contains_word wiring and the first pointer read). Not
recounted: the fixed pointer read (94 of 120), the per-head sweep, spelling and the residual map. The page marks each.

## Contents

| path | what it is |
|---|---|
| `docs/index.html`, `docs/data.js` | the page and the numbers it shows |
| `build/build_explainer_data.py` | writes `data.js`; checks every count against the audit, recompute and result files |
| `results/` | every result file of the study's repository that the build reads (56 files) |
| `study/` | the audits the page cites, the scoreboard, and the journal entries the page uses (`JOURNAL_excerpt.md`) |
| `study/NOTES_ptr.md`, `results/ptr/` | the note and the 15 metrics files behind page section 14 (the job code is not in this repository) |
| `REDACTIONS.md` | every private name replaced in the copied files, and the one edit that is not a redaction |

The per-item decode rows the build also reads (about 15 MB) are kept in the study's storage and are not in this repository,
so the build cannot be rerun from this copy alone; the page and `data.js` are complete.

## License

CC BY 4.0 for text and figures. See `LICENSE`.
