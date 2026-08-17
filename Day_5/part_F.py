# excercise 19

def vowel_counts(sentence):
    vowels = "aeiou"
    counts = {}
    for word in sentence.split():
        count = sum(1 for char in word.lower() if char in vowels)
        counts[word] = count
    return counts
result = vowel_counts("The Quick Brown Fox Jumps")
print(result)
# Output
# {'The': 1, 'Quick': 2, 'Brown': 1, 'Fox': 1, 'Jumps': 1}

# excercise 20

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
roster = [
    {"name": "Amit", "scores": [78, 82, 74]},{"name": "Reni", "scores": [91, 95, 87]},{"name": "Tara", "scores": [65, 70, 68]}]
print(grade_summary(roster))
# Output
# [{'name': 'Amit', 'average': 78.0, 'grade': 'C'}, {'name': 'Reni', 'average': 91.0, 'grade': 'A'}, {'name': 'Tara', 'average': 67.7, 'grade': 'D'}]

# excercise 21 

def unique_words(text):
    unique = {word.lower() for word in text.split()}
    return sorted(unique)
sentence = "The quick brown fox jumps over the lazy dog and the quick fox"
print(unique_words(sentence))

# exercise 22
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
# Out put
#{1: '1', 2: '2', 3: 'Fizz', 4: '4', 5: 'Buzz', 6: 'Fizz', 7: '7', 8: '8', 9: 'Fizz', 10: 'Buzz', 11: '11', 12: 'Fizz', 13: '13', 14: '14', 15: 'FizzBuzz', 16: '16', 17: '17', 18: 'Fizz', 19: '19', 20: 'Buzz'}

# excercise 23

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
    "hehe","secret","learnningpython@134",  
]
print(password_report(passwords))

# output
#{'weak': ['hehe'], 'medium': ['secret'], 'strong': ['learnningpython@134']}