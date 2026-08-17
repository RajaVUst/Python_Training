names = ["Amit", "Reni", "Tara"]
scores = [78, 91, 65]

scores_dict = {name: score for name, score in zip(names, scores)}

print(scores_dict)

"""
Output->
{'Amit': 78, 'Reni': 91, 'Tara': 65}
"""