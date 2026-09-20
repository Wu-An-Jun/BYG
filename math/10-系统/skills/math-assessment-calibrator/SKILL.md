---
name: math-assessment-calibrator
description: Create, score, and audit Mathematics I assessments with frozen pre-answer probability forecasts, separate evidence, and no backfilled predictions; use for new questions, delayed review, grading, and forecast comparison.
---

# Math Assessment Calibrator

Use the Mathematics I project evidence rules. Never convert a few simple questions into a score or talent judgment.

## Before the learner answers

1. Assign a stable test and question ID.
2. Freeze the exact question, conditions, scoring points, linked node IDs, difficulty, risks, `p_core`, and `p_full` in `06-测试与掌握度/出题预测/`.
3. Show at least the full-correctness probability and explain that it is a rough subjective estimate, not a calibrated model.
4. Check whether the question or its complete solution appeared earlier. If yes, label it reproduction and exclude it from new-transfer calibration.

## After the learner answers

1. Preserve the raw answer exactly once; repeated LaTeX/rendered copies count once.
2. Score process and final answer separately. Use `core_correct` for the main mathematical method/result and `full_correct` for the requested complete answer.
3. Record unknown time as unknown, not zero. Record unattempted separately from wrong.
4. Write actual outcomes in a separate result file; never change the frozen prediction file.
5. Compare forecasts only when conditions are meaningfully comparable. Keep small-sample caveats.

## Grading boundaries

Do not double-penalize one omission. Distinguish method error, coefficient/sign error, condition error, algebra error, notation ambiguity, and missing completeness (`+C`, bounds, absolute value). If the prompt was ambiguous, ask or state the interpretation instead of inventing an error.

## Deliverables

Update the answer record, evidence log, node ledger and mirror, progress snapshot, forecast board, daily task state, and continuation note. If no new answer was provided, do not create a fake result.
