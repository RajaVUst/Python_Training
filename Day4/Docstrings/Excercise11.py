# Docstrings

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

print(multiply(5, 4))
print(celsius_to_fahrenheit(100))

help(multiply)
help(celsius_to_fahrenheit)

# Output:
# 20
# 212.0
# Help on function multiply in module __main__: 