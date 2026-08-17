def grade_summary(roster):
    result = []

    for student in roster:
        name = student["name"]
        scores = student["scores"]

        average = sum(scores) / len(scores)

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

        result.append({
            "name": name,
            "average": average,
            "grade": grade
        })

    return result


# Roster of 3 students
roster = [
    {"name": "Yeshwanth", "scores": [85, 90, 88]},
    {"name": "Rahul", "scores": [72, 75, 70]},
    {"name": "Priya", "scores": [95, 92, 96]}
]

print(grade_summary(roster))
#output
"""
[{'name': 'Yeshwanth', 'average': 87.66666666666667, 'grade': 'B'}, {'name': 'Rahul', 'average': 72.33333333333333, 'grade': 'C'}, {'name': 'Priya', 'average': 94.33333333333333, 'grade': 'A'}]
"""