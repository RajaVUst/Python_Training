cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}

print("Common skills:", cohort_a & cohort_b)
print("Only in cohort_a:", cohort_a - cohort_b)
print("All skills:", cohort_a | cohort_b)

# output
# Common skills: {'excel', 'python'}
# Only in cohort_a: {'sql'}
# All skills: {'excel', 'tableau', 'python', 'sql'}