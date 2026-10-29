# Smart Project Team Formation Platform

| | |
|---|---|
| **Course** | Data Structure and Algorithms - II (CCSE0301) |
| **Faculty** | Mr. Shamshad Ali |
| **Student** | Aman Gupta (Roll No. 2501330100053), B.Tech CSE-A |
| **Type** | Individual PBL Assignment |
| **SDG** | SDG 4 - Quality Education |

## About
A prototype for a student project-team platform that picks tasks, finds common interests,
shares students among projects and schedules meeting slots using Dynamic Programming and
Backtracking. Only dummy data is used.

## Current Status
- **Review 1 (Month 1):** Problem understanding and concept study.
- **Review 2 (Month 2):** Unit 3 (DP) and Unit 4 (Backtracking) parts designed and implemented in Python, with a demo and tests.
- **Next:** Join with Month 1 structures (AVL tree, graph, heap) into one flow, real compatibility score, larger test data, complexity analysis.

## Algorithms Used
| Requirement | Technique | Complexity | File |
|---|---|---|---|
| Choose tasks within an hour limit | 0/1 Knapsack (DP) + traceback | O(n x W) | `src/knapsack.py` |
| Common interests of two students | Longest Common Subsequence (DP) | O(m x n) | `src/lcs.py` |
| Share students among projects | Resource Allocation (DP) | O(P x R^2) | `src/resource_allocation.py` |
| Tasks that add up to exact hours | Subset Sum (Backtracking + pruning) | O(2^n) worst case | `src/subset_sum.py` |
| Meeting slots without clashes | Graph Colouring (Backtracking) | O(m^V) worst case | `src/graph_coloring.py` |

Matrix chain, N-Queens, Hamiltonian cycle and branch and bound were studied but marked "not used"
(see `docs/concept_mapping.md`).

## How to Run
Requires Python 3. No external libraries are needed.

```bash
cd src
python demo.py          # all five parts
python demo.py 1        # one part only (1 = knapsack ... 5 = graph colouring)
python test_all.py      # slide examples + project data checks
```
(`make_screenshots.py` needs Pillow and only regenerates the images.)

## Results
| Part | Result |
|---|---|
| Knapsack | 6 tasks, 30 h -> priority **23** (Profile form, Matching, Dashboard = 30 h). Slide example W=5 -> 7 |
| LCS | Interests lists -> length **3** (web, design, db). STONE / LONGEST -> 3 |
| Resource allocation | 5 students, 3 projects -> max profit **11**, split **3, 0, 2** |
| Subset sum | Target 24 -> {6,8,10}, {10,14}. Slide example 35 -> 4 subsets |
| Graph colouring | 5 teams, 5 conflicts -> **3 slots** (2 fail as T0,T1,T2 clash) |

## Repository Contents
- `src/` - source code, demo and tests
- `docs/` - concept mapping, design decisions, viva notes
- `research/` - research papers referred to
- `screenshots/` - output screenshots for Review 2
