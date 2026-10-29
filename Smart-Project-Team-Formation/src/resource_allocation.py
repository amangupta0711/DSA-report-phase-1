"""Resource allocation DP - share R students among P projects for maximum profit.
dp[i][r] = best profit for the first i projects using r students.
Try every split k = 0..r for project i and remember the best k.   Time O(P*R^2)
"""

def allocate(profit, R):
    """profit[p][k] = profit of project p when given k students (k = 0..R)."""
    P = len(profit)
    dp = [[0] * (R + 1) for _ in range(P + 1)]
    choice = [[0] * (R + 1) for _ in range(P + 1)]
    for i in range(1, P + 1):
        for r in range(R + 1):
            for k in range(r + 1):
                val = dp[i - 1][r - k] + profit[i - 1][k]
                if val > dp[i][r]:
                    dp[i][r], choice[i][r] = val, k
    # rebuild the split
    split, r = [], R
    for i in range(P, 0, -1):
        split.append(choice[i][r]); r -= choice[i][r]
    split.reverse()
    return dp[P][R], split, dp
