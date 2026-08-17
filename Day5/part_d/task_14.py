grade_lookup = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60,
    "F": 0
}

score = 90

if score >= grade_lookup["A"]:
    grade = "A"
elif score >= grade_lookup["B"]:
    grade = "B"
elif score >= grade_lookup["C"]:
    grade = "C"
elif score >= grade_lookup["D"]:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

# Grade: A