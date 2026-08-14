def calculate_total(numbers):
    """Return the sum of all numbers in the list."""
    return sum(numbers)

def find_average(numbers):
    """Return the arithmetic mean of a list of numbers."""
    return sum(numbers) / len(numbers)

help(calculate_total)
help(find_average)

#Output:
"""
calculate_total(numbers)
    Return the sum of all numbers in the list.

Help on function find_average in module __main__:                                                                         

find_average(numbers)
    Return the arithmetic mean of a list of numbers.
    """