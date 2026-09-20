---
name: math-study-orchestrator
description: Run one Chinese postgraduate Mathematics I study block with complete teaching, method selection, evidence-backed exercises, and durable project updates; use for daily study, chapter continuation, or deciding the next math task.
---

# Math Study Orchestrator

Use this skill only for the Mathematics I project at `/Users/apple/Documents/Anyka/BYG/math`. Do not manage 408, English, Politics, or unrelated BYG work.

## Start

1. Read `AGENTS.md`, `project-state.json`, `00-总览/当前状态.md`, `00-总览/总进度与今日看板.md`, and `00-总览/会话续接说明.md`.
2. Read the active daily plan and `06-测试与掌握度/复习队列.md`.
3. Report: total node coverage, independent evidence, delayed evidence, today's execution state, today's remaining scope, and the stop rule.
4. If today's time is unknown, do not invent a 60/90/180-minute completion claim; offer time-bounded options.

## Teaching shape

Prefer one coherent knowledge unit: concepts → why the method works → method-selection table → complete worked examples → one grouped exercise set → one grading pass. Do not turn every algebraic blank into a separate conversational round unless the learner asks for stepwise hints.

Before creating new exercises, compare against recent lectures and displayed answers. A question whose full solution was already shown is an example-reproduction exercise, not a new transfer test.

## Evidence

- Store original answers, prompt level, lecture visibility, hints, elapsed time, score, and linked node IDs.
- Separate core mathematical correctness from full correctness (`+C`, absolute values, coefficients, signs, bounds, and requested process).
- Keep G4/G3 chapter status conservative: a clean exercise block is not a whole-chapter pass.
- Finish by updating the daily record, node ledger/mirror, evidence log, queue, current state, and continuation note.

## Stop rule

A completed study block is not automatically the end of the whole day. Check the original daily plan and ask/observe whether another planned block remains. Do not append punishment exercises because a targeted test exposed an error; move unresolved work to the next queue.
