names = ["Aron", "Reni", "Pranav"]
scores = [78, 91, 65]

scores_dict = {
    name: score
    for name, score in zip(names, scores)
}

passing_scores = {
    name: score
    for name, score in scores_dict.items()
    if score >= 70
}

print(passing_scores)

"""
OUTPUT:
{'Aron': 78, 'Reni': 91}
"""