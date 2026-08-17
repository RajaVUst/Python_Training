names = ["Amit", "Reni", "Tara"]
scores = [78, 91, 65]

scores_dict = dict(zip(names, scores))
passed = {name: score for name, score in scores_dict.items() if score >= 70}

print(passed)


# OUTPUT
# {'Amit': 78, 'Reni': 91}