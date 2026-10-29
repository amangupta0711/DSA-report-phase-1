"""Longest Common Subsequence - common interests of two students.
If items match: diagonal + 1, else max(left, up).   Time O(m*n)
Tie rule: go UP first, so output is always the same.
"""

def lcs(a, b):
    m, n = len(a), len(b)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    # traceback
    res, i, j = [], m, n
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            res.append(a[i - 1]); i -= 1; j -= 1
        elif L[i - 1][j] >= L[i][j - 1]:               # tie -> go up
            i -= 1
        else:
            j -= 1
    res.reverse()
    return L[m][n], res, L


def print_table(a, b, L):
    print("        " + "  ".join(f"{str(x)[:3]:>3}" for x in ["-"] + list(b)))
    for i, row in enumerate(L):
        lab = "-" if i == 0 else str(a[i - 1])[:3]
        print(f"  {lab:>3}   " + "  ".join(f"{v:>3}" for v in row))
