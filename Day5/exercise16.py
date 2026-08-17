temps = [15, 22, 31, 8, 27, 19]

labels = [
    "hot" if temperature >= 25
    else "mild" if temperature >= 15
    else "cold"
    for temperature in temps
]

print(labels)


'''
['mild', 'mild', 'hot', 'cold', 'hot', 'mild']

'''
