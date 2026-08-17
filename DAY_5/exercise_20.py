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

roster = [
    {"name": "Amit",  "scores": [85, 90, 78]},
    {"name": "Reni",  "scores": [92, 95, 97]},
    {"name": "Tara",  "scores": [55, 60, 58]},
]

for entry in grade_summary(roster):
    print(f"{entry['name']}: average={entry['average']}, grade={entry['grade']}")
