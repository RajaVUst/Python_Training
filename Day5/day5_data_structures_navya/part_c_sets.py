# Exercise 8 - De-duplicating Attendance
attendance = ["navya", "deepak", "navya", "varsha", "deepak", "hema"]
unique_attendees = set(attendance)
print(len(unique_attendees))
# Output: 4


# Exercise 9 - Common Interests
cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}

print(cohort_a & cohort_b)
print(cohort_a - cohort_b)
print(cohort_a | cohort_b)
# Output:
# {'python', 'excel'}
# {'sql'}
# {'python', 'sql', 'excel', 'tableau'}


# Exercise 10 - Fast Membership Check
seen = set(range(1000))

if 999 in seen:
    print("999 is in seen")
else:
    print("999 is not in seen")
# Output: 999 is in seen
# a set checks membership much faster than a list, especially for large collections