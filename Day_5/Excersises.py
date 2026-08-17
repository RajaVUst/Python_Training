

# Exercise 1: Shopping List Manager
cart = ["milk", "bread", "rice"]

cart.append("eggs")
cart.append("sugar")

cart.remove("rice")

print("Exercise 1")
print("Original list:", cart)
print("Sorted list:", sorted(cart))
print()


# Exercise 2: Rotate the Queue
queue = ["Amit", "Reni", "Tara", "Sam"]

print("Exercise 2")
print("Before:", queue)

person = queue.pop(0)
queue.append(person)

print("After:", queue)
print()


# Exercise 3: Running Total With Slicing
readings = [12, 15, 9, 22, 30, 4, 18]

print("Exercise 3")
print("First three readings:", readings[:3])
print("Last two readings:", readings[-2:])
print("Every second reading:", readings[::2])
print()


# Exercise 4: Copy vs Reference
original = [1, 2, 3]

alias = original
safe_copy = original.copy()

alias.append(100)
safe_copy.append(200)

print("Exercise 4")
print("Original:", original)
print("Alias:", alias)
print("Safe copy:", safe_copy)

# alias refers to the same list object as original,
# while safe_copy is a separate list.
print()


# Exercise 5: Coordinates
location = (12.97, 77.59)

print("Exercise 5")
print("Location:", location)

try:
    location[0] = 13.00
except TypeError as error:
    print("Expected error:", error)

print()


# Exercise 6: Unpacking a Tuple
record = ("Reni", 91, "Cohort 2")

name, score, cohort = record

print("Exercise 6")
print(f"{name} scored {score} marks and belongs to {cohort}.")
print()


# Exercise 7: Multiple Return Values
def stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average


minimum, maximum, average = stats([4, 9, 1, 7, 15])

print("Exercise 7")
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)
print()


# Exercise 8: De-duplicating Attendance
attendance = [
    "amit",
    "reni",
    "amit",
    "tara",
    "reni",
    "sam"
]

unique_attendees = set(attendance)

print("Exercise 8")
print("Unique attendees:", unique_attendees)
print("Number of unique attendees:", len(unique_attendees))
print()


# Exercise 9: Common Interests
cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}

print("Exercise 9")
print("Common skills:", cohort_a & cohort_b)
print("Unique to cohort A:", cohort_a - cohort_b)
print("All skills:", cohort_a | cohort_b)
print()


# Exercise 10: Fast Membership Check
seen = set(range(1000))

print("Exercise 10")

if 999 in seen:
    print("999 is present in the set.")
else:
    print("999 is not present in the set.")

print()



# Exercise 11: Contact Card
contact = {
    "name": "Reni",
    "email": "reni@example.com",
    "phone": "9876543210"
}

print("Exercise 11")

print("Name:", contact["name"])
print("Email:", contact["email"])
print("Phone:", contact["phone"])

contact["city"] = "Chennai"
contact["phone"] = "9876501234"

contact.pop("email")

print("Updated contact:", contact)
print()


# Exercise 12: Word Frequency Counter
text = "the quick brown fox jumps over the lazy dog the fox runs"

words = text.split()

word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print("Exercise 12")
print("Word counts:", word_counts)
print()


# Exercise 13: Class Roster
roster = [
    {
        "name": "Amit",
        "scores": [80, 85, 90]
    },
    {
        "name": "Reni",
        "scores": [91, 88, 94]
    },
    {
        "name": "Tara",
        "scores": [70, 75, 80]
    }
]

print("Exercise 13")

for student in roster:
    average = sum(student["scores"]) / len(student["scores"])

    print(
        student["name"],
        "Average:",
        round(average, 1)
    )

print()


# Exercise 14: Lookup Table
grade_lookup = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60,
    "F": 0
}

score = 84

print("Exercise 14")

for grade, threshold in grade_lookup.items():

    if score >= threshold:
        print("Score:", score)
        print("Grade:", grade)
        break

print()


# Exercise 15: Squares and Cubes
cubes = [
    n ** 3
    for n in range(1, 11)
]

even_cubes = [
    n ** 3
    for n in range(1, 11)
    if n % 2 == 0
]

print("Exercise 15")
print("Cubes:", cubes)
print("Even cubes:", even_cubes)
print()


# Exercise 16: Label the Temperatures
temps = [15, 22, 31, 8, 27, 19]

labels = [
    "hot" if t >= 25
    else "mild" if t >= 15
    else "cold"
    for t in temps
]

print("Exercise 16")
print("Temperatures:", temps)
print("Labels:", labels)
print()


# Exercise 17: Dictionary From Two Lists
names = ["Amit", "Reni", "Tara"]
scores = [78, 91, 65]

scores_dict = {
    name: score
    for name, score in zip(names, scores)
}

print("Exercise 17")
print("Scores dictionary:", scores_dict)
print()


# Exercise 18: Filtering With a Dict Comprehension
passing_scores = {
    name: score
    for name, score in scores_dict.items()
    if score >= 70
}

print("Exercise 18")
print("Scores 70 or above:", passing_scores)
print()




# Exercise 19: Vowel Counter by Word
def vowel_counts(sentence):

    result = {}

    for word in sentence.lower().split():

        count = 0

        for character in word:

            if character in "aeiou":
                count += 1

        result[word] = count

    return result


sentence = "The Quick Brown Fox Jumps"

print("Exercise 19")
print(vowel_counts(sentence))
print()


# Exercise 20: Grade Book Summary
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


grade_roster = [
    {
        "name": "Amit",
        "scores": [80, 85, 90]
    },
    {
        "name": "Reni",
        "scores": [91, 88, 94]
    },
    {
        "name": "Tara",
        "scores": [70, 75, 80]
    }
]

print("Exercise 20")
print(grade_summary(grade_roster))
print()


# Exercise 21: Unique Word Finder
def unique_words(text):

    words = text.lower().split()

    unique = set(words)

    return sorted(unique)


test_sentence = "Python is easy and Python is powerful"

print("Exercise 21")
print(unique_words(test_sentence))
print()


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


print("Exercise 22")
print(fizzbuzz_map(20))
print()


# Exercise 23: Password Strength Report
def password_report(passwords):

    result = {
        "weak": [],
        "medium": [],
        "strong": []
    }

    for password in passwords:

        has_digit = any(
            character.isdigit()
            for character in password
        )

        if len(password) >= 10 and has_digit:
            result["strong"].append(password)

        elif len(password) >= 6:
            result["medium"].append(password)

        else:
            result["weak"].append(password)

    return result


passwords = [
    "abc",
    "12345",
    "python",
    "python123",
    "HelloWorld",
    "SecurePass123"
]

print("Exercise 23")
print(password_report(passwords))
print()

