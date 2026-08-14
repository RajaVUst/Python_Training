# Task 17 

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]
print(is_palindrome('level'))
print(is_palindrome('python'))
print(is_palindrome('Madam'))

# Output

# True
# False
# True

# Task 18 

def grade_from_score(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
scores = [95, 82, 61, 40, 100]
for score in scores:
    print(f"{score} -> {grade_from_score(score)}")

# Output 

# 95 -> A
# 82 -> B
# 61 -> D
# 40 -> F
# 100 -> A

# Task 19

def count_vowels(text):
    count = 0
    vowels = "aeiou"
    for char in text.lower():
        if char in vowels:
            count += 1
    return count
print(count_vowels("Python Bootcamp"))
print(count_vowels("Learning Python is fun!"))

# Output

# 4
# 6

# task 21

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
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes
print(primes_up_to(30))

# Output

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Task 22

def password_strength(password):
    has_digit = False
    has_upper = False
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True

    if len(password) < 8:
        return "Weak"
    elif has_digit and has_upper:
        return "Strong"
    else:
        return "Medium"
print(password_strength('strong'))
print(password_strength('Password'))
print(password_strength('Pyhtonpass67'))

# output

# Weak
# Medium
# Strong

# Task 23

def build_utilities(operation, *values):
    if operation == "sum":
        return sum(values)
    elif operation == "max":
        return max(values)
    elif operation == "min":
        return min(values)
    elif operation == "average":
        return sum(values) / len(values)
    else:
        return "Invalid operation"
print(build_utilities("sum", 4, 8, 15))
print(build_utilities("average", 2, 4, 6, 8))
print(build_utilities("max", 3,28,19))
print(build_utilities("min", 3,28,19))
