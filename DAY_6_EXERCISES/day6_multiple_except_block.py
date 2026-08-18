num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

try:
    result = int(num1) / int(num2)
    print("Result:", result)

except ValueError:
    print("Invalid number entered.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

"""
Output->
Enter first number: 5
Enter second number: g
Invalid number entered.
"""