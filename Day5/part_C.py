# Exercise 8: De-duplicating Attendance
attendance = ["amit","reni","amit","tara","reni","sam"]
unique = set(attendance)
print(len(unique))      # 4

# Exercise 9: Common Interests
cohort_a = {"python","sql","excel"}
cohort_b = {"python","tableau","excel"}
print("Skills common",cohort_a & cohort_b)      # Skills common {'excel', 'python'}
print("Unique Skills", cohort_a - cohort_b)     # Unique Skills {'sql'}
print("Combined Skills", cohort_a | cohort_b)   # Combined Skills {'sql', 'excel', 'python', 'tableau'}

# Exercise 10: Fast Membership Check
seen = set(range(1000))
check = 999 in seen;
if check:                               # Output
    print("999 is present in set")      # 999 is present in set
else:
    print("Not present")