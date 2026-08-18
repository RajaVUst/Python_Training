# Day 6 - Exercise 20

first_input = input("Enter the first number: ")
second_input = input("Enter the second number: ")

try:
    first_number = int(first_input)
    second_number = int(second_input)

    result = first_number / second_number
    print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("A number cannot be divided by zero.")

#output
'''
Enter the first number: 4
Enter the second number: 0
A number cannot be divided by zero.
'''

