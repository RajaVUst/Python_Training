# Exercise 19: Vowel Counter by Word
def vowel_counts(sentence):
    dict_vowels = {}
    for word in sentence.lower().split():
        for i in word:
            if i in "aeiou":
                dict_vowels[word] = dict_vowels.get(word,0)+1
    return dict_vowels

print(vowel_counts("The Quick Brown Fox Jumps"))    # {'the': 1, 'quick': 2, 'brown': 1, 'fox': 1, 'jumps': 1}

# Exercise 20: Grade Book Summary
def grade_summary(roster):
    result = []
    for student in roster:
        name = student["name"]
        scores = student["scores"]
        average = sum(scores) / len(scores)

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

        result.append({"name": name,"average": average,"grade": grade})
    return result

roster = [
    {"name": "Alice", "scores": [90, 85, 95]},
    {"name": "Bob", "scores": [75, 80, 70]},
    {"name": "Charlie", "scores": [55, 60, 50]}
]

print(grade_summary(roster))    # [{'name': 'Alice', 'average': 90.0, 'grade': 'A'}, {'name': 'Bob', 'average': 75.0, 'grade': 'C'}, {'name': 'Charlie', 'average': 55.0, 'grade': 'F'}]

# Exercise 21: Unique Word Finder
def unique_words(text):
    return sorted(set(text.lower().split()))

print(unique_words("The good boy is on the boy house"))   # ['boy', 'good', 'house', 'is', 'on', 'the'] 

# Exercise 22: FizzBuzz, Structured
def fizzbuzz_map(n):
    result = {}
    for i in range(1, n + 1):
        if i % 15 == 0:
            value = "FizzBuzz"
        elif i % 3 == 0:
            value = "Fizz"
        elif i % 5 == 0:
            value = "Buzz"
        else:
            value = i
        result[i] = value
    return result

print(fizzbuzz_map(20)) # {1: '1', 2: '2', 3: 'Fizz', 4: '4', 5: 'Buzz', 6: 'Fizz', 7: '7', 8: '8', 9: 'Fizz', 10: 'Buzz', 11: '11', 12: 'Fizz', 13: '13', 14: '14', 15: 'FizzBuzz', 16: '16', 17: '17', 18: 'Fizz', 19: '19', 20: 'Buzz'}

# Exercise 23: Password Strength Report (Capstone)
def password_report(passwords):
    result = { "weak": [], "medium": [], "strong": [] }

    for pw in passwords:
        has_digit = any(ch.isdigit() for ch in pw)

        if len(pw) >= 10 and has_digit:
            category = "strong"
        elif len(pw) >= 6:
            category = "medium"
        else:
            category = "weak"

        result[category].append(pw)
    return result

passwords = ["cat", "hello", "python", "python123", "myPassword", "SuperCode123"]

print(password_report(passwords))   # {'weak': ['cat', 'hello'], 'medium': ['python', 'python123', 'myPassword'], 'strong': ['SuperCode123']}