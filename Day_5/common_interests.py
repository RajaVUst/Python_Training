cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}

print("Common skills:", cohort_a & cohort_b)
print("Unique to cohort A:", cohort_a - cohort_b)
print("All skills:", cohort_a | cohort_b)

# output:
# Common skills: {'excel', 'python'}
# Unique to cohort A: {'sql'}
# All skills: {'tableau', 'excel', 'python', 'sql'}