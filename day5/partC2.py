cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}

print(f"common skills:{cohort_a & cohort_b}")
print(f"skill unique to cohort_a:{cohort_a-cohort_b}")
print(f"combined:{cohort_b|cohort_a}")

# OUTPUT

# common skills:{'python', 'excel'}
# skill unique to cohort_a:{'sql'}
# combined:{'python', 'excel', 'tableau', 'sql'}