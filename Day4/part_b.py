# Part B: Return Values vs print()

# Task 4
def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b
result = multiply(6, 6)
print("Product:", result)
# Output:
# Product: 36


# Task 5
def is_even_print(n):
    """Prints whether a number is even or odd."""
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
def is_even_return(n):
    return n % 2 == 0
print("Using print version:")
is_even_print(8)
print("Using return version:")
result = is_even_return(8)
print(result)
# Output:
# Using print version:
# Even
# Using return version:
# True


# Task 6
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(37))
print(celsius_to_fahrenheit(100))
# Output:
# 32.0
# 98.6
# 212.0
