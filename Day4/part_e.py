# Part E: Cumulative Challenges

# Task 17
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


# Task 18
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
for score in scores:
    print(f"{score} -> {grade_from_score(score)}")
# Output:
# 95 -> A
# 82 -> B
# 61 -> D
# 40 -> F
# 100 -> A


# Task 19
def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count
print(count_vowels("Python Bootcamp"))
print(count_vowels("I am learning Python Functions"))
# Output:
# 4
# 9


# Task 20
def fizzbuzz_range(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
fizzbuzz_range(1, 15)
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


# Task 21
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def primes_up_to(limit):
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes
print(primes_up_to(30))
# Output:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


# Task 22
def password_strength(password):
    has_digit = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    if len(password) >= 8 and has_digit and has_upper:
        return "Strong"
    elif len(password) >= 6:
        return "Medium"
    else:
        return "Weak"
print(password_strength("abc"))
print(password_strength("python12"))
print(password_strength("Python123"))