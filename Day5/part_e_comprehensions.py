# Part E: Comprehensions

# Exercise 15: Squares and Cubes
cubes = [n ** 3 for n in range(1, 11)]
even_cubes = [n ** 3 for n in range(1, 11) if n % 2 == 0]
print("Cubes:", cubes)
print("Even Cubes:", even_cubes)
# Output:
# Cubes: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# Even Cubes: [8, 64, 216, 512, 1000]
print("\n" + "="*40 + "\n")


# Exercise 16: Label the Temperatures
temps = [15, 22, 31, 8, 27, 19]
labels = [
    "hot" if t >= 25 else ("mild" if t >= 15 else "cold")
    for t in temps
]
print("Temperatures:", temps)
print("Labels:", labels)
# Output:
# Temperatures: [15, 22, 31, 8, 27, 19]
# Labels: ['mild', 'mild', 'hot', 'cold', 'hot', 'mild']
print("\n" + "="*40 + "\n")


# Exercise 17: Dictionary From Two Lists
names = ["Amit", "Varsha", "Tara"]
scores = [78, 91, 65]
scores_dict = dict(zip(names, scores))
print(scores_dict)
# Output:
# {'Amit': 78, 'Varsha': 91, 'Tara': 65}
print("\n" + "="*40 + "\n")


# Exercise 18: Filtering With a Dict Comprehension
passing_scores = {
    name: score
    for name, score in scores_dict.items()
    if score >= 70
}
print(passing_scores)
# Output:
# {'Amit': 78, 'varsha': 91}