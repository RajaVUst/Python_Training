scores_dict = {'Amit': 78,'Reni': 91,'Tara': 65}
passing_scores = {name: score for name, score in scores_dict.items() if score >= 70 }

print(passing_scores)

# Output:
# {'Amit': 78, 'Reni': 91}