names = ["Amit", "Reni", "Tara"]
scores = [78, 91, 65]

scores_dict = {name: score for name, score in zip(names, scores)}

passing = {name: score for name, score in scores_dict.items() if score >= 70}

print("All scores:", scores_dict)
print("Scores >= 70:", passing)
