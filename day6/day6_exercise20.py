num1 = "10"
num2 = "0"

try:
    a = int(num1)
    b = int(num2)

    result = a / b
    print("Result:", result)

except ValueError:
    print("Invalid number entered.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

"""
OUTPUT:
You cannot divide by zero.
"""