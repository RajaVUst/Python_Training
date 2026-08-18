# Day 6 - Exercise 23

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

    return age


test_ages = [23, -5]

for age in test_ages:
    try:
        print("Valid age:", check_age(age))
    except ValueError as error:
        print("Error:", error)

#output
'''
Valid age: 23
Error: Age cannot be negative.
'''

