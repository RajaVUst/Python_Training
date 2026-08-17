roster = [
    {"name": "Amit", "scores": [80, 90, 70]},
    {"name": "Gokul", "scores": [95, 91, 88]},
    {"name": "Tara", "scores": [60, 75, 82]},
]

def grade_summary(roster):
    result = []
    for student in roster:
        avg = sum(student["scores"]) / len(student["scores"])
        if avg >= 90:
            letter = "A"
        elif avg >= 80:
            letter = "B"
        elif avg >= 70:
            letter = "C"
        elif avg >= 60:
            letter = "D"
        else:
            letter = "F"
        result.append({"name": student["name"], "average": round(avg, 1), "grade": letter})
    return result

print(grade_summary(roster))

#output
# [{'name': 'Amit', 'average': 80.0, 'grade': 'B'},{'name': 'Gokul', 'average': 91.3, 'grade': 'A'},{'name': 'Tara', 'average': 72.3, 'grade': 'C'}]