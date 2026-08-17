# Exercise 19 - Vowel Counter by Word
def vowel_counts(sentence):
    words = sentence.lower().split()
    result = {}
    for word in words:
        count = 0
        for ch in word:
            if ch in "aeiou":
                count += 1
        result[word] = count
    return result
 
print(vowel_counts("The Quick Brown Fox Jumps"))
# Output: {'the': 1, 'quick': 2, 'brown': 1, 'fox': 1, 'jumps': 1}
 
# Exercise 20 - Grade Book Summary
def grade_summary(roster):
    result = []
    for student in roster:
        average = sum(student["scores"]) / len(student["scores"])
        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        else:
            grade = "F"
        result.append({"name": student["name"], "average": round(average, 1), "grade": grade})
    return result
 
roster = [
    {"name": "Navya", "scores": [85, 90, 78]},
    {"name": "Deepak", "scores": [70, 65, 80]},
    {"name": "Varsha", "scores": [92, 88, 95]}
]
 
print(grade_summary(roster))
# Output:
# [{'name': 'Navya', 'average': 84.3, 'grade': 'B'}, {'name': 'Deepak', 'average': 71.7, 'grade': 'C'}, {'name': 'Varsha', 'average': 91.7, 'grade': 'A'}]
 
# Exercise 21 - Unique Word Finder
def unique_words(text):
    words = text.lower().split()
    return sorted(set(words))
 
print(unique_words("The fox ran and the fox jumped"))
# Output: ['and', 'fox', 'jumped', 'ran', 'the']
 
# Exercise 22 - FizzBuzz, Structured
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
# Output:
# {1: '1', 2: '2', 3: 'Fizz', 4: '4', 5: 'Buzz', 6: 'Fizz', 7: '7', 8: '8', 9: 'Fizz', 10: 'Buzz', 11: '11', 12: 'Fizz', 13: '13', 14: '14', 15: 'FizzBuzz', 16: '16', 17: '17', 18: 'Fizz', 19: '19', 20: 'Buzz'}
  
# Exercise 23 - Password Strength Report (Capstone)
def password_report(passwords):
    report = {"weak": [], "medium": [], "strong": []}
    for pw in passwords:
        has_digit = any(ch.isdigit() for ch in pw)
        if len(pw) >= 10 and has_digit:
            report["strong"].append(pw)
        elif len(pw) >= 6:
            report["medium"].append(pw)
        else:
            report["weak"].append(pw)
    return report
 
passwords = ["abc", "abcdef", "abcdefgh12", "pass1", "strongpass99"]
print(password_report(passwords))
# Output:
# {'weak': ['abc', 'pass1'], 'medium': ['abcdef'], 'strong': ['abcdefgh12', 'strongpass99']}