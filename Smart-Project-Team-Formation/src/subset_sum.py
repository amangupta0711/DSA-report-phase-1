"""Subset Sum (backtracking with pruning) - tasks whose hours add up exactly to a target.
Tasks are sorted. Include/skip each task. Prune a branch when
  (1) current sum > target, or (2) current sum + remaining < target.
"""

def subset_sum(tasks, target):
    tasks = sorted(tasks)
    suffix = [0] * (len(tasks) + 1)                   # suffix[i] = sum of tasks[i:]
    for i in range(len(tasks) - 1, -1, -1):
        suffix[i] = suffix[i + 1] + tasks[i]
    results, nodes = [], [0]

    def bt(i, cur, total):
        nodes[0] += 1
        if total == target:
            results.append(list(cur)); return
        if i == len(tasks) or total > target or total + suffix[i] < target:
            return                                      # prune
        cur.append(tasks[i])                            # include
        bt(i + 1, cur, total + tasks[i])
        cur.pop()                                       # go back
        bt(i + 1, cur, total)                           # skip

    bt(0, [], 0)
    return results, nodes[0]
