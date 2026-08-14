# Task 11: Docstrings
def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

help(multiply)
help(celsius_to_fahrenheit)
# Output:
# Help on function multiply:
# multiply(a, b)
#     Returns the product of a and b.
# Help on function celsius_to_fahrenheit:
# celsius_to_fahrenheit(celsius)
#     Converts Celsius to Fahrenheit.


# Task 12: Local Scope
def reset_score():
    score = 0

reset_score()
print(score)
# Output:
# NameError: name 'score' is not defined


# Task 13: Global Keyword
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


# Task 14: Cube 
cube = lambda x: x ** 3
print(cube(3))

def cube_func(x):
    return x ** 3

print(cube_func(3))
# Output:
# 27
# 27


# Task 15: Countdown 
def countdown(n):
    if n < 1:
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


# Task 16: Sum Upto (Recursion)
def sum_upto(n):
    if n == 1:
        return 1
    return n + sum_upto(n - 1)

print(sum_upto(5))
print(sum_upto(1))
# Output:
# 15
# 1