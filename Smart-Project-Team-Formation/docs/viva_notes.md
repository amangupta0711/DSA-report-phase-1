# Viva Quick Notes

**Why DP for knapsack?** Same subproblems (first i tasks, w hours) repeat. Recursion would be O(2^n), the table makes it O(n x W).
**Why 0/1?** A task is either taken whole or skipped.
**How do you know which tasks were chosen?** If c[i][w] != c[i-1][w], task i was taken; subtract its hours and move up.
**LCS vs substring?** Subsequence need not be contiguous, but order is kept.
**LCS recurrence?** match: L[i-1][j-1]+1; else max(L[i-1][j], L[i][j-1]).
**Resource allocation complexity?** P projects x R students x up to R splits = O(P x R^2).
**DP vs Backtracking?** DP stores and reuses answers to overlapping subproblems (optimisation). Backtracking builds a solution step by step and undoes a step when a rule fails.
**What is pruning?** Cutting a branch early because it can never lead to a solution.
**Why does colouring need 3 slots?** T0, T1, T2 all clash with each other (a triangle), so 3 distinct colours are needed.
**Why were matrix chain, N-Queens, Hamiltonian, B&B not used?** The platform has no such problem (see concept_mapping.md).
**Limitations?** Dummy data, parts not yet joined with Month 1, backtracking is exponential in the worst case.
