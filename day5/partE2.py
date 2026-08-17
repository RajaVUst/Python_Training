temps = [15, 22, 31, 8, 27, 19]

labels = [
    "hot" if temp >= 25 else "mild" if temp >= 15 else "cold"
    for temp in temps
]

print(labels)

# OUTPUT

# ['mild', 'mild', 'hot', 'cold', 'hot', 'mild']