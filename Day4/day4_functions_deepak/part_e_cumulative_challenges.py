# Task 17: Palindrome Checker
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]
 
print(is_palindrome("level"))
print(is_palindrome("python"))
print(is_palindrome("Madam"))
# Output:
# True
# False
# True
 
 
# Task 18: Grade from Score
def grade_from_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
 
scores = [95, 82, 61, 40, 100]
for s in scores:
    print(f"{s} -> {grade_from_score(s)}")
# Output:
# 95 -> A
# 82 -> B
# 61 -> D
# 40 -> F
# 100 -> A
 
 
# Task 19: Count Vowels
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count
 
print(count_vowels("Python Bootcamp"))
print(count_vowels("Hello World"))
# Output:
# 4
# 3
 
 
# Task 20: FizzBuzz Range
def fizzbuzz_range(start, end):
    for i in range(start, end + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
 
fizzbuzz_range(1, 20)
# Output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
 
 
# Task 21: Prime Check & Primes Up To
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
 
def primes_up_to(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes
 
print(primes_up_to(30))
# Output:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
 
 
# Task 22: Password Strength
def password_strength(password):
    has_digit = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    length_ok = len(password) >= 8
 
    if length_ok and has_digit and has_upper:
        return "Strong"
    elif length_ok and (has_digit or has_upper):
        return "Medium"
    else:
        return "Weak"
 
print(password_strength("abc123"))
print(password_strength("Abcdefgh1"))
print(password_strength("abcdefgh"))
# Output:
# Weak
# Strong
# Weak
 
 
# Task 23: Capstone
def build_utilities(operation, *values):
    if operation == "sum":
        return sum(values)
    elif operation == "max":
        return max(values)
    elif operation == "min":
        return min(values)
    elif operation == "average":
        return sum(values) / len(values)
 
print(build_utilities("sum", 4, 8, 15))
print(build_utilities("average", 2, 4, 6, 8))
# Output:
# 27
# 5.0