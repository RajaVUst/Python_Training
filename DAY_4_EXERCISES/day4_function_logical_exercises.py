# Docstring

def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def total_cost(*prices):
    """Return the sum of all prices provided."""
    return sum(prices)

help = help(celsius_to_fahrenheit)

"""
RESULT ->function_logical_exercises.py

Help on function celsius_to_fahrenheit in module __main__:                                              

celsius_to_fahrenheit(celsius)
    Convert a temperature from Celsius to Fahrenheit."""

# Reset Score

def reset_score():
    score = 0
reset_score()

""" NameError occurs because 'score' is a local variable.
Local variables exist only inside the function where they are created.
After the function finishes executing, the variable is no longer accessible.
"""
print(score)

# Scope exercise

total_attempts = 0

def  log_attempt():
    global total_attempts
    total_attempts += 1
    print(total_attempts)

log_attempt()
log_attempt()
log_attempt()

print(total_attempts)

""" 
Output->
1
2
3
"""

# Lambda function and Equavalent Def

cube = lambda x: x ** 3 

print(cube(3))

""" Output -> 27 """

def cube_function(x):
    return x ** 3

print(cube_function(3))

""" Output -> 27 """

# Recursive Function

def countdown(n):
    if n<1:
        print("Lift-Off!!!")
    else:
        print(n)
        countdown(n-1)

countdown(10)

""" 
Output ->
10
9
8
7
6
5
4
3
2
1
Lift-Off!!!
"""

# Sum of numbers using recursion

def sum_upto(n):
    if n == 1:
        return 1
    return n + sum_upto(n - 1)

print(sum_upto(5))
print(sum_upto(1))

""" 
Output->
15
1
"""


