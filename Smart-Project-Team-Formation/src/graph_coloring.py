"""Graph Colouring (backtracking) - give meeting slots to teams so that
teams sharing a student never get the same slot. Colour = slot.
Each team gets the first allowed slot; if none works, go back.
"""

def graph_coloring(n, edges, m):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    color = [-1] * n

    def safe(v, c):
        return all(color[u] != c for u in adj[v])

    def bt(v):
        if v == n:
            return True
        for c in range(m):
            if safe(v, c):
                color[v] = c
                if bt(v + 1):
                    return True
                color[v] = -1                           # go back
        return False

    return (color[:] if bt(0) else None)


def min_slots(n, edges):
    for m in range(1, n + 1):
        sol = graph_coloring(n, edges, m)
        if sol:
            return m, sol
