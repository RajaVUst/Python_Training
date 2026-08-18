test_value = "hello"

try:
    number = int(test_value)
    print(number)
except ValueError:
    print("Please enter a valid whole number.")

"""
OUTPUT:
Please enter a valid whole number.
"""