a = input("Enter first number: ")
b = input("Enter second number: ")
try:
    num1 = int(a)
    num2 = int(b)
    result = num1 / num2
    print(result)
except ValueError:
    print("Please enter valid numbers")
except ZeroDivisionError:
    print("Cannot divide by zero")

#     output
#     Enter first number: 10
# Enter second number: 0
# Cannot divide by zero