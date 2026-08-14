# Task 4: Multiply
def multiply(a, b):
    return a * b
 
result = multiply(6, 7)
print(result)
# Output:
# 42
 
 
# Task 5: Even Checker (Print vs Return)
def is_even_print(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
 
def is_even_return(n):
    return n % 2 == 0
 
is_even_print(7)
print(is_even_return(7))
# Output:
# Odd
# False
 
 
# Task 6: Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32
 
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(37))
print(celsius_to_fahrenheit(100))
# Output:
# 32.0
# 98.6
# 212.0