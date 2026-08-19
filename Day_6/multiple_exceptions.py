first = input("Enter first number: ")
second = input("Enter second number: ")

try:
    num1 = int(first)
    num2 = int(second)

    result = num1 / num2

    print(result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

# output:
# Enter first number: 11
# Enter second number: 22
# 0.5