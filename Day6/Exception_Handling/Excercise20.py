# Multiple except blocks

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

# Output:
# Enter first number: 3
# Enter second number: 0
# Cannot divide by zero.

# Enter first number: d
# Please enter numbers only.