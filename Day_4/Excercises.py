# ------------------------------------------------------------
# Task 1
# Write say_hello() and call it three times.
# ------------------------------------------------------------

def say_hello():
    print("Hello, Python learner!")


say_hello()
say_hello()
say_hello()

# Sample Output:
# Hello, Python learner!
# Hello, Python learner!
# Hello, Python learner!


# ------------------------------------------------------------
# Task 2
# Write greet_user(name) with one parameter.
# ------------------------------------------------------------

def greet_user(name):
    print(f"Hello, {name}! Welcome to Python.")


greet_user("Harish")
greet_user("Rahul")

# Sample Output:
# Hello, Harish! Welcome to Python.
# Hello, Rahul! Welcome to Python.


# ------------------------------------------------------------
# Task 3
# Write show_square(number).
# ------------------------------------------------------------

def show_square(number):
    print(number ** 2)


show_square(5)
show_square(10)
show_square(-4)

# Sample Output:
# 25
# 100
# 16


# ============================================================
# Part B: Return Values vs. print()
# ============================================================


# ------------------------------------------------------------
# Task 4
# multiply(a, b) should RETURN the product.
# ------------------------------------------------------------

def multiply(a, b):
    return a * b


result = multiply(5, 6)
print("Task 4:", result)

# Sample Output:
# Task 4: 30


# ------------------------------------------------------------
# Task 5
# Create one function using print()
# and another using return.
# ------------------------------------------------------------

def is_even_print(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


def is_even_return(n):
    if n % 2 == 0:
        return True
    else:
        return False


print("Task 5:")

is_even_print(7)

result = is_even_return(7)
print(result)

if is_even_return(7):
    print("The number is even")
else:
    print("The number is odd")

# Sample Output:
# Task 5:
# Odd
# False
# The number is odd


# ------------------------------------------------------------
# Task 6
# Convert Celsius to Fahrenheit.
# Formula: F = C * 9/5 + 32
# ------------------------------------------------------------

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


print("Task 6:")

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(37))
print(celsius_to_fahrenheit(100))

# Sample Output:
# Task 6:
# 32.0
# 98.6
# 212.0


# ============================================================
# Part C: Positional, Default & Keyword Arguments
# ============================================================


# ------------------------------------------------------------
# Task 7
# order_summary(item, quantity=1)
# ------------------------------------------------------------

def order_summary(item, quantity=1):
    print(f"Item: {item}, Quantity: {quantity}")


order_summary("Laptop")
order_summary("Laptop", 3)

# Sample Output:
# Item: Laptop, Quantity: 1
# Item: Laptop, Quantity: 3


# ------------------------------------------------------------
# Task 8
# book_ticket(passenger, seat_type="Economy", meal="Veg")
# ------------------------------------------------------------

def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(
        f"Passenger: {passenger}, "
        f"Seat: {seat_type}, "
        f"Meal: {meal}"
    )


# (a) Only passenger
book_ticket("Harish")

# (b) Override only meal
book_ticket("Harish", meal="Non-Veg")

# (c) Override both defaults using keyword arguments
# in a different order than they were defined.
book_ticket(
    "Harish",
    meal="Non-Veg",
    seat_type="Business"
)

# Sample Output:
# Passenger: Harish, Seat: Economy, Meal: Veg
# Passenger: Harish, Seat: Economy, Meal: Non-Veg
# Passenger: Harish, Seat: Business, Meal: Non-Veg


# ------------------------------------------------------------
# Task 9
# total_cost(*prices)
# ------------------------------------------------------------

def total_cost(*prices):
    return sum(prices)


print("Task 9:")

print(total_cost(100, 200))
print(total_cost(100, 200, 300, 400, 500))

# Sample Output:
# Task 9:
# 300
# 1500


# ------------------------------------------------------------
# Task 10
# print_student_info(**details)
# ------------------------------------------------------------

def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


print("Task 10:")

print_student_info(
    name="Harish",
    age=22,
    course="Python",
    city="Chennai"
)

# Sample Output:
# Task 10:
# name: Harish
# age: 22
# course: Python
# city: Chennai


# ============================================================
# Part D: Docstrings, Scope, Lambda & Recursion
# ============================================================


# ------------------------------------------------------------
# Task 11
# Add docstrings to two functions.
# ------------------------------------------------------------

def celsius_to_fahrenheit_doc(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


def multiply_doc(a, b):
    """Return the product of two numbers."""
    return a * b


# help() output can be lengthy and Python-version dependent.
# Important part of the output:
#
# Help on function celsius_to_fahrenheit_doc:
# celsius_to_fahrenheit_doc(celsius)
#     Convert Celsius temperature to Fahrenheit.
#
# Help on function multiply_doc:
# multiply_doc(a, b)
#     Return the product of two numbers.

help(celsius_to_fahrenheit_doc)
help(multiply_doc)


# ------------------------------------------------------------
# Task 12
# Demonstrate local variable scope.
# ------------------------------------------------------------

def reset_score():
    score = 0
    print("Inside function:", score)


reset_score()

# Sample Output:
# Inside function: 0

# If you execute:
#
# print(score)
#
# you will get:
#
# NameError: name 'score' is not defined
#
# Explanation:
# score is a LOCAL variable.
# It exists only inside reset_score().
# It cannot be accessed outside the function.


# ------------------------------------------------------------
# Task 13
# Use global keyword to modify total_attempts.
# ------------------------------------------------------------

total_attempts = 0


def log_attempt():
    global total_attempts
    total_attempts += 1


log_attempt()
log_attempt()
log_attempt()

print("Task 13:", total_attempts)

# Sample Output:
# Task 13: 3


# ------------------------------------------------------------
# Task 14
# Lambda function and equivalent regular function.
# ------------------------------------------------------------

cube = lambda x: x ** 3

print("Lambda cube:", cube(3))


def cube_regular(x):
    return x ** 3


print("Regular function cube:", cube_regular(3))

# Sample Output:
# Lambda cube: 27
# Regular function cube: 27


# ------------------------------------------------------------
# Task 15
# Recursive countdown.
# ------------------------------------------------------------

def countdown(n):
    if n <= 0:
        print("Liftoff!")
        return

    print(n)
    countdown(n - 1)


countdown(5)

# Sample Output:
# 5
# 4
# 3
# 2
# 1
# Liftoff!


# ------------------------------------------------------------
# Task 16
# Recursive sum from 1 to n.
#
# Base case:
#     n == 1
#
# Recursive case:
#     n + sum_upto(n - 1)
# ------------------------------------------------------------

def sum_upto(n):
    if n == 1:
        return 1

    return n + sum_upto(n - 1)


print("Task 16:")

print(sum_upto(5))
print(sum_upto(1))

# Sample Output:
# Task 16:
# 15
# 1


# ============================================================
# Part E: Cumulative Challenges
# ============================================================


# ------------------------------------------------------------
# Task 17
# Check whether a string is a palindrome.
# Case-insensitive.
# ------------------------------------------------------------

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


print("Task 17:")

print(is_palindrome("level"))
print(is_palindrome("python"))
print(is_palindrome("Madam"))

# Sample Output:
# Task 17:
# True
# False
# True


# ------------------------------------------------------------
# Task 18
# Convert score into letter grade.
# ------------------------------------------------------------

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


print("Task 18:")

scores = [95, 82, 61, 40, 100]

for score in scores:
    grade = grade_from_score(score)
    print(f"{score} -> {grade}")

# Sample Output:
# Task 18:
# 95 -> A
# 82 -> B
# 61 -> D
# 40 -> F
# 100 -> A


# ------------------------------------------------------------
# Task 19
# Count vowels in a string.
# ------------------------------------------------------------

def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


print("Task 19:")

print(count_vowels("Python Bootcamp"))
print(count_vowels("Python is easy to learn"))

# Sample Output:
# Task 19:
# 4
# 7


# ------------------------------------------------------------
# Task 20
# FizzBuzz from start to end.
# ------------------------------------------------------------

def fizzbuzz_range(start, end):

    for number in range(start, end + 1):

        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")

        elif number % 3 == 0:
            print("Fizz")

        elif number % 5 == 0:
            print("Buzz")

        else:
            print(number)


print("Task 20:")

fizzbuzz_range(1, 20)

# Sample Output:
# Task 20:
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


# ------------------------------------------------------------
# Task 21
# Check prime numbers and find all primes up to a limit.
# ------------------------------------------------------------

def is_prime(n):

    if n < 2:
        return False

    for number in range(2, n):
        if n % number == 0:
            return False

    return True


def primes_up_to(limit):

    primes = []

    for number in range(2, limit + 1):

        if is_prime(number):
            primes.append(number)

    return primes


print("Task 21:")

print(primes_up_to(30))

# Sample Output:
# Task 21:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


# ------------------------------------------------------------
# Task 22
# Password strength checker.
#
# Rules:
# Strong:
#     length >= 10
#     AND has digit
#     AND has uppercase
#
# Medium:
#     length >= 6
#     AND has digit OR uppercase
#
# Otherwise:
#     Weak
# ------------------------------------------------------------

def password_strength(password):

    has_digit = False
    has_uppercase = False

    for char in password:

        if char.isdigit():
            has_digit = True

        if char.isupper():
            has_uppercase = True

    if len(password) >= 10 and has_digit and has_uppercase:
        return "Strong"

    elif len(password) >= 6 and (has_digit or has_uppercase):
        return "Medium"

    else:
        return "Weak"


print("Task 22:")

print("abc ->", password_strength("abc"))
print("hello12 ->", password_strength("hello12"))
print("Hello12345 ->", password_strength("Hello12345"))

# Sample Output:
# Task 22:
# abc -> Weak
# hello12 -> Medium
# Hello12345 -> Strong


# ------------------------------------------------------------
# Task 23
# Capstone:
# build_utilities(operation, *values)
#
# Supported operations:
# sum
# max
# min
# average
# ------------------------------------------------------------

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


print("Task 23:")

print(build_utilities("sum", 4, 8, 15))
print(build_utilities("average", 2, 4, 6, 8))
print(build_utilities("max", 10, 20, 5, 30))
print(build_utilities("min", 10, 20, 5, 30))

# Sample Output:
# Task 23:
# 27
# 5.0
# 30
# 5
