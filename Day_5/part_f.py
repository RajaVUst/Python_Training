# Exercise 19: Vowel Counter by Word

def vowel_counts(sentence):
    result = {}

    for word in sentence.split():
        count = 0

        for ch in word.lower():
            if ch in "aeiou":
                count += 1

        result[word] = count

    return result


print(vowel_counts("The Quick Brown Fox Jumps"))


# Exercise 20: Grade Book Summary

def grade_summary(roster):
    summary = []

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

        summary.append({
            "name": student["name"],
            "average": round(avg, 1),
            "grade": grade
        })

    return summary


roster = [
    {"name": "Jay", "scores": [78, 82, 80]},
    {"name": "Niki", "scores": [95, 90, 92]},
    {"name": "Jake", "scores": [65, 70, 68]}
]

print(grade_summary(roster))
print()


# Exercise 21: Unique Word Finder

def unique_words(text):
    words = [word.lower() for word in text.split()]
    return sorted(set(words))


print(unique_words("Python is fun and Python is powerful"))
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

print(fizzbuzz_map(20))
print()


# Exercise 23: Password Strength Report

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
    "python",
    "hello123",
    "StrongPass1",
    "password2025",
    "cat"
]

print(password_report(sample_passwords))