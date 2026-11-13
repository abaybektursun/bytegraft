"""Data for join_explainer.html, read from stored runs. No model is run.

Run with a Python that has `tokenizers` (OLMo's tokenizer is a lookup table plus BPE merges, not a model):
    python build_explainer_data.py <folder with the inputs below>
Writes join_explainer_data.js next to this file.

Inputs (copied from S3, bucket <s3-bucket>):
    published.jsonl            results/bytegraft/bank/smoke_7/season_1/published.jsonl
    join_4.decodes.jsonl       results/bytegraft/join/join_4/out/decodes.jsonl
    join_3.decodes.jsonl       results/bytegraft/join/join_3/out/decodes.jsonl
    diff_3m.decodes.jsonl      results/bytegraft/join/diff_3m/out/decodes.jsonl
    dist_1.decodes.jsonl       results/bytegraft/join/dist_1/out/decodes.jsonl
    select1/                   results/bytegraft/bench/select_1/out/{evidence.csv, references.json, rankings.json, scored.jsonl}
                               and results/bytegraft/select/select_1_final_{a,b}/out/decodes.jsonl as final_{a,b}.decodes.jsonl
    (and, from this repository: studies/bytegraft/results/select_1/{select_1_final_sets.json, recompute.json},
     studies/bytegraft/results/audit_2026-11-11f/audit_select.json)
    new/                       later runs: route/decodes.jsonl (results/bytegraft/route/route_1/out/decodes.jsonl);
                               select_2_final/ and select_3_final/decodes.jsonl (results/bytegraft/select/select_{2,3}_final/out/);
                               pair_1/decodes.jsonl (results/bytegraft/pair/pair_1/out/); wire_h/*.jsonl and wire_py/*.jsonl
                               (results/bytegraft/bench/wire_2i_h/out/decodes/ and bench/wire_3d_pythia/out/decodes/)
    (and, from this repository: studies/bytegraft/results/{select_2, select_3, route_1, wire, wire_pythia, audit_2026-11-12h2,
     audit_2026-11-12i}/)
    olmo_tokenizer.json        weights/hf/hub/models--allenai--OLMo-2-0425-1B/snapshots/a1847dff35000b4271fa70afc5db10fd29fedbdf/tokenizer.json
    olmo_config.json           the same snapshot's config.json
    bolmo_config.json          weights/hf/hub/models--allenai--Bolmo-1B/snapshots/452690a8cfab1dd1ec27b74f2667632f17a21b46/config.json
"""
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

from tokenizers import Tokenizer

ITEM = "published:del_word:009539"
EDIT = ("del_word", "ins_word", "sub_word", "swap_word")
DRAWS, SEED = 10_000, 20261111
# Known answers: right answers of 160 on the four edit tasks, AUDIT_2026-11-11e.md §1 table.
AUDIT_E = {"O": 16, "deciding": 95, "PD": 42, "deciding_early": 40, "PD_early": 15, "deciding_late": 75, "PD_late": 45,
           "P2": 41, "F": 101}


def rows(path):
    return [json.loads(line) for line in open(path)]


def by_id_cond(rs, host=None):
    out = defaultdict(dict)
    for r in rs:
        if r.get("host") == host:
            out[r["id"]][r["condition"]] = r
    return out


def main(src: Path):
    tok = Tokenizer.from_file(str(src / "olmo_tokenizer.json"))
    published = {r["id"]: r for r in rows(src / "published.jsonl")}
    j4 = by_id_cond(rows(src / "join_4.decodes.jsonl"))
    j3 = by_id_cond(rows(src / "join_3.decodes.jsonl"))
    d3 = by_id_cond(rows(src / "diff_3m.decodes.jsonl"), host="main")
    dist_rows = rows(src / "dist_1.decodes.jsonl")
    if not d3:  # diff_3m rows may carry no host key
        d3 = by_id_cond(rows(src / "diff_3m.decodes.jsonl"))

    edit_ids = sorted(i for i, c in j4.items() if c["O"]["task"] in EDIT)
    assert len(edit_ids) == 160, len(edit_ids)
    task_of = {i: j4[i]["O"]["task"] for i in edit_ids}
    assert all(sum(task_of[i] == t for i in edit_ids) == 40 for t in EDIT)

    # The tokenization the job used: BOS + encode(context). Check: 1 / (deciding share at step 0) = number of positions.
    bos = tok.token_to_id("<|endoftext|>")
    for i, c in j4.items():
        s0 = c["deciding"]["steps"][0]
        if s0["last_carried"]:
            n = 1 + len(tok.encode(published[i]["context"], add_special_tokens=False).ids)
            assert abs(1 / s0["carried_share"] - n) < 1e-6, (i, n, s0["carried_share"])

    # Per-item correctness tables (strict, the field `correct`).
    table = {}
    for c in ("O", "all", "context", "deciding", "deciding_early", "deciding_late", "F"):
        table[c] = {i: bool(j4[i][c]["correct"]) for i in edit_ids}
    for c in ("PD", "PD_early", "PD_late", "P2"):
        table[c] = {i: bool(d3[i][c]["correct"]) for i in edit_ids}
    for c in ("S", "S_scaled", "other"):
        table["j3_" + c] = {i: bool(j3[i][c]["correct"]) for i in edit_ids}
    for c, n in AUDIT_E.items():
        got = sum(table[c].values())
        assert got == n, f"{c}: {got} right of 160, AUDIT e says {n}"

    # Separately trained OLMo checkpoints as host (dist_1), alone ("O") and with all paired positions copied ("all").
    dist = {}
    for host in ("stage1-step1907359-tokens4001B", "stage1-step970000-tokens2035B", "stage1-step190000-tokens399B", None):
        m = by_id_cond(dist_rows, host=host)
        assert set(edit_ids) <= set(m), host
        for c in ("O", "all"):
            dist[f"{host or 'main'}|{c}"] = {i: bool(m[i][c]["correct"]) for i in edit_ids}
    assert sum(dist["main|O"].values()) == AUDIT_E["O"]

    rng = random.Random(SEED)
    by_task = {t: [i for i in edit_ids if task_of[i] == t] for t in EDIT}
    draws = [{t: [rng.randrange(40) for _ in range(40)] for t in EDIT} for _ in range(DRAWS)]

    def stat(vals_of):            # vals_of: item -> float; mean over the four task means, with a within-task bootstrap
        point = sum(sum(vals_of[i] for i in by_task[t]) / 40 for t in EDIT) / 4
        bs = sorted(sum(sum(vals_of[by_task[t][k]] for k in d[t]) / 40 for t in EDIT) / 4 for d in draws)
        return {"mean": point, "lo": bs[int(0.025 * DRAWS)], "hi": bs[int(0.975 * DRAWS) - 1]}

    def summary(tab):
        out = stat({i: float(tab[i]) for i in edit_ids})
        out["right"] = sum(tab.values())
        out["per_task"] = {t: sum(tab[i] for i in by_task[t]) for t in EDIT}
        return out

    acc = {k: summary(v) for k, v in {**table, **{"dist|" + k: v for k, v in dist.items()}}.items()}
    diffs = {}
    for a, b in (("deciding", "O"), ("deciding", "F"), ("deciding", "PD"), ("deciding_early", "PD_early"),
                 ("deciding_late", "PD_late"), ("deciding", "P2")):
        diffs[f"{a}-{b}"] = stat({i: float(table[a][i]) - float(table[b][i]) for i in edit_ids})

    # The item.
    it = published[ITEM]
    enc = tok.encode(it["context"], add_special_tokens=False)
    ctx = it["context"].encode("utf-8")
    assert ctx.decode("ascii") == it["context"]          # ASCII, so byte offsets = character offsets
    spans = [list(o) for o in enc.offsets]
    assert spans[0][0] == 0 and spans[-1][1] == len(ctx) and all(a[1] == b[0] for a, b in zip(spans, spans[1:]))
    positions = [{"pos": 0, "id": bos, "text": "<|endoftext|>", "span": None}]
    positions += [{"pos": k + 1, "id": i, "text": it["context"][a:b], "span": [a, b]} for k, (i, (a, b)) in enumerate(zip(enc.ids, spans))]
    full = [all(abs(s["carried_share"] - 1) < 1e-9 for s in j4[ITEM]["all"]["steps"])]
    assert full[0], "the item must have every position paired at every step"

    def toks(r):
        return [{"id": t, "text": tok.decode([t])} for t in (r.get("tokens") or [])]

    rep = d3[ITEM]["deciding_reproduced"]
    assert rep["generated"] == j4[ITEM]["deciding"]["generated"] and rep["tokens"] == j4[ITEM]["deciding"]["tokens"]
    n_prompt = len(positions)
    steps = []
    for t, s in enumerate(rep["steps"]):
        assert abs(s["carried_share"] - (t + 1) / (n_prompt + t)) < 1e-9 and s["last_carried"], (t, s["carried_share"])
        steps.append({"t": t, "carried": t + 1, "positions": n_prompt + t, "own": s["own"], "landed": s["landed"]})

    runs = {}
    for c in ("O", "all", "context", "deciding", "deciding_early", "deciding_late", "F"):
        r = j4[ITEM][c]
        runs[c] = {"generated": r["generated"], "correct": bool(r["correct"]), "tokens": toks(r)}
    for c in ("PD", "PD_early", "PD_late", "P2"):
        r = d3[ITEM][c]
        runs[c] = {"generated": r["generated"], "correct": bool(r["correct"]), "tokens": toks(r)}

    olmo, bolmo = (json.load(open(src / f)) for f in ("olmo_config.json", "bolmo_config.json"))
    arch = {k: olmo[k] for k in ("hidden_size", "intermediate_size", "num_attention_heads", "num_hidden_layers", "vocab_size", "rms_norm_eps")}
    arch["head_dim"] = olmo["hidden_size"] // olmo["num_attention_heads"]
    arch["bolmo"] = {k: bolmo[k] for k in ("hidden_size", "intermediate_size", "num_attention_heads", "num_hidden_layers", "head_dim",
                                         "num_local_encoder_layers", "num_local_decoder_layers", "vocab_size", "subword_vocab_size",
                                         "boundary_predictor_lookahead", "block_type", "add_expanded_embeddings")}
    for k in ("hidden_size", "intermediate_size", "num_attention_heads", "num_hidden_layers"):
        assert arch[k] == arch["bolmo"][k], k

    res = Path(__file__).resolve().parents[1] / "results"
    select = build_select(src / "select1", res, table, edit_ids, j4)
    later = build_later(src / "new", res, select, table, edit_ids, task_of, stat)
    select.pop("_rows")
    data = {"item": {"id": ITEM, "task": it["task"], "context": it["context"], "gold": it["gold"], "sentence": it["word_or_sentence"],
                     "positions": positions, "n_prompt": n_prompt},
            "runs": runs, "steps": steps, "acc": acc, "diffs": diffs, "arch": arch,
            "draws": DRAWS, "seed": SEED, "n_items": 160, "select": select, **later}
    out = Path(__file__).with_name("join_explainer_data.js")
    out.write_text("// Generated by build_explainer_data.py from stored runs; do not edit.\nconst DATA = " + json.dumps(data) + ";\n")
    print("wrote", out, f"{out.stat().st_size} bytes")
    for k in ("O", "deciding", "deciding_early", "deciding_late", "all", "context", "F", "PD", "P2", "j3_S", "j3_S_scaled", "j3_other"):
        a = acc[k]
        print(f"{k:16s} {a['right']:3d}/160  {a['mean']:.3f} ({a['lo']:.3f} to {a['hi']:.3f})  {a['per_task']}")
    for k, v in acc.items():
        if k.startswith("dist|"):
            print(f"{k:44s} {v['right']:3d}/160  {v['mean']:.3f}")
    for k, v in diffs.items():
        print(f"{k:28s} {v['mean']:+.4f} ({v['lo']:+.4f} to {v['hi']:+.4f})")


ATT = ("operand", "verb_quotes", "sentence", "previous", "first")
METHODS = ("agent_a", "agent_b", "random", "surrogate")


def build_select(sel: Path, res: Path, table: dict, edit_ids: list, j4: dict) -> dict:
    """select_1: the evidence table, the single-head screen, the gradient ranking, every scored set, the final sets and their test reads."""
    import csv
    ev = list(csv.DictReader(open(sel / "evidence.csv")))
    assert len(ev) == 256 and [(int(r["layer"]), int(r["head"])) for r in ev] == [(L, h) for L in range(16) for h in range(16)]
    heads = []
    for r in ev:
        row = {k: float(v) for k, v in r.items() if k not in ("layer", "head", "F_items")}
        row["F_items"] = int(r["F_items"])
        row["att_shift"] = sum(abs(row["F_" + a] - row["main_" + a]) for a in ATT)    # the table's attention columns, |F − main| summed
        heads.append(row)
    refs, rk = json.load(open(sel / "references.json")), json.load(open(sel / "rankings.json"))
    singles = {tuple(map(tuple, s["set"]))[0]: s["score"] for s in refs["singles"]}
    assert len(singles) == 256
    grad = rk["gradient"]["scores"]
    for i, (L, h) in enumerate((L, h) for L in range(16) for h in range(16)):
        heads[i]["single"], heads[i]["gradient"] = singles[(L, h)], grad[L][h]
    top = lambda key: sorted(sorted(range(256), key=lambda i: -heads[i][key])[:16])       # noqa: E731
    as_pairs = lambda idx: [[i // 16, i % 16] for i in idx]                                 # noqa: E731
    final = json.load(open(res / "select_1" / "select_1_final_sets.json"))
    assert as_pairs(top("gradient")) == sorted(final["gradient_top16"]["set"]) == sorted(rk["gradient"]["top16"])
    assert as_pairs(top("direct_effect")) == sorted(final["direct_top16"]["set"]) == sorted(rk["direct_effect"]["top16"])
    assert as_pairs(top("single")) == sorted(rk["single_head"]["top16"])
    assert abs(refs["all_256"]["score"] - 3.904171581051082) < 1e-9 and refs["none"]["score"] == 0.0

    scored = defaultdict(list)
    for line in open(sel / "scored.jsonl"):
        r = json.loads(line)
        if r["requester"] in METHODS:
            scored[r["requester"]].append({"set": r["set"], "score": r["score"], "round": len(scored[r["requester"]]) // 20 + 1})
    for m in METHODS:
        assert len(scored[m]) == 60, (m, len(scored[m]))
        best = max(scored[m], key=lambda s: s["score"])
        assert sorted(best["set"]) == sorted(final[m]["set"]) and abs(best["score"] - final[m]["fit_score"]) < 1e-12, m

    audit = json.load(open(res / "audit_2026-11-11f" / "audit_select.json"))
    rec = json.load(open(res / "select_1" / "recompute.json"))
    dec = {}
    for p in "ab":
        for line in open(sel / f"final_{p}.decodes.jsonl"):
            r = json.loads(line)
            dec.setdefault(r["condition"], {})[r["id"]] = r
    test = {}
    for m, rows in dec.items():
        assert set(rows) == set(edit_ids), m
        right = [sum(rows[i]["correct"] for i in edit_ids if rows[i]["task"] == t) for t in EDIT]
        if m in rec["right_del_ins_sub_swap"]:
            assert right == rec["right_del_ins_sub_swap"][m], m
        a = audit["accuracy"][m]
        assert right == a["per_task"] and sum(right) == a["right"], m
        test[m] = {"right": sum(right), "per_task": right, "mean": a["mean"], "lo": a["lo"], "hi": a["hi"]}
    for m, key in (("all_256", "deciding"), ("none", "O")):          # the stored rows the study uses for these two
        right = [sum(table[key][i] for i in edit_ids if j4[i]["O"]["task"] == t) for t in EDIT]
        a = audit["accuracy"][m]
        assert right == a["per_task"], m
        test[m] = {"right": sum(right), "per_task": right, "mean": a["mean"], "lo": a["lo"], "hi": a["hi"]}
    example = {m: {"generated": rows[ITEM]["generated"], "correct": bool(rows[ITEM]["correct"])} for m, rows in dec.items()}
    rule = audit["rules"]["attention_shift_L1"]
    assert abs(rule["fit_if_scored"] - 1.450438546212749) < 1e-12
    sets = {m: sorted(final[m]["set"]) for m in ("agent_a", "agent_b", "random", "surrogate", "gradient_top16", "direct_top16")}
    sets["att_shift_rule"] = sorted(rule["set"])
    fit = {m: final[m].get("fit_score") for m in ("agent_a", "agent_b", "random", "surrogate")}
    fit["att_shift_rule"], fit["direct_top16"] = rule["fit_if_scored"], audit["rules"]["direct_effect"]["fit_if_scored"]
    paired = {k: audit["paired"][k] for k in ("A - surrogate", "A - gradient_top16", "A - direct_top16", "agent_a - agent_b")}
    quotes = {"agent_a": "The table's direct-effect column ranked heads badly: its top head, 15.8, scored -0.009 alone. Attention change in "
                         "layers 8 to 15 ranked the right heads.",
              "agent_b": "The donor shifts these heads' attention away from the operand: four of them onto the rest of the sentence, and 12.1 "
                         "off the instruction words."}
    for m, q in quotes.items():
        assert q in audit["final_words"][m], m
    print("select_1:", {m: test[m]["right"] for m in test}, "fit", {m: round(v, 3) for m, v in fit.items() if v is not None})
    return {"heads": heads, "scored": scored, "sets": sets, "fit": fit, "test": test, "example": example, "paired": paired,
            "all_256_fit": refs["all_256"]["score"], "best_single": max(singles.items(), key=lambda kv: kv[1]), "quotes": quotes,
            "_rows": {m: {i: bool(r[i]["correct"]) for i in edit_ids} for m, r in dec.items()}}


def rounds_of(n_sets: int, dup: int) -> list:
    """Round of each scored set: rounds of 20, round 1 short by `dup` dropped duplicates and round 3 longer by as many (select_2's rule)."""
    assert n_sets == 60
    return [1] * (20 - dup) + [2] * 20 + [3] * (20 + dup)


def build_later(new: Path, res: Path, sel: dict, table: dict, edit_ids: list, task_of: dict, stat) -> dict:
    """The runs after select_1: select_2 and select_3 (more head-set searches), route_1 (weights apart from values), wire (attention
    weights given to heads of separately trained hosts). Every count is checked against the study's own recompute or result files."""
    ld = lambda p: json.load(open(p))                       # noqa: E731
    per = lambda tab, ids: [sum(tab[i] for i in ids if task_of_all[i] == t) for t in EDIT]   # noqa: E731

    # ---- the fresh list (80 edit items, 20 per task) and a bootstrap for it, as `stat` does for the 160 (independent draws per task)
    s2 = rows(new / "select_2_final" / "decodes.jsonl")
    s3 = rows(new / "select_3_final" / "decodes.jsonl")
    p1 = rows(new / "pair_1" / "decodes.jsonl")
    fresh_ids = sorted({r["id"] for r in s2 if r["condition"] == "agent_a"})
    assert len(fresh_ids) == 80 and not set(fresh_ids) & set(edit_ids)
    task_of_all = dict(task_of)
    task_of_all.update({r["id"]: r["task"] for r in s2})
    fresh_by_task = {t: [i for i in fresh_ids if task_of_all[i] == t] for t in EDIT}
    assert all(len(v) == 20 for v in fresh_by_task.values())
    rng = random.Random(f"{SEED}:fresh")
    draws20 = [{t: [rng.randrange(20) for _ in range(20)] for t in EDIT} for _ in range(DRAWS)]

    def stat20(vals_of):
        point = sum(sum(vals_of[i] for i in fresh_by_task[t]) / 20 for t in EDIT) / 4
        bs = sorted(sum(sum(vals_of[fresh_by_task[t][k]] for k in d[t]) / 20 for t in EDIT) / 4 for d in draws20)
        return {"mean": point, "lo": bs[int(0.025 * DRAWS)], "hi": bs[int(0.975 * DRAWS) - 1]}

    def summ(tab: dict, which: str) -> dict:
        ids = edit_ids if which == "test" else fresh_ids
        assert set(tab) == set(ids), which
        out = (stat if which == "test" else stat20)({i: float(tab[i]) for i in ids})
        out["right"], out["per_task"] = sum(tab.values()), per(tab, ids)
        return out

    # ---- per-item rows of every head set (test and fresh)
    tabs = {"test": dict(sel["_rows"]), "fresh": {}}
    tabs["test"]["all_256"], tabs["test"]["none"] = table["deciding"], table["O"]
    texts = {}
    for r in s2 + s3:
        which = "test" if r["id"] in table["O"] else "fresh"
        tabs[which].setdefault(r["condition"], {})[r["id"]] = bool(r["correct"])
        if r["id"] == ITEM:
            texts[r["condition"]] = {"generated": r["generated"], "correct": bool(r["correct"])}
    for r in p1:
        if r["id"] in fresh_by_task.get(r["task"], []) and r["condition"] == "O":
            tabs["fresh"].setdefault("none", {})[r["id"]] = bool(r["correct"])
    route = rows(new / "route" / "decodes.jsonl")
    for r in route:
        if r["condition"] == "join" and r["id"] in fresh_ids:
            tabs["fresh"].setdefault("all_256", {})[r["id"]] = bool(r["correct"])
    rec2, rec3 = ld(res / "select_2" / "recompute.json"), ld(res / "select_3" / "recompute.json")
    for which in ("test", "fresh"):
        for m, tab in tabs[which].items():
            ids = edit_ids if which == "test" else fresh_ids
            want = rec3["right"][which].get(m) or rec2["right"][which].get(m)
            if m == "all_256" and which == "fresh":
                want = ld(res / "route_1" / "metrics.json")["steps"]["results"]["route"]["all"]["strict"]["fresh"]["right"]["join"]
            assert want is not None and per(tab, ids) == [want[t] for t in EDIT], (which, m, per(tab, ids), want)
    acc = {w: {m: summ(tab, w) for m, tab in tabs[w].items()} for w in ("test", "fresh")}
    for m, v in rec3["accuracy"]["test"].items():
        assert abs(acc["test"][m]["mean"] - v) < 1e-12, m
    for m, v in rec3["accuracy"]["fresh"].items():
        assert abs(acc["fresh"][m]["mean"] - v) < 1e-12, m

    # ---- the later searches: scored sets, greedy's path, final sets, fit scores
    sc = ld(res / "select_2" / "scripts.json")
    g3 = ld(res / "select_3" / "select3.json")
    f3 = ld(res / "select_3" / "select_3_final_sets.json")
    scored = {}
    for m, src in (("script_columns", sc["script_columns"]), ("script_direct", sc["script_direct"]), ("script_raw", g3["script_raw"])):
        dup = src.get("round1_duplicates", 0)
        scored[m] = [{"set": s["set"], "score": s["score"], "round": k} for s, k in zip(src["sets"], rounds_of(len(src["sets"]), dup))]
        best = max(src["sets"], key=lambda s: s["score"])
        assert abs(best["score"] - src["fit_score"]) < 1e-12 and sorted(best["set"]) == sorted(src["set"]), m
    assert rec2["fit_scores"]["script_columns"] == sc["script_columns"]["fit_score"]
    gp, cum = [], 0
    for s in g3["greedy"]["path"]:
        cum += s["scored"]
        gp.append({"step": s["step"], "added": s["added"], "score": s["score"], "cum": cum})
    assert cum == g3["greedy"]["scored"] == 1048 and abs(gp[-1]["score"] - f3["greedy"]["fit_score"]) < 1e-12
    sets = {"script_columns": sorted(sc["script_columns"]["set"]), "script_direct": sorted(sc["script_direct"]["set"]),
            "script_raw": sorted(f3["script_raw"]["set"]), "greedy": sorted(f3["greedy"]["set"])}
    fit = {"script_columns": sc["script_columns"]["fit_score"], "script_direct": sc["script_direct"]["fit_score"],
           "script_raw": f3["script_raw"]["fit_score"], "greedy": f3["greedy"]["fit_score"]}
    assert sets["greedy"] == sorted(g3["greedy"]["path"][-1]["set"])

    # ---- the frozen-rule differences, with AUDIT h2's independent task draws (10,000) beside the job's interval
    h2 = {iv["path"]: (r, iv) for r in ld(res / "audit_2026-11-12h2" / "h2_table.json")["rows"] for iv in r["intervals"]}
    sent = {r["sentence"]["path"]: r["sentence"] for r in ld(res / "audit_2026-11-12h2" / "h2_table.json")["rows"] if r.get("sentence")}
    A = lambda w: {i: (tabs[w]["agent_a"][i] + tabs[w]["agent_b"][i]) / 2 for i in tabs[w]["agent_a"]}   # noqa: E731

    def fav(x: dict, y: dict) -> tuple:
        d = [x[i] - y[i] for i in x]
        return sum(v > 0 for v in d), sum(v < 0 for v in d)

    spec = [("select_1", "A − ridge surrogate (the better search arm, no table)", "/select/strict/differences/surrogate", "/select/strict/A_vs_BB", "test", "A", "surrogate"),
            ("select_1", "A − gradient top 16", "/select/strict/differences/gradient_top16", "/select/strict/A_vs_gradient", "test", "A", "gradient_top16"),
            ("select_1", "A − direct-effect top 16", "/select/strict/differences/direct_top16", "/select/strict/A_vs_direct", "test", "A", "direct_top16"),
            ("select_2", "A − script with the same table (script_columns)", "/select2/strict/test/difference", "/select2/strict/test/A_vs_S", "test", "A", "script_columns"),
            ("select_2", "A − script with the same table (script_columns)", "/select2/strict/fresh/difference", "/select2/strict/fresh/A_vs_S", "fresh", "A", "script_columns"),
            ("select_2", "A − gradient top 16", "/select2/strict/fresh/gradient_difference", "/select2/strict/fresh/A_vs_gradient", "fresh", "A", "gradient_top16"),
            ("select_3", "greedy (1,048 scored sets) − A", "/select3/strict/test/greedy_minus_A", "/select3/strict/room", "test", "greedy", "A"),
            ("select_3", "greedy (1,048 scored sets) − A", "/select3/strict/fresh/greedy_minus_A", "/select3/strict/room", "fresh", "greedy", "A"),
            ("select_3", "A − script without the attention-change rankings (script_raw)", "/select3/strict/test/A_minus_raw", "/select3/strict/raw", "test", "A", "script_raw"),
            ("select_3", "A − script without the attention-change rankings (script_raw)", "/select3/strict/fresh/A_minus_raw", "/select3/strict/raw", "fresh", "A", "script_raw")]
    paired = []
    for run, lab, path, spath, which, x, y in spec:
        _, iv = h2[path]
        tx = A(which) if x == "A" else {i: float(v) for i, v in tabs[which][x].items()}
        ty = A(which) if y == "A" else {i: float(v) for i, v in tabs[which][y].items()}
        mean = sum(tx[i] - ty[i] for i in tx) / len(tx)
        assert abs(mean - iv["ind10000"]["mean"]) < 1e-9, (path, mean)
        s = sent[spath]
        fx, fy = fav(tx, ty)
        paired.append({"run": run, "label": lab, "list": which, "mean": mean, "lo": iv["ind10000"]["lo"], "hi": iv["ind10000"]["hi"],
                       "job_lo": iv["job"]["lo"], "job_hi": iv["job"]["hi"], "printed": s["job"], "independent": s["ind10000"], "fav_x": fx, "fav_y": fy})
    later_select = {"acc": acc, "scored": scored, "greedy": gp, "sets": sets, "fit": fit, "example": texts, "paired": paired,
                    "fresh_n": 80}

    # ---- route_1: Bolmo's attention weights apart from its values, on main, all 256 heads, at the deciding rows
    rm = ld(res / "route_1" / "metrics.json")["steps"]["results"]["route"]["all"]["strict"]
    rt = {"test": {}, "fresh": {}}
    for r in route:
        rt["test" if r["id"] in table["O"] else "fresh"].setdefault(r["condition"], {})[r["id"]] = bool(r["correct"])
    route_out = {"test": {}, "fresh": {}, "example": {}, "printed": {"re_routing": rm["re_routing"], "values": rm["values"]}}
    for which in ("test", "fresh"):
        for c in ("join", "w_only", "v_only", "none", "w_other"):
            want = [rm[which]["right"][c][t] for t in EDIT]
            if c in rt[which]:
                assert per(rt[which][c], edit_ids if which == "test" else fresh_ids) == want, (which, c)
            route_out[which][c] = {"right": sum(want), "per_task": want}
    assert route_out["test"]["join"]["right"] == 95 and route_out["test"]["none"]["right"] == 16 and route_out["fresh"]["none"]["right"] == 7
    for r in route:
        if r["id"] == ITEM:
            route_out["example"][r["condition"]] = {"generated": r["generated"], "correct": bool(r["correct"])}
    route_out["diffs"] = {k: rm["test"][k] for k in ("w1", "w2", "v1", "v2")} | {"fresh_" + k: rm["fresh"][k] for k in ("w1", "w2", "v1", "v2")}

    # ---- wire: host heads given one Bolmo head's attention weights, on H and on Pythia 1.4B
    def wire_reads(files: list, names: list, rowdir: Path) -> dict:
        """Counts from the study's result files; the per-item rows from S3, matched by spec index, recounted to the same numbers."""
        out, k = {}, 0
        for f in files:
            for e in ld(f):
                nm = names[k]
                k += 1
                d = e["decode"]
                right = d.get("right", round(d["strict"] * d["items"]))
                pt = [d["right_per_task"][t][0] for t in EDIT] if d.get("right_per_task") else None
                out.setdefault(nm, {})[d["list"]] = {"right": right, "items": d["items"], "per_task": pt, "rows": e.get("rows"), "n": e.get("n")}
        if rowdir is not None:
            got = defaultdict(list)
            for f in sorted(rowdir.glob("*.jsonl")):
                for r in rows(f):
                    got[(f.name, r["spec_index"])].append(r)
            for nm, lists in out.items():
                for lst, v in lists.items():
                    if not v["rows"]:
                        continue
                    fname = v["rows"].split("/")[-1]
                    cands = [rs for (fn, si), rs in got.items() if fn == fname and len(rs) == v["items"] and sum(x["strict"] for x in rs) == v["right"]
                             and (v["per_task"] is None or [sum(x["strict"] for x in rs if x["task"] == t) for t in EDIT] == v["per_task"])]
                    ex = {json.dumps([x["generated"] for x in rs if x["id"] == ITEM]) for rs in cands}
                    assert cands and len(ex) == 1, (nm, lst, len(cands))
                    hit = [x for x in cands[0] if x["id"] == ITEM]
                    if hit:
                        v["example"] = {"generated": hit[0]["generated"], "correct": bool(hit[0]["strict"])}
        for lists in out.values():
            for v in lists.values():
                v.pop("rows"), v.pop("n")
        return out

    W, P = res / "wire", res / "wire_pythia"
    h_reads = wire_reads([W / "reread_final5_test.json", W / "reread_final5_fresh.json", W / "reread_controls_test.json", W / "reread_controls_fresh.json"],
                         ["pairs_15+out_U", "pairs_15", "out_U", "host_alone", "direct_proc"] * 2 + ["pairs_15_from_S", "pairs_15_other_item"] * 2, new / "wire_h")
    first = {"test": ld(W / "final1_test.json"), "fresh": ld(W / "final1_fresh.json")}
    for lst, es in first.items():          # the first read gave the same counts (AUDIT i)
        for nm, e in zip(ld(W / "final1_names.json"), es):
            assert h_reads[nm][lst]["right"] == round(e["decode"]["strict"] * e["decode"]["items"]), (nm, lst)
    p_reads = wire_reads([P / "final_test.json", P / "final_fresh.json"], ld(P / "final_names.json") * 2, new / "wire_py")
    p_reads.update(wire_reads([P / "step33_final2_test.json", P / "step33_final2_fresh.json"], ["pairs_27", "pairs_27_from_S", "pairs_27_other_item"] * 2, None))
    p_reads.update(wire_reads([P / "step34_final1_test.json", P / "step34_final1_fresh.json"],
                              ["pairs_15+out_U_q", "pairs_15+out_U_q_from_S", "out_U_q", "pairs_15_again"] * 2, None))
    for lst in ("test", "fresh"):
        assert p_reads["pairs_15_again"][lst]["right"] == p_reads["pairs_15"][lst]["right"]
    p_reads.pop("pairs_15_again")
    aw = ld(res / "audit_2026-11-12i" / "audit_wire.json")
    f_alone = {"test": {"right": sum(table["F"][i] for i in edit_ids), "per_task": per(table["F"], edit_ids)},
               "fresh": {"right": aw["stored_runs"]["fresh | F alone"]["stored_right"], "per_task": [aw["stored_runs"]["fresh | F alone"]["per_task"][t] for t in EDIT]}}
    pf = [sum(r["correct"] for r in p1 if r["condition"] == "F" and r["id"] in fresh_by_task.get(r["task"], []) and r["task"] == t) for t in EDIT]
    assert pf == f_alone["fresh"]["per_task"]
    pairs = {"H": ld(W / "chosen_pairs_15.json"), "pythia": ld(P / "chosen_pairs_15.json")}
    g33 = ld(P / "step33_greedy2.json")
    cos = ld(W / "cosine_rule_select.json")
    cos_names = ld(W / "cosine_rule_names.json")
    sel_h = ld(W / "pairs_15_select.json")
    wire = {"H": {"reads": h_reads, "pairs": pairs["H"]}, "pythia": {"reads": p_reads, "pairs": pairs["pythia"], "pairs_27_added": g33},
            "f_alone": f_alone,
            "cosine": {nm: round(e["decode"]["strict"] * e["decode"]["items"]) for nm, e in zip(cos_names, cos)},
            "select_h": [(e["decode"].get("right", round(e["decode"]["strict"] * e["decode"]["items"]))) for e in sel_h]}
    assert wire["cosine"]["cosine_same15hosts_F_no_bos"] == 22 and wire["select_h"][0] == 57, (wire["cosine"], wire["select_h"])
    wire.update(build_latest(res, ld))
    print("later select test:", {m: v["right"] for m, v in acc["test"].items()})
    print("later select fresh:", {m: v["right"] for m, v in acc["fresh"].items()})
    print("route:", {w: {c: v["right"] for c, v in route_out[w].items()} for w in ("test", "fresh")})
    print("wire H:", {nm: {l: v["right"] for l, v in d.items()} for nm, d in h_reads.items()})
    print("wire pythia:", {nm: {l: v["right"] for l, v in d.items()} for nm, d in p_reads.items()})
    return {"later": later_select, "route": route_out, "wire": wire}


def build_latest(res: Path, ld) -> dict:
    """The runs of 2026-11-12 afternoon and evening: two more hosts (GRAFT step 38), the hand-made pointer (step 41), parts of the donor
    switched off (step 40), two tasks that are not copying (step 36) and a residual map (step 42). Counts from the study's result
    files, each checked against the number its journal entry prints."""
    def counts(folder: Path, names: list, lists=("test", "fresh"), stem="final_count") -> dict:
        out = {}
        for lst in lists:
            for nm, e in zip(names, ld(folder / f"{stem}_{lst}.json")):
                c = e["count"]
                out.setdefault(nm, {})[lst] = {k: c[k] for k in ("right", "items", "yes_written", "right_on_yes_golds", "right_on_no_golds") if k in c}
                out[nm][lst]["per_task"] = [c["right_per_task"][t][0] for t in EDIT] if set(EDIT) <= set(c["right_per_task"]) else None
        return out

    def check(reads: dict, want: dict):
        for nm, by_list in want.items():
            for lst, n in by_list.items():
                assert reads[nm][lst]["right"] == n, (nm, lst, reads[nm][lst]["right"], n)

    hosts = {}
    for key, folder, want in (("dscoder", "wire_dscoder", {"host_alone": {"test": 28, "fresh": 12}, "pairs_15": {"test": 70, "fresh": 36},
                                                            "pairs_15 from S": {"test": 26, "fresh": 10}, "pairs_15 other item": {"test": 5, "fresh": 0}}),
                              ("smollm2", "wire_smollm2", {"host_alone": {"test": 38, "fresh": 25}, "pairs_15": {"test": 86, "fresh": 42},
                                                           "pairs_15 from S": {"test": 43, "fresh": 20}, "pairs_15 other item": {"test": 12, "fresh": 6}})):
        f = res / folder
        reads = counts(f, ld(f / "final_names.json"))
        check(reads, want)
        hosts[key] = {"reads": reads, "pairs": ld(f / "chosen_pairs.json")}

    P = res / "wire_pythia"
    pointer = {}
    for key, stem in (("first", "step41_oracle"), ("fixed", "step41b_oracle")):
        nm = ld(P / f"{stem}_names.json")
        pointer[key] = {n: {"right": e["count"]["right"], "per_task": [e["count"]["right_per_task"][t][0] for t in EDIT]}
                        for n, e in zip(nm, ld(P / f"{stem}_select.json"))}
    assert [v["right"] for v in pointer["fixed"].values()] == [8, 50, 94, 60, 92] and [v["right"] for v in pointer["first"].values()] == [8, 50, 93, 60, 91]
    heads = [json.loads(line) for line in open(P / "step41b_oracle_heads.jsonl")]
    assert len(heads) == 384 and all(h["spec"][0]["donor"] == "oracle" and len(h["spec"][0]["pairs"]) == 1 for h in heads)
    seq = {(h["spec"][0]["pairs"][0][0], h["spec"][0]["pairs"][0][1]): h["seq"] for h in heads}
    assert abs(seq[(10, 9)] - 0.501) < 5e-4 and abs(seq[(10, 0)] - 0.390) < 5e-4
    p15 = [tuple(p[:2]) for p in ld(P / "chosen_pairs_15.json")]
    rank = {hd: k + 1 for k, hd in enumerate(sorted(seq, key=lambda x: -seq[x]))}
    assert sorted(rank[h] for h in p15)[:11] == list(range(1, 12)), sorted(rank[h] for h in p15)
    a = ld(P / "step40_A_right.json")
    off = {"clean": a["nothing off"], "heads": [a[f"heads of layer {L} (mean)"] for L in range(16)], "mlp": [a[f"mlp of layer {L} (mean)"] for L in range(16)]}
    assert off["clean"] == 14 and off["heads"][11:] == [12, 13, 14, 14, 14] and max(off["heads"][:11]) == 9 and off["mlp"][11] == 12
    cw = counts(res / "wire_h_contains_word", ld(res / "wire_h_contains_word" / "final_names.json"), ("select", "test", "fresh"))
    check(cw, {"host_alone": {"test": 22, "fresh": 8}, "pairs_7": {"test": 27, "fresh": 13}, "pairs_7 from S": {"test": 18}, "pairs_7 other item": {"test": 22}})
    sp = counts(res / "wire_h_spell", ld(res / "wire_h_spell" / "final_names.json"), ("select", "test", "fresh"))
    check(sp, {"host_alone": {"test": 46}, "pairs_10": {"test": 30}, "pairs_10 from S": {"test": 33}, "pairs_10 other item": {"test": 34}})
    site = counts(res / "site_h_contains_word", ld(res / "site_h_contains_word" / "final_names.json"))
    check(site, {"host alone": {"test": 22, "fresh": 8}, "resid 15 F-S -> resid 16 x1.0": {"test": 33, "fresh": 19},
                 "resid 15 F-S -> resid 16 x1.0 | S in F's place": {"test": 22, "fresh": 8}, "resid 15 F-S -> resid 16 x1.0 | another item": {"test": 23, "fresh": 11}})
    return {**hosts, "pointer": {"reads": pointer, "head_seq": [[L, h, seq[(L, h)]] for L in range(24) for h in range(16)], "search15": p15, "rank15": [rank[h] for h in p15]},
            "donor_off": off, "contains_word": cw, "spell": sp, "site": site}



if __name__ == "__main__":
    main(Path(sys.argv[1]))
