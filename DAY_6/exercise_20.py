num1 = "10"
num2 = "0"

try:
    result = int(num1) / int(num2)
    print("Result:", result)
except ValueError:
    print("Error: Both inputs must be valid numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
