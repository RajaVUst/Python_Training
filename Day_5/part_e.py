# Exercise 15: Squares and Cubes

cubes = [n ** 3 for n in range(1, 11)]
even_cubes = [n ** 3 for n in range(1, 11) if n % 2 == 0]

print("Cubes:", cubes)
print("Even Cubes:", even_cubes)


# Exercise 16: Label the Temperatures

temps = [15, 22, 31, 8, 27, 19]

labels = [
    "hot" if t >= 25 else ("mild" if t >= 15 else "cold")
    for t in temps
]

print("Exercise 16")
print("Temperatures:", temps)
print("Labels:", labels)


# Exercise 17: Dictionary From Two Lists

names = ["Jay", "Hee", "Dino"]
scores = [78, 91, 65]

scores_dict = {
    name: score
    for name, score in zip(names, scores)
}

print("Scores Dictionary:", scores_dict)

# Exercise 18: Filtering With a Dict Comprehension

passing_scores = {
    name: score
    for name, score in scores_dict.items()
    if score >= 70
}

print("Students with scores >= 70:", passing_scores)