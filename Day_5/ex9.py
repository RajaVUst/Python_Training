cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}

# Common skills
print("Common skills:", cohort_a & cohort_b)

# Skills unique to cohort_a
print("Unique to cohort_a:", cohort_a - cohort_b)

# All skills combined
print("All skills:", cohort_a | cohort_b)

# Output:
# Common skills: {'python', 'excel'}
# Unique to cohort_a: {'sql'}
# All skills: {'python', 'tableau', 'sql', 'excel'}