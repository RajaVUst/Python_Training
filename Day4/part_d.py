# Part D: Docstrings, Scope, Lambda & Recursion

# Task 11
def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b
def is_even_print(n):
    """Prints whether a number is even or odd."""
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
print(multiply.__doc__)
print(is_even_print.__doc__)
# Output:
# Returns the product of two numbers.
# Prints whether a number is even or odd.


# Task 12
def reset_score():
    score = 0
    print("Inside Function:", score)
reset_score()
# print(score)
# Output:
# Inside Function: 0
# If print(score) is uncommented:
# NameError: name 'score' is not defined
# Reason:
# score is a local variable and exists only inside the function.


# Task 13
total_attempts = 0
def log_attempt():
    global total_attempts
    total_attempts += 1
log_attempt()
log_attempt()
log_attempt()
print(total_attempts)
# Output:
# 3


# Task 14
cube = lambda x: x ** 3
print(cube(3))
def cube_function(x):
    return x ** 3
print(cube_function(3))
# Output:
# 27
# 27


# Task 15
def countdown(n):
    if n == 0:
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)
countdown(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# Liftoff!


# Task 16
# Base Case:
# n == 1
# Recursive Case:
# n + sum_upto(n - 1)
def sum_upto(n):
    if n == 1:
        return 1
    return n + sum_upto(n - 1)
print(sum_upto(5))
print(sum_upto(1))
# Output:
# 15
# 1