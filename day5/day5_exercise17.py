names = ["Pranav", "Aron", "Lekhya", "Chaila"]
scores = [78, 91, 100, 80]

scores_dict = {
    name: score
    for name, score in zip(names, scores)
}

print(scores_dict)

"""
OUTPUT:
{'Pranav': 78, 'Aron': 91, 'Lekhya': 100, 'Chaila': 80}
"""