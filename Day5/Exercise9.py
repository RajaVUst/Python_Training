
cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}
print("Common:", cohort_a & cohort_b)
print("Unique to A:", cohort_a - cohort_b)
print("All skills:", cohort_a | cohort_b)

#output
# Common: {'excel', 'python'}
# Unique to A: {'sql'}
# All skills: {'sql', 'tableau', 'python', 'excel'}