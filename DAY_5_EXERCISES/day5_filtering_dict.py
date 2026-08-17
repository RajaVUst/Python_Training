names = ["Amit", "Reni", "Tara"]
scores = [78, 91, 65]

scores_dict = {name: score for name, score in zip(names, scores)}

passing_scores = {
    name: score
    for name, score in scores_dict.items()
    if score >= 70
}

print("All scores:", scores_dict)
print("Scores >= 70:", passing_scores)

"""
All scores: {'Amit': 78, 'Reni': 91, 'Tara': 65}
Scores >= 70: {'Amit': 78, 'Reni': 91}
"""