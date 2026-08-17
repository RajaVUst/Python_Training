# Exercise 8: De-duplicating Attendance

attendance = ["amit", "reni", "amit", "tara", "reni", "sam"]

unique_attendees = set(attendance)

print("Unique attendees:", unique_attendees)
print("Number of unique attendees:", len(unique_attendees))


# Exercise 9: Common Interests

cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}

common_skills = cohort_a & cohort_b
unique_to_a = cohort_a - cohort_b
all_skills = cohort_a | cohort_b

print("Common skills:", common_skills)
print("Unique to Cohort A:", unique_to_a)
print("All skills:", all_skills)


# Exercise 10: Membership Check

seen = set(range(1000))
if 999 in seen:
    print("999 is present in the set.")
else:
    print("999 is not present in the set.")
