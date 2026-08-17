data = [
    ("Amit", 85),
    ("Reni", 92),
    ("Tara", 78),
    ("Sam", 95)
]

top_scores = {
    name: score
    for name, score in data
    if score >= 90
}

print(top_scores)



#output:
'''{'Reni': 92, 'Sam': 95}'''