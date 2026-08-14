def sum_upto(n):
    # Base case: when n reaches 1, return 1
    if n == 1:
        return 1
    
    # Recursive case: add n to the sum of numbers before it
    return n + sum_upto(n - 1)
print(sum_upto(5))
print(sum_upto(1))

"""
output
15
1
"""

