# Exercise 15: Squares and Cubes

cube = [n ** 3 for n in range(1,11)]
print(f'cubes : {cube}')
even_cube = [n**3 for n in range (1,11) if n % 2 == 0]
print(f'even cubes {even_cube}')
# Output 
# cubes : [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# even cubes [8, 64, 216, 512, 1000]

# Excercise 16

temps = [15, 22, 31, 8, 27, 19]
labels = ['hot' if t >= 25 else ('mild' if t >= 15 else "cold")
for t in temps]
print(labels)

# output
# ['mild', 'mild', 'hot', 'cold', 'hot', 'mild']

# Excercise 17 

names = ["Amit", "Reni", "Tara"]
scores = [78, 91, 65]
score_dict = {name: score for name, score in zip(names, scores)}
print(score_dict)


# Exercise 18

score_dict = {"Amit": 78,"Reni": 91,"Tara": 65}
passing_scores = {name: score for name, score in score_dict.items()if score >= 70}
print(passing_scores)

# excercise 19

def vowel_counts(sentence):
    vowels = "aeiou"
    counts = {}
    for word in sentence.split():
        count = sum(1 for char in word.lower() if char in vowels)
        counts[word] = count
    return counts
result = vowel_counts("The Quick Brown Fox Jumps")
print(result)
# Output
# {'The': 1, 'Quick': 2, 'Brown': 1, 'Fox': 1, 'Jumps': 1}

# excercise 20

def grade_summary(roster):
    result = []

    for student in roster:
        average = sum(student["scores"]) / len(student["scores"])

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

        result.append({
            "name": student["name"],
            "average": round(average, 1),
            "grade": grade
        })

    return result
roster = [
    {"name": "Amit", "scores": [78, 82, 74]},{"name": "Reni", "scores": [91, 95, 87]},{"name": "Tara", "scores": [65, 70, 68]}]
print(grade_summary(roster))