"""Dummy data only - no real student data is used."""
# (task, hours, priority)
TASKS = [("Profile form", 8, 6), ("Matching", 12, 10), ("Dashboard", 10, 7),
         ("Login", 14, 6), ("Notifications", 9, 4), ("Reports", 16, 7)]
STUDENT_A = ["python", "web", "ml", "design", "db"]
STUDENT_B = ["web", "design", "python", "db"]
# profit[project][k] = profit when project gets k students (k = 0..5)
PROFIT = [[0, 2, 3, 6, 7, 8],
          [0, 1, 2, 5, 6, 7],
          [0, 2, 5, 6, 7, 8]]
TASK_HOURS = [6, 8, 10, 14, 20]
TEAMS = 5
CONFLICTS = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4)]   # teams sharing a student
