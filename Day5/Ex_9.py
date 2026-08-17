cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}
print(cohort_a.union(cohort_b))
print(cohort_a.intersection(cohort_b))
print(cohort_a.difference(cohort_b),cohort_b.difference(cohort_a))
#output
"""
{'excel', 'sql', 'tableau', 'python'}
{'excel', 'python'}
{'sql'} {'tableau'}
"""