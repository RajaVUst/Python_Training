first = input("Enter the first number: ")
second = input("Enter the second number: ")

try:
    num1 = int(first)
    num2 = int(second)

    result = num1 / num2

    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# Enter the first number: 5
# Enter the second number: 2
# Result: 2.5

# Enter the first number: abc
# Enter the second number: 3
# Invalid input. Please enter numbers only.

# Enter the first number: 20
# Enter the second number: 0
# Cannot divide by zero.
