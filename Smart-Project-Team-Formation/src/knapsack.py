"""0/1 Knapsack with traceback - pick project tasks within an hour limit.
c[i][w] = best priority using the first i tasks in w hours.   Time O(n*W), Space O(n*W)
"""

def knapsack(tasks, W, verbose=False):
    """tasks: list of (name, hours, priority). Returns (best, chosen, table)."""
    n = len(tasks)
    c = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        _, hrs, pri = tasks[i - 1]
        for w in range(W + 1):
            c[i][w] = c[i - 1][w]                      # skip task i
            if hrs <= w:                                # take task i
                c[i][w] = max(c[i][w], c[i - 1][w - hrs] + pri)
    # traceback: walk back from last cell (whole table is kept for this)
    chosen, w = [], W
    for i in range(n, 0, -1):
        if c[i][w] != c[i - 1][w]:                      # value changed -> task i taken
            chosen.append(tasks[i - 1])
            w -= tasks[i - 1][1]
    chosen.reverse()
    return c[n][W], chosen, c


def print_table(c, W):
    print("      w: " + " ".join(f"{w:>2}" for w in range(W + 1)))
    for i, row in enumerate(c):
        print(f"  i={i}:   " + " ".join(f"{v:>2}" for v in row))
