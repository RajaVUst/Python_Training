# Exercise 11: Contact Card

contact = {
    "name": "Jay park",
    "email": "jay@example.com",
    "phone": "98755543210"
}

print("Name :", contact["name"])
print("Email:", contact["email"])
print("Phone:", contact["phone"])

# Add a new key
contact["city"] = "Trivandrum"

# Update phone number
contact["phone"] = "9998887776"

# Remove email
contact.pop("email")

print("Updated Contact:", contact)


# Exercise 12: Word Frequency Counter

text = "the quick brown fox jumps over the lazy dog the fox runs"

word_counts = {}

for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)


# Exercise 13: Class Roster (Nested)

roster = [
    {"name": "Shua", "scores": [91, 88, 95]},
    {"name": "Hanie", "scores": [75, 80, 78]},
    {"name": "Coups", "scores": [85, 92, 89]}
]


for student in roster:
    average = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']} -> Average Score: {average:.1f}")



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