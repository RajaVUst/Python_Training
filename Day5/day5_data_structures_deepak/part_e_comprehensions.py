# Exercise 15 - Squares and Cubes
cubes = [n ** 3 for n in range(1, 11)]
even_cubes = [n ** 3 for n in range(1, 11) if n % 2 == 0]
 
print(cubes)
print(even_cubes)
# Output:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# [8, 64, 216, 512, 1000]
 
# Exercise 16 - Label the Temperatures
temps = [15, 22, 31, 8, 27, 19]
labels = ["hot" if t >= 25 else ("mild" if t >= 15 else "cold") for t in temps]
 
print(labels)
# Output:
# ['mild', 'mild', 'hot', 'cold', 'hot', 'mild']
 
# Exercise 17 - Dictionary From Two Lists
names = ["Navya", "Deepak", "Varsha"]
scores = [88, 91, 95]
 
name_scores = {name: score for name, score in zip(names, scores)}
print(name_scores)
# Output: {'Navya': 88, 'Deepak': 91, 'Varsha': 95}
 
# Exercise 18 - Filtering With a Dict Comprehension
passed_scores = {name: score for name, score in name_scores.items() if score >= 70}
print(passed_scores)
# Output: {'Navya': 88, 'Deepak': 91, 'Varsha': 95}