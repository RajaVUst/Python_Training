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
    {"name": "Amit", "scores": [85, 90, 88]},
    {"name": "Reni", "scores": [91, 95, 89]},
    {"name": "Tara", "scores": [65, 70, 68]}
]

print(grade_summary(roster))

# output:
# [{'name': 'Amit', 'average': 87.7, 'grade': 'B'}, 
# {'name': 'Reni', 'average': 91.7, 'grade': 'A'},
#  {'name': 'Tara', 'average': 67.7, 'grade': 'D'}]