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
            "average": round(average, 1),
            "grade": grade
        })

    return result


roster = [
    {"name": "Amit", "scores": [85, 90, 88]},
    {"name": "Reni", "scores": [95, 92, 96]},
    {"name": "Tara", "scores": [65, 70, 68]}
]

result = grade_summary(roster)

print(result)



#output:
'''[{'name': 'Amit', 'average': 87.7, 'grade
': 'B'}, {'name': 'Reni', 'average': 94.3, 'grade': 'A'}, 
{'name': 'Tara', 'average': 67.7, 'grade': 'D'}]'''