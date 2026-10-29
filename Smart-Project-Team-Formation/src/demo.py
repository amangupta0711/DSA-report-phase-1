"""Smart Project Team Formation Platform - Month 2 demo (DP + Backtracking)."""
import sys
from knapsack import knapsack, print_table as kt
from lcs import lcs, print_table as lt
from resource_allocation import allocate
from subset_sum import subset_sum
from graph_coloring import graph_coloring, min_slots
import data

def hdr(t): print("\n" + "=" * 60 + f"\n {t}\n" + "=" * 60)

def part_knapsack():
    hdr("1. 0/1 KNAPSACK - choose tasks within hour limit (DP)")
    print("[Slide check] weights 2,3,4,5  values 3,4,5,6  W=5")
    b, ch, c = knapsack([("a", 2, 3), ("b", 3, 4), ("c", 4, 5), ("d", 5, 6)], 5)
    kt(c, 5); print(f"  Best value = {b}  (expected 7)")
    print("\n[Project data] 6 tasks, W = 30 hours")
    for n, h, p in data.TASKS: print(f"  {n:<14} {h:>2} h   priority {p}")
    b, ch, _ = knapsack(data.TASKS, 30)
    print(f"\n  Best priority = {b}")
    print("  Chosen tasks  = " + ", ".join(x[0] for x in ch))
    print(f"  Total hours   = {sum(x[1] for x in ch)}")

def part_lcs():
    hdr("2. LCS - common interests of two students (DP)")
    n, r, L = lcs("STONE", "LONGEST")
    print(f"[Slide check] STONE vs LONGEST -> length {n}  {''.join(r)}")
    n, r, L = lcs(data.STUDENT_A, data.STUDENT_B)
    print(f"\n  Student A: {data.STUDENT_A}\n  Student B: {data.STUDENT_B}\n")
    lt(data.STUDENT_A, data.STUDENT_B, L)
    print(f"\n  LCS length = {n}\n  Common interests (in order) = {r}")

def part_alloc():
    hdr("3. RESOURCE ALLOCATION - share 5 students among 3 projects (DP)")
    print("  profit table (rows = projects, cols = students 0..5)")
    for i, row in enumerate(data.PROFIT): print(f"   P{i}: {row}")
    best, split, dp = allocate(data.PROFIT, 5)
    print("\n  dp table (rows = first i projects, cols = r students)")
    for i, row in enumerate(dp): print(f"   i={i}: {row}")
    print(f"\n  Maximum profit = {best}\n  Split (P0,P1,P2) = {tuple(split)}")

def part_subset():
    hdr("4. SUBSET SUM - tasks adding to exact hours (Backtracking + pruning)")
    s, nodes = subset_sum([5, 7, 10, 13, 15, 20], 35)
    print(f"[Slide check] set [5,7,10,13,15,20], target 35 -> {len(s)} subsets")
    for x in s: print("    ", x)
    s, nodes = subset_sum(data.TASK_HOURS, 24)
    print(f"\n[Project data] task hours {data.TASK_HOURS}, target 24")
    for x in s: print("    ", x)
    print(f"  Nodes visited (with pruning) = {nodes}   (without pruning: {2**(len(data.TASK_HOURS)+1)-1})")

def part_color():
    hdr("5. GRAPH COLOURING - meeting slots for teams (Backtracking)")
    print(f"  Teams T0..T4, conflicts (shared student): {data.CONFLICTS}")
    print(f"  Try 2 slots -> {graph_coloring(data.TEAMS, data.CONFLICTS, 2)}  (T0,T1,T2 clash with each other)")
    m, sol = min_slots(data.TEAMS, data.CONFLICTS)
    print(f"  Minimum slots needed = {m}")
    for t, c in enumerate(sol): print(f"    T{t} -> Slot {c + 1}")

PARTS = {"1": part_knapsack, "2": part_lcs, "3": part_alloc, "4": part_subset, "5": part_color}

if __name__ == "__main__":
    for k in (sys.argv[1:] or PARTS):
        PARTS[k]()
