# exercise 8 
attendance = ["amit", "reni", "amit", "tara", "reni", "sam"]
a = set(attendance)
print(a)
print(f'unique people attended: {len(a)}')
# output
# unique people attended: 4

# excercise 9
cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}

print(f'common to both cohort: {cohort_a.intersection(cohort_b)}')
print(f'skills unique to cohort a: {cohort_a.difference(cohort_b)}')
print(f'all skills combined: {cohort_a.union(cohort_b)}')

# Output

# unique people attended: 4
# common to both cohort: {'python', 'excel'}
# skills unique to cohort a: {'sql'}
# all skills combined: {'tableau', 'python', 'excel', 'sql'}

# Excercise 10

seen = set(range(1000))

if 999 in seen:
    print("999 is in the set.")
else:
    print("999 is not in the set.")

# Output
# 999 is in the set.

# excercise 11

contact = {"name": "Ren","email": "reni@example.com","phone": "1234567890"}
print("Name:", contact["name"])
print("Email:", contact["email"])
print("Phone:", contact["phone"])
contact["city"] = "Trivandrum"
contact["phone"] = "9876543210"
removed_email = contact.pop("email")
print("Updated contact:", contact)
print("Removed email:", removed_email)

# Output
# Name: Ren
# Email: reni@example.com
# Phone: 1234567890
# Updated contact: {'name': 'Ren', 'phone': '9876543210', 'city': 'Trivandrum'}
# Removed email: reni@example.com

# excercise 12

text = "the quick brown fox jumps over the lazy dog the fox runs"
words = text.split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)

# Output
#{'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1, 'runs': 1}

# excercise 13

roster = [{"name": "Reni", "scores": [85, 92, 88]},{"name": "Amit", "scores": [78, 81, 75]},{"name": "Tara", "scores": [90, 95, 93]}]
for student in roster:
    average = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}: {round(average, 1)}")
    # Output 
    # Reni: 88.3
    # Amit: 78.0
    # Tara: 92.7

    # excercise 14

grade_lookup = {"A": 90,"B": 80,"C": 70,"D": 60,"F": 0}
score = 84
for grade, threshold in grade_lookup.items():
    if score >= threshold:
        print(f"Score {score} earns a grade of {grade}")
        break