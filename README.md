# Problem Solving

A structured, multi-platform competitive programming and DSA practice repository.
Solutions are organized by source platform and algorithmic topic, with each file
containing problem metadata, a concise approach explanation, complexity analysis,
and runnable test cases.

## Platforms

- `leetcode/` — LeetCode solutions, grouped by topic
- `codeforces/` — Codeforces solutions, grouped by topic
- `neetcode/` — NeetCode patterns and curated problems
- `notes/` — Topic-wise notes, tricks, and revision material
- `template/` — Reusable boilerplate for fast local testing

## Structure

```
problem-solving/
├── leetcode/
│   ├── arrays-hashing/
│   ├── stack/
│   ├── linked-list/
│   ├── 1-d-dp/
│   ├── 2-d-dp/
│   ├── math-geometry/
│   └── ...
├── codeforces/
├── neetcode/
├── notes/
└── template/
```

## Solution Format

Every solution file follows a consistent layout:

- **Header docstring** — problem number, title, topic, difficulty, and link
- **Approach** — short bullet explanation of the strategy
- **Complexity** — time and space analysis
- **`__main__` block** — self-contained test cases that run locally

Example:

```bash
python leetcode/stack/503_next_greater_element_ii.py
```

## Conventions

- Filename: `<problem_number>_<slug>.py`
- One problem per file
- Prefer clean, readable logic over clever one-liners
- Include both brute-force and optimized versions where applicable

## Goals

- Build strong intuition for common patterns
- Maintain an organized, interview-ready reference
- Track progress across platforms

## Notes

Topic-wise revision notes for solved problems live in `notes/`, one file per topic:

- `notes/arrays-hashing.md`
- `notes/stack.md`
- `notes/linked-list.md`
- `notes/1-d-dp.md`
- `notes/2-d-dp.md`
- `notes/math-geometry.md`

Each note summarizes the pattern, key idea, edge cases, and complexity for the
corresponding solutions.

---

Happy grinding.
