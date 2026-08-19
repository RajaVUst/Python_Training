first = input("Enter the first integer: ")
second = input("Enter the second integer: ")

try:
    result = int(first) / int(second)
    print("Result:", result)
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("A number cannot be divided by zero.")

# OUTPUT (when the inputs are 10 and 2)

# Result: 5.0
