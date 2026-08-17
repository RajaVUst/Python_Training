
# Part F: Cumulative Challenges (Days 1-5)

# Exercise 19: Vowel Counter by Word
def vowel_counts(sentence):
    vowels = "aeiou"
    result = {}
    for word in sentence.split():
        count = sum(1 for ch in word.lower() if ch in vowels)
        result[word] = count
    return result
print(vowel_counts("The Quick Brown Fox Jumps"))
# Output:
# {'The': 1, 'Quick': 2, 'Brown': 1, 'Fox': 1, 'Jumps': 1}
print("\n" + "=" * 40 + "\n")


# Exercise 20: Grade Book Summary
def grade_summary(roster):
    summary = []
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
        summary.append({
            "name": student["name"],
            "average": round(average, 1),
            "grade": grade
        })
    return summary
roster = [
    {"name": "Amit", "scores": [85, 90, 88]},
    {"name": "Varsha", "scores": [95, 92, 89]},
    {"name": "Tara", "scores": [70, 75, 80]}
]
print(grade_summary(roster))
# Output:
# [{'name': 'Amit', 'average': 87.7, 'grade': 'B'},
#  {'name': 'Varsha', 'average': 92.0, 'grade': 'A'},
#  {'name': 'Tara', 'average': 75.0, 'grade': 'C'}]
print("\n" + "=" * 40 + "\n")


# Exercise 21: Unique Word Finder
def unique_words(text):
    words = set(text.lower().split())
    return sorted(words)
print(unique_words("Python is fun and Python is powerful"))
# Output:
# ['and', 'fun', 'is', 'powerful', 'python']
print("\n" + "=" * 40 + "\n")


# Exercise 22: FizzBuzz, Structured
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

# Output:
# {
# 1: '1', 2: '2', 3: 'Fizz', 4: '4', 5: 'Buzz',
# 6: 'Fizz', 7: '7', 8: '8', 9: 'Fizz', 10: 'Buzz',
# 11: '11', 12: 'Fizz', 13: '13', 14: '14', 15: 'FizzBuzz',
# 16: '16', 17: '17', 18: 'Fizz', 19: '19', 20: 'Buzz'
# }
print("\n" + "=" * 40 + "\n")


# Exercise 23: Password Strength Report (Capstone)
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
passwords = [
    "abc",
    "hello",
    "secret",
    "python123",
    "StrongPass1",
    "welcome12"
]
print(password_report(passwords))
#output
#{
#   'weak': ['abc', 'hello'],
#  'medium': ['secret', 'python123'],
#   'strong': ['StrongPass1', 'welcome12']
#}