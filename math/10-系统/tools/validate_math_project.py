#!/usr/bin/env python3
"""Validate the durable invariants of the BYG Mathematics I project."""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=Path(__file__).resolve().parents[2], type=Path)
    args = ap.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    def read_json(rel):
        p = root / rel
        try: return json.loads(p.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"JSON {rel}: {exc}")
            return {}
    state = read_json("project-state.json")
    ledger = read_json("06-测试与掌握度/节点台账.json")
    nodes = ledger.get("nodes", [])
    ids = [n.get("id") for n in nodes]
    if len(ids) != 186: errors.append(f"expected 186 nodes, got {len(ids)}")
    if len(set(ids)) != len(ids): errors.append("duplicate node IDs")
    chapters = {c["id"]: c for c in state.get("chapters", []) if isinstance(c, dict) and "id" in c}
    for n in nodes:
        cid = str(n.get("id", "")).split(".")[0]
        if cid not in chapters: errors.append(f"node {n.get('id')} has no chapter")
        else:
            page = root / chapters[cid]["path"]
            text = page.read_text(encoding="utf-8") if page.exists() else ""
            row = f"| {n['id']} | {n['name']} | {n.get('priority', '')} | {n['state']} |"
            if row not in text: errors.append(f"mirror row missing: {n['id']}")
            if n.get("coverage_note") not in text: errors.append(f"coverage note missing: {n['id']}")
    # Forecast hashes must match and predictions must be frozen.
    for p in (root / "06-测试与掌握度/出题预测").glob("*事前预测.json"):
        h = p.with_name(p.stem.replace("-事前预测", "-预测锁定") + ".sha256")
        if h.exists() and hashlib.sha256(p.read_bytes()).hexdigest() != h.read_text().strip():
            errors.append(f"forecast hash mismatch: {p.name}")
    # Active links: accept project-relative, vault-relative, and unique stem links.
    md = {str(p.relative_to(root)): p for p in root.rglob("*.md") if "99-归档" not in p.parts}
    stems: dict[str, list[Path]] = {}
    for p in md.values(): stems.setdefault(p.stem, []).append(p)
    for p in md.values():
        for ref in re.findall(r"\[\[([^\]]+)\]\]", p.read_text(encoding="utf-8")):
            target = ref.split("|")[0].split("#")[0]
            if not target: continue
            path = target if target.endswith((".md", ".json")) else target + ".md"
            if not ((root / path).exists() or (p.parent / path).exists() or len(stems.get(target, [])) == 1):
                errors.append(f"missing link: {p.relative_to(root)} -> {target}")
    if errors:
        print("VALIDATION FAILED")
        print("\n".join(f"- {e}" for e in errors))
        return 1
    print(f"OK: math project; {len(nodes)} nodes; {len(md)} active markdown files; forecast hashes and mirrors valid")
    return 0

if __name__ == "__main__": sys.exit(main())
