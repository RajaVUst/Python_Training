cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}

print("Common skills:", cohort_a & cohort_b)
print("Skills unique to cohort_a:", cohort_a - cohort_b)
print("All skills:", cohort_a | cohort_b)

"""
OUTPUT:
Common skills: {'excel', 'python'}
Skills unique to cohort_a: {'sql'}
All skills: {'sql', 'tableau', 'excel', 'python'}
"""