temps = [15, 22, 31, 8, 27, 19]

labels = [
    "hot" if t >= 25 else ("mild" if t >= 15 else "cold")
    for t in temps
]

print(labels)


#output:
'''['mild', 'mild', 'hot', 'cold', 'hot', '
mild']'''