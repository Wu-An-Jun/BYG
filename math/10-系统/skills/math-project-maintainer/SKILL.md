---
name: math-project-maintainer
description: Maintain the durable BYG Mathematics I project, validate node mirrors and links, preserve evidence provenance, and synchronize only authorized math changes through the parent BYG Git repository.
---

# Math Project Maintainer

Project root: `/Users/apple/Documents/Anyka/BYG/math`. Git root: `/Users/apple/Documents/Anyka/BYG`. The math project has no nested Git repository.

## Canonical sources

- `project-state.json`: current machine state and workflow pointers.
- `06-测试与掌握度/节点台账.json`: authoritative node evidence/state.
- `06-测试与掌握度/作答记录/`: immutable answer records.
- `06-测试与掌握度/出题预测/`: frozen forecasts and separate outcomes.
- Markdown dashboards and chapter pages are readable mirrors, not a second source of truth.
- `99-归档/` is historical; compressed archives are ignored and must not be staged.

## Safe maintenance

1. Read local `AGENTS.md` and current state first.
2. Back up before a batch restructuring; never reset, clean, force-push, or rewrite history.
3. Preserve raw answers and source dates. Corrections append a correction note rather than deleting history.
4. Validate JSON, 186 node IDs, chapter-page mirrors, Obsidian links, forecast hashes, and ignored archive paths with `10-系统/tools/validate_math_project.py`.
5. Stage only math files belonging to the current task. Do not stage a root-level unrelated untracked file.
6. From the BYG root, commit with a focused message and push `origin/main`; verify local HEAD equals remote HEAD and report failure honestly.
