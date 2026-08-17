def grade_summary(roster):
    result = []

    for i in roster:
        avg = sum(i["scores"]) / len(i["scores"])

        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        else:
            grade = "F"

        result.append({
            "name": i["name"],
            "average": avg,
            "grade": grade
        })

    return result


roster = [
    {"name": "Bonny", "scores": [50, 60, 70]},
    {"name": "Vinaya", "scores": [55, 66, 77]},
    {"name": "arjun", "scores": [56, 67, 78]}
]

print(grade_summary(roster))

# OUTPUT

# [{'name': 'Bonny', 'average': 60.0, 'grade': 'D'},
#  {'name': 'Vinaya', 'average': 66.0, 'grade': 'D'}
#  {'name': 'arjun', 'average': 67.0, 'grade': 'D'}]