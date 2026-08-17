#Common Interests
cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}

print("Common:", cohort_a & cohort_b)
print("Only in A:", cohort_a - cohort_b)
print("All skills:", cohort_a | cohort_b)


# Output:
# Common: {'python', 'excel'}
# Only in A: {'sql'}
# All skills: {'sql', 'python', 'excel', 'tableau'}