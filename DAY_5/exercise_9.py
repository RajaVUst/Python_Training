cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}

print("Common skills:", cohort_a & cohort_b)
print("Unique to cohort_a:", cohort_a - cohort_b)
print("All skills combined:", cohort_a | cohort_b)
