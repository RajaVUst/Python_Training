names = ["Amit", "Reni", "Tara"]
scores = [78, 91, 65]
scores_dict = {name: score for name, score in zip(names, scores)}
passed_students = {
    name: score
    for name, score in scores_dict.items()
    if score >= 70
}
print(passed_students)

# output
# {'Amit': 78, 'Reni': 91}