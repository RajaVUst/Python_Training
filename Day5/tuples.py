#------------EXERCISE 5---------------
# location = (12.97, 77.59)
# location[0]=(13.00)
# print(location)

# Error: TypeError: 'tuple' object does not support item assignment because tuples are immutable.

#------------EXERCISE 6---------------

record = ("Reni", 91, "Cohort 2")
name, score, cohort = record
print(f"{name} scored {score} marks and belongs to {cohort}.")

#--------------EXERCISE 7-23--------------

# Exercise 7: Min, Max, Average
def stats(numbers):
    low = min(numbers)
    high = max(numbers)
    avg = sum(numbers) / len(numbers)
    return low, high, avg

low, high, avg = stats([4, 9, 1, 7, 15])
print(low, high, avg)
# Output: 1 15 7.2


# Exercise 8: De-duplicating Attendance
attendance = ["amit", "reni", "amit", "tara", "reni", "sam"]
unique_attendees = set(attendance)
print(unique_attendees)
# Output: {'amit', 'sam', 'tara', 'reni'}   (set order can vary)
print(len(unique_attendees))
# Output: 4


# Exercise 9: Common Interests
cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}
print(cohort_a & cohort_b)
# Output: {'excel', 'python'}
print(cohort_a - cohort_b)
# Output: {'sql'}
print(cohort_a | cohort_b)
# Output: {'sql', 'tableau', 'excel', 'python'}


# Exercise 10: Fast Membership Check
seen = set(range(1000))
if 999 in seen:
    print("999 is in seen")
else:
    print("999 is not in seen")
# Output: 999 is in seen
# A set is faster than a list here because membership checks are O(1)
# on average (hash lookup), while a list needs an O(n) linear scan.


# Exercise 11: Contact Card
contact = {"name": "Amit", "email": "amit@example.com", "phone": "9876543210"}
print(contact["name"])
# Output: Amit
print(contact["email"])
# Output: amit@example.com
print(contact["phone"])
# Output: 9876543210

contact["city"] = "Bangalore"
contact["phone"] = "9123456780"
contact.pop("email")
print(contact)
# Output: {'name': 'Amit', 'phone': '9123456780', 'city': 'Bangalore'}


# Exercise 12: Word Frequency Counter
text = "the quick brown fox jumps over the lazy dog the fox runs"
word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)
# Output: {'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1, 'runs': 1}


# Exercise 13: Class Roster (Nested Structure)
roster = [
    {"name": "Amit", "scores": [80, 90, 70]},
    {"name": "Reni", "scores": [60, 75, 85]},
    {"name": "Tara", "scores": [95, 88, 92]},
]
for student in roster:
    average = sum(student["scores"]) / len(student["scores"])
    print(student["name"], round(average, 1))
# Output:
# Amit 80.0
# Reni 73.3
# Tara 91.7


# Exercise 14: Lookup Table
grade_lookup = {"A": 90, "B": 80, "C": 70, "D": 60, "F": 0}
score = 84
for letter, threshold in sorted(grade_lookup.items(), key=lambda item: item[1], reverse=True):
    if score >= threshold:
        print(letter)
        break
# Output: B


# Exercise 15: Squares and Cubes
cubes = [n ** 3 for n in range(1, 11)]
print(cubes)
# Output: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

even_cubes = [n ** 3 for n in range(1, 11) if n % 2 == 0]
print(even_cubes)
# Output: [8, 64, 216, 512, 1000]


# Exercise 16: Label the Temperatures
temps = [15, 22, 31, 8, 27, 19]
labels = ["hot" if t >= 25 else ("mild" if t >= 15 else "cold") for t in temps]
print(labels)
# Output: ['mild', 'mild', 'hot', 'cold', 'hot', 'mild']


# Exercise 17: Dictionary From Two Lists
names = ["Amit", "Reni", "Tara"]
scores = [78, 91, 65]
name_to_score = {name: score for name, score in zip(names, scores)}
print(name_to_score)
# Output: {'Amit': 78, 'Reni': 91, 'Tara': 65}


# Exercise 18: Filtering With a Dict Comprehension
passing_scores = {name: score for name, score in name_to_score.items() if score >= 70}
print(passing_scores)
# Output: {'Amit': 78, 'Reni': 91}


# Exercise 19: Vowel Counter by Word
def vowel_counts(sentence):
    vowels = "aeiou"
    return {word: sum(1 for ch in word.lower() if ch in vowels) for word in sentence.split()}

print(vowel_counts("The Quick Brown Fox Jumps"))
# Output: {'The': 1, 'Quick': 2, 'Brown': 1, 'Fox': 1, 'Jumps': 1}


# Exercise 20: Grade Book Summary
def grade_summary(roster):
    result = []
    for student in roster:
        average = sum(student["scores"]) / len(student["scores"])
        if average >= 90:
            letter = "A"
        elif average >= 80:
            letter = "B"
        elif average >= 70:
            letter = "C"
        elif average >= 60:
            letter = "D"
        else:
            letter = "F"
        result.append({"name": student["name"], "average": round(average, 1), "grade": letter})
    return result

print(grade_summary(roster))
# Output: [{'name': 'Amit', 'average': 80.0, 'grade': 'B'}, {'name': 'Reni', 'average': 73.3, 'grade': 'C'}, {'name': 'Tara', 'average': 91.7, 'grade': 'A'}]


# Exercise 21: Unique Word Finder
def unique_words(text):
    words = {word.lower() for word in text.split()}
    return sorted(words)

print(unique_words("The cat sat on the mat and the cat slept"))
# Output: ['and', 'cat', 'mat', 'on', 'sat', 'slept', 'the']


# Exercise 22: FizzBuzz, Structured
def fizzbuzz_map(n):
    result = {}
    for i in range(1, n + 1):
        if i % 15 == 0:
            result[i] = "FizzBuzz"
        elif i % 3 == 0:
            result[i] = "Fizz"
        elif i % 5 == 0:
            result[i] = "Buzz"
        else:
            result[i] = str(i)
    return result

print(fizzbuzz_map(20))
# Output: {1: '1', 2: '2', 3: 'Fizz', 4: '4', 5: 'Buzz', 6: 'Fizz', 7: '7', 8: '8', 9: 'Fizz', 10: 'Buzz', 11: '11', 12: 'Fizz', 13: '13', 14: '14', 15: 'FizzBuzz', 16: '16', 17: '17', 18: 'Fizz', 19: '19', 20: 'Buzz'}


# Exercise 23: Password Strength Report (Capstone)
def password_report(passwords):
    report = {"weak": [], "medium": [], "strong": []}
    for pw in passwords:
        has_digit = any(ch.isdigit() for ch in pw)
        if len(pw) < 6:
            report["weak"].append(pw)
        elif len(pw) >= 10 and has_digit:
            report["strong"].append(pw)
        else:
            report["medium"].append(pw)
    return report

sample_passwords = ["abc", "password", "Str0ngPass99", "hello1", "gh"]
print(password_report(sample_passwords))
# Output: {'weak': ['abc', 'gh'], 'medium': ['password', 'hello1'], 'strong': ['Str0ngPass99']}