def grade_summary(roster):
    summary = []

    for student in roster:
        average = sum(student["scores"]) / len(student["scores"])
        average = round(average, 1)

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

        result = {
            "name": student["name"],
            "average": average,
            "grade": grade
        }

        summary.append(result)

    return summary


roster = [
    {"name": "Amit", "scores": [78, 82, 80]},
    {"name": "Reni", "scores": [91, 89, 94]},
    {"name": "Tara", "scores": [65, 72, 70]}
]

print(grade_summary(roster))

'''
output
[{'name': 'Amit', 'average': 80.0, 'grade': 'B'}, 
{'name': 'Reni', 'average': 91.3, 'grade': 'A'}, 
{'name': 'Tara', 'average': 69.0, 'grade': 'D'}]

'''