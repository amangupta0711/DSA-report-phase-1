# Design Decisions
- **Knapsack:** the full table c[i][w] is kept (not one row) so the chosen tasks can be found by walking back.
- **LCS:** on a tie the traceback goes up first, so the output is the same every time.
- **Resource allocation:** all splits k = 0..r are tried; the best k is stored in `choice` to rebuild the split.
- **Subset sum:** tasks are sorted; a branch is dropped if sum > target or sum + remaining < target (47 nodes visited instead of 63 on the dummy data).
- **Graph colouring:** first allowed slot is given; if none works, go back. `min_slots` tries 1, 2, 3 ... slots.
