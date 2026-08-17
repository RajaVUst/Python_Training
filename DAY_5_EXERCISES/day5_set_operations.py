cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}

print("Common skills:", cohort_a & cohort_b)
print("Unique to cohort_a:", cohort_a - cohort_b)
print("All skills:", cohort_a | cohort_b)

"""
Output->
Common skills: {'excel', 'python'}
Unique to cohort_a: {'sql'}
All skills: {'python', 'tableau', 'sql', 'excel'}
"""