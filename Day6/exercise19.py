# Day 6 - Exercise 19

test_value = "abc"

try:
    number = int(test_value)
    print("Number:", number)
except ValueError:
    print("The value must be a valid integer.")

#output
'''
The value must be a valid integer.
'''

