# Redactions

The files in `docs/`, `build/`, `results/` and `study/` are copies of the study's files at commit 1a55d3e8a of its private working repository. A script (`studies/bytegraft/explainer/make_public.py` there) applied the rules below line by line, logged every replacement, and refused to finish if any searched pattern survived. 29 replacements in 2 files; no line was added or removed by a redaction. `study/JOURNAL_excerpt.md` holds whole entries of the study's journal, each marked with its line range there; the other copied files keep the study's line numbers.

The page was also changed where it names files: paths to files in this repository point here, files not published are named as not public, and the sources line lists what is here and what is not.

## Rules

| pattern class | replacement |
|---|---|
| S3 bucket name (contains the AWS account id) | `s3://<s3-bucket>` |
| S3 bucket name (contains the AWS account id) | `<s3-bucket>` |
| credential store parameter name | `<ssm-parameter>` |
| AWS profile name | `<aws-profile>` |
| local session scratchpad path | `<local-scratchpad>` |
| local absolute path containing the username | `<local>/` |
| EC2 instance id | `<instance>` |

## Edits that are not redactions

| file | line | what changed |
|---|---|---|
| `study/SCOREBOARD.md` | 3-7 | the owner's verbatim message paraphrased in two lines (lines 5 to 7 left empty so later line numbers match) |
| `study/SCOREBOARD.md` | 31 | DeepSeek-Coder row: 6 heads corrected to 7 (results/wire_dscoder/chosen_pairs.json holds 7 distinct Bolmo heads; JOURNAL.md lists seven) |

## Every redaction

| file | line | pattern class | replacement | count |
|---|---|---|---|---|
| `build/build_explainer_data.py` | 7 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `study/JOURNAL_excerpt.md` | 10 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 152 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 284 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 297 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 461 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 462 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 464 | S3 bucket name (contains the AWS account id) | `s3://<s3-bucket>` | 1 |
| `study/JOURNAL_excerpt.md` | 466 | S3 bucket name (contains the AWS account id) | `s3://<s3-bucket>` | 1 |
| `study/JOURNAL_excerpt.md` | 473 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 661 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 663 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 793 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 921 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 924 | EC2 instance id | `<instance>` | 2 |
| `study/JOURNAL_excerpt.md` | 990 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 993 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 1035 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 1037 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 1127 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 1225 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 1245 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 1252 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 1289 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 1306 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 1322 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 1351 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 1397 | EC2 instance id | `<instance>` | 1 |
| `study/JOURNAL_excerpt.md` | 1459 | EC2 instance id | `<instance>` | 1 |

## Added 2026-11-13: section 14

`results/ptr/` and `study/NOTES_ptr.md` are copies of `studies/bytegraft/results/ptr/` and `studies/bytegraft/NOTES_ptr.md` at commit 76180a711 of branch `research/ptr-install` in the private working repository. One rule was applied with `sed`: the S3 bucket name replaced by `<s3-bucket>`. 44 replacements in 16 files; no line added or removed. Section 14 of `docs/index.html` was written for this repository and has no private original.

| file | line | pattern class | replacement | count |
|---|---|---|---|---|
| `results/ptr/ptr_1.json` | 4 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_2.json` | 4 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_2.json` | 10 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_2.json` | 11 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_3b.json` | 4 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_3b.json` | 10 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_3b.json` | 11 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_4.json` | 4 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_4.json` | 10 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_4.json` | 11 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_5.json` | 4 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_5.json` | 10 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_5.json` | 11 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_6b.json` | 4 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_6b.json` | 10 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_6b.json` | 11 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_7b.json` | 4 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_7b.json` | 10 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_7b.json` | 11 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_8b.json` | 4 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_8b.json` | 10 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_8b.json` | 11 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_dscoder_2.json` | 4 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_dscoder_2.json` | 10 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_dscoder_2.json` | 11 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_dscoder_qk.json` | 4 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_dscoder_qk.json` | 10 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_dscoder_qk.json` | 11 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_pythia_qk.json` | 4 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_pythia_qk.json` | 10 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_pythia_qk.json` | 11 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_smollm2_1.json` | 4 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_smollm2_1.json` | 10 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_smollm2_1.json` | 11 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_smollm2_2.json` | 4 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_smollm2_2.json` | 10 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_smollm2_2.json` | 11 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_smollm2_3.json` | 4 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_smollm2_3.json` | 10 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_smollm2_3.json` | 11 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_smollm2_all12b.json` | 4 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_smollm2_all12b.json` | 10 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `results/ptr/ptr_smollm2_all12b.json` | 11 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
| `study/NOTES_ptr.md` | 7 | S3 bucket name (contains the AWS account id) | `<s3-bucket>` | 1 |
