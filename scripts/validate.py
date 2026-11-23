"""Validate the files in data/. Run: python3 scripts/validate.py"""
import json
import re
import sys
from pathlib import Path

TOPICS = {"time", "modality", "constraints", "programs", "modular", "benchmarks"}
REQUIRED = ["title", "authors", "venue", "year", "topics", "paper", "note"]
ALLOWED = set(REQUIRED) | {"project", "code", "image"}

ROOT = Path(__file__).resolve().parent.parent
path = ROOT / "data" / "papers.json"
try:
    papers = json.loads(path.read_text(encoding="utf-8"))
except json.JSONDecodeError as e:
    sys.exit(f"papers.json is not valid JSON: {e}")

errors = []
seen = {}
for i, p in enumerate(papers):
    where = f"entry {i} ({p.get('title', 'no title')!r})"
    for k in REQUIRED:
        if not p.get(k):
            errors.append(f"{where}: missing '{k}'")
    for k in p:
        if k not in ALLOWED:
            errors.append(f"{where}: unknown field '{k}'")
    topics = p.get("topics")
    if topics is not None and (not isinstance(topics, list) or not topics or any(t not in TOPICS for t in topics)):
        errors.append(f"{where}: topics must be a non-empty list drawn from {sorted(TOPICS)}")
    if p.get("year") is not None and not (isinstance(p["year"], int) and 1950 <= p["year"] <= 2100):
        errors.append(f"{where}: year must be a number like 2026")
    for k in ("paper", "project", "code"):
        if k in p and not str(p[k]).startswith(("https://", "http://")):
            errors.append(f"{where}: '{k}' must start with https://")
    if "image" in p:
        img = str(p["image"])
        if not re.fullmatch(r"images/papers/[\w.-]+\.(jpe?g|png|webp|gif)", img, re.I):
            errors.append(f"{where}: image must be a file in images/papers/ (jpg, png, webp or gif)")
        elif not (ROOT / img).is_file():
            errors.append(f"{where}: image file {img} does not exist")
    key = p.get("paper")
    if key in seen:
        errors.append(f"{where}: same paper link as entry {seen[key]}")
    seen[key] = i

def check_list(name, required):
    try:
        items = json.loads((ROOT / "data" / name).read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append(f"{name} is not valid JSON: {e}")
        return []
    for i, item in enumerate(items):
        for k in required:
            if not item.get(k):
                errors.append(f"{name} entry {i}: missing '{k}'")
    return items


background = check_list("background.json", ["title", "authors", "venue", "year", "paper", "note"])
workshops = check_list("workshops.json", ["title", "url", "venue", "date", "location", "organizers", "speakers"])

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(papers)} papers, {len(background)} background, {len(workshops)} workshops")
