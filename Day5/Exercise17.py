
names = ["Amit", "Gokul", "Tara"]
scores = [78, 91, 65]
scores_dict = {name: score for name, score in zip(names, scores)}
print(scores_dict)

#output
# {'Amit': 78, 'Gokul': 91, 'Tara': 65}