# Exercise 11 - Contact Card
contact = {
    "name": "Deepak",
    "email": "deepak@email.com",
    "phone": "9751541641"
}
 
print(contact["name"])
print(contact["email"])
print(contact["phone"])
 
contact["city"] = "Salem"
contact["phone"] = "9751541641"
contact.pop("email")
 
print(contact)
# Output:
# Deepak
# deepak@email.com
# 9751541641
# {'name': 'Deepak', 'phone': '9751541641', 'city': 'Salem'}
 
# Exercise 12 - Word Frequency Counter
text = "the quick brown fox jumps over the lazy dog the fox runs"
words = text.split()
 
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
 
print(word_counts)
# Output:
# {'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1, 'runs': 1}
 
# Exercise 13 - Class Roster (Nested Structure)
roster = [
    {"name": "Navya", "scores": [85, 90, 78]},
    {"name": "Deepak", "scores": [70, 65, 80]},
    {"name": "Varsha", "scores": [92, 88, 95]}
]
 
for student in roster:
    average = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}: {round(average, 1)}")
# Output:
# Navya: 84.3
# Deepak: 71.7
# Varsha: 91.7 
 
# Exercise 14 - Lookup Table
grade_lookup = {"A": 90, "B": 75, "C": 60, "D": 40, "F": 0}
score = 84
 
for grade, threshold in grade_lookup.items():
    if score >= threshold:
        print(grade)
        break
# Output: B