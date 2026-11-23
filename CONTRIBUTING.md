# Contributing

Thanks for helping. Your own work is welcome.

**Scope:** robotics work where composition or modularity is the main idea.

## Suggest a paper

[Open the suggestion form](https://github.com/compositional-robot/awesome-compositional-robot-learning/issues/new?template=add-paper.yml). A maintainer adds it for you.

## Add a paper yourself

Append one entry to [`data/papers.json`](data/papers.json) and open a pull request. Do not edit `README.md`: it is generated from the data, and both the README and the [website](https://compositional-robot.github.io/) update after your pull request is merged.

```json
{
  "title": "Paper title",
  "authors": "First Author, Second Author",
  "venue": "CoRL 2026",
  "year": 2026,
  "topics": ["modality"],
  "paper": "https://arxiv.org/abs/xxxx.xxxxx",
  "project": "https://project-page.github.io/",
  "code": "https://github.com/org/repo",
  "image": "images/papers/xxxx.xxxxx.jpg",
  "note": "One sentence on what is composed and how."
}
```

`project`, `code` and `image` are optional. Order in the file does not matter.

`topics` lists one or more of the ids below. The first one is the section the paper appears under in the README.

| id | Topic |
|---|---|
| `time` | Composing skills over time |
| `modality` | Composing modalities & policies |
| `constraints` | Composing constraints & objectives |
| `programs` | Programs & symbolic structure |
| `modular` | Modular architectures |
| `benchmarks` | Benchmarks & analysis |

For `image`, add a teaser figure to `images/papers/`, about 480 px wide and under 100 KB, named after the arXiv id.

## Check before opening the pull request

```bash
python3 scripts/validate.py
python3 scripts/build_readme.py   # optional: preview the README locally
```

The same checks run on every pull request.

## Preview the website locally

Clone this repository and [the website](https://github.com/compositional-robot/compositional-robot.github.io) side by side, then serve their parent folder:

```bash
python3 -m http.server 8000
# open http://localhost:8000/compositional-robot.github.io/
```
