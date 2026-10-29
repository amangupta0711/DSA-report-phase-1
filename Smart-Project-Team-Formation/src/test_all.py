"""Quick tests - run: python test_all.py"""
from knapsack import knapsack; from lcs import lcs
from resource_allocation import allocate; from subset_sum import subset_sum
from graph_coloring import graph_coloring, min_slots; import data
assert knapsack([("a",2,3),("b",3,4),("c",4,5),("d",5,6)],5)[0]==7
b,ch,_=knapsack(data.TASKS,30); assert b==23 and [x[0] for x in ch]==["Profile form","Matching","Dashboard"]
assert lcs("STONE","LONGEST")[0]==3
assert lcs(data.STUDENT_A,data.STUDENT_B)[1]==["web","design","db"]
assert allocate(data.PROFIT,5)[:2]==(11,[3,0,2])
assert len(subset_sum([5,7,10,13,15,20],35)[0])==4
assert sorted(subset_sum(data.TASK_HOURS,24)[0])==[[6,8,10],[10,14]]
assert graph_coloring(5,data.CONFLICTS,2) is None and min_slots(5,data.CONFLICTS)[0]==3
print("All tests passed")
