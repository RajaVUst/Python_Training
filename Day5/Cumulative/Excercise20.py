# Grade Book Summary

def grade_summary(roster):
    result = []
    for student in roster:
        average = sum(student["scores"]) / len(student["scores"])

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
            "name": student["name"],
            "average": round(average, 1),
            "grade": grade
        })

    return result

roster = [
    {"name": "Rohit", "scores": [80, 90, 85]},
    {"name": "Logesh", "scores": [95, 92, 90]},
    {"name": "Dev", "scores": [60, 65, 70]}
]

print(grade_summary(roster))


# Output:
# [{'name': 'Rohit', 'average': 85.0, 'grade': 'B'}, {'name': 'Logesh', 'average': 92.3, 'grade': 'A'}, {'name': 'Dev', 'average': 65.0, 'grade': 'D'}]