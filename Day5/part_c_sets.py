# Part C: Sets

# Exercise 8: De-duplicating Attendance
attendance = ["amit", "reni", "amit", "tara", "reni", "sam"]
unique_attendees = set(attendance)
print("Unique Attendees:", unique_attendees)
print("Number of Unique Attendees:", len(unique_attendees))
# Output:
# Unique Attendees: {'amit', 'reni', 'tara', 'sam'}
# Number of Unique Attendees: 4
print("\n" + "="*40 + "\n")


# Exercise 9: Common Interests
cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}
print("Common Skills:", cohort_a & cohort_b)
print("Unique to Cohort A:", cohort_a - cohort_b)
print("All Skills:", cohort_a | cohort_b)
# Output:
# Common Skills: {'python', 'excel'}
# Unique to Cohort A: {'sql'}
# All Skills: {'python', 'sql', 'excel', 'tableau'}
print("\n" + "="*40 + "\n")


# Exercise 10: Fast Membership Check
seen = set(range(1000))
if 999 in seen:
    print("999 is present in the set.")
else:
    print("999 is not present in the set.")
# Output:
# 999 is present in the set.