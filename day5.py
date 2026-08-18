# Part A - Lists

# Q1
cart = ["milk", "bread", "eggs"]

cart.append("rice")
cart.append("apple")
cart.remove("bread")

print(sorted(cart))


# Q2
queue = ["Amit", "Reni", "Tara", "Sam"]

print(queue)

first_person = queue.pop(0)
queue.append(first_person)

print(queue)


# Q3
readings = [12, 15, 9, 22, 30, 4, 18]

print(readings[:3])
print(readings[-2:])
print(readings[::2])


# Q4
original = [1, 2, 3]
alias = original
safe_copy = original.copy()

alias.append(100)
safe_copy.append(200)

print(original)
print(alias)
print(safe_copy)


# Part B - Tuples

# Q5
location = (12.97, 77.59)

try:
    location[0] = 13.00
except TypeError as e:
    print(e)


# Q6
record = ("Reni", 91, "Cohort 2")

name, score, cohort = record

print(f"{name} scored {score} and belongs to {cohort}.")


# Q7
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

low, high, avg = stats([4, 9, 1, 7, 15])

print(low)
print(high)
print(avg)


# Part C - Sets

# Q8
attendance = ["amit", "reni", "amit", "tara", "reni", "sam"]

unique_attendees = set(attendance)

print(unique_attendees)
print(len(unique_attendees))


# Q9
cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}

print(cohort_a & cohort_b)
print(cohort_a - cohort_b)
print(cohort_a | cohort_b)


# Q10
seen = set(range(1000))

if 999 in seen:
    print("999 found in set")
else:
    print("999 not found")


# Part D - Dictionaries & Nested Structures

# Q11
contact = {
    "name": "Amit",
    "email": "amit@example.com",
    "phone": "9876543210"
}

print(contact["name"])
print(contact["email"])
print(contact["phone"])

contact["city"] = "Trivandrum"
contact["phone"] = "9999999999"

contact.pop("email")

print(contact)


# Q12
text = "the quick brown fox jumps over the lazy dog the fox runs"

word_counts = {}

for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)


# Q13
roster = [
    {"name": "Amit", "scores": [80, 85, 90]},
    {"name": "Reni", "scores": [95, 88, 92]},
    {"name": "Tara", "scores": [70, 75, 78]}
]

for student in roster:
    average = sum(student["scores"]) / len(student["scores"])
    print(student["name"], round(average, 1))


# Q14
grade_lookup = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60,
    "F": 0
}

score = 84

for grade, threshold in grade_lookup.items():
    if score >= threshold:
        print(grade)
        break


# Part E - Comprehensions

# Q15
cubes = [n ** 3 for n in range(1, 11)]
even_cubes = [n ** 3 for n in range(1, 11) if n % 2 == 0]

print(cubes)
print(even_cubes)


# Q16
temps = [15, 22, 31, 8, 27, 19]

labels = [
    "hot" if t >= 25 else ("mild" if t >= 15 else "cold")
    for t in temps
]

print(labels)


# Q17
names = ["Amit", "Reni", "Tara"]
scores = [78, 91, 65]

scores_dict = {
    name: score
    for name, score in zip(names, scores)
}

print(scores_dict)


# Q18
filtered_scores = {
    name: score
    for name, score in scores_dict.items()
    if score >= 70
}

print(filtered_scores)


# Part F - Cumulative Challenges

# Q19
def vowel_counts(sentence):
    vowels = "aeiou"
    result = {}

    for word in sentence.split():
        count = sum(1 for ch in word.lower() if ch in vowels)
        result[word] = count

    return result

print(vowel_counts("The Quick Brown Fox Jumps"))


# Q20
def grade_summary(roster):
    result = []

    for student in roster:
        avg = sum(student["scores"]) / len(student["scores"])

        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        else:
            grade = "F"

        result.append({
            "name": student["name"],
            "average": round(avg, 1),
            "grade": grade
        })

    return result

print(grade_summary(roster))


# Q21
def unique_words(text):
    return sorted(set(text.lower().split()))

print(unique_words("Python is fun and Python is powerful"))


# Q22
def fizzbuzz_map(n):
    result = {}

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result[i] = "FizzBuzz"
        elif i % 3 == 0:
            result[i] = "Fizz"
        elif i % 5 == 0:
            result[i] = "Buzz"
        else:
            result[i] = str(i)

    return result

print(fizzbuzz_map(20))


# Q23
def password_report(passwords):
    report = {
        "weak": [],
        "medium": [],
        "strong": []
    }

    for pw in passwords:
        has_digit = any(ch.isdigit() for ch in pw)

        if len(pw) >= 10 and has_digit:
            report["strong"].append(pw)
        elif len(pw) >= 6:
            report["medium"].append(pw)
        else:
            report["weak"].append(pw)

    return report

sample_passwords = [
    "abc",
    "secret",
    "mypassword",
    "pass123456",
    "StrongPass1",
    "qwerty"
]

print(password_report(sample_passwords))