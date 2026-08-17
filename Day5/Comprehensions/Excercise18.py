# Filtering With a Dict Comprehension

scores_dict = {
    "Logesh": 78,
    "Rohit": 91,
    "Dev": 65
}
passed_students = {
    name: score
    for name, score in scores_dict.items()
    if score >= 70
}
print(passed_students)


# Output:
# {'Logesh': 78, 'Rohit': 91}