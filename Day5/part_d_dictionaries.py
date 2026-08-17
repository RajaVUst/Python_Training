# Part D: Dictionaries & Nested Structures

# Exercise 11: Contact Card
contact = {
    "name": "Varsha",
    "email": "varsha@example.com",
    "phone": "9876543210"
}
print("Name:", contact["name"])
print("Email:", contact["email"])
print("Phone:", contact["phone"])
contact["city"] = "Hyderabad"
contact["phone"] = "9998887776"
contact.pop("email")
print("Updated Contact:", contact)
# Output:
# Name: Varsha
# Email: varsha@example.com
# Phone: 9876543210
# Updated Contact:
# {'name': 'Varsha', 'phone': '9998887776', 'city': 'Hyderabad'}
print("\n" + "="*40 + "\n")


# Exercise 12: Word Frequency Counter
text = "the quick brown fox jumps over the lazy dog the fox runs"
word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)
# Output:
# {'the': 3, 'quick': 1, 'brown': 1, 'fox': 2,
#  'jumps': 1, 'over': 1, 'lazy': 1,
#  'dog': 1, 'runs': 1}
print("\n" + "="*40 + "\n")


# Exercise 13: Class Roster (Nested Structure)
roster = [
    {"name": "Amit", "scores": [85, 90, 88]},
    {"name": "Varsha", "scores": [92, 95, 89]},
    {"name": "Tara", "scores": [78, 82, 80]}
]
for student in roster:
    average = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']} - Average Score: {round(average, 1)}")
# Output:
# Amit - Average Score: 87.7
# Varsha - Average Score: 92.0
# Tara - Average Score: 80.0
print("\n" + "="*40 + "\n")


# Exercise 14: Lookup Table
grade_lookup = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60,
    "F": 0
}
score = 84
print("Score:", score)
for grade, threshold in grade_lookup.items():
    if score >= threshold:
        print("Grade:", grade)
        break

# 