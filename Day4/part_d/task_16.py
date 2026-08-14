# Base case: when n is 1, return 1.
# Recursive case: add n to the sum of numbers from 1 to n-1.

def sum_upto(n):
    if n == 1:
        return 1
    return n + sum_upto(n - 1)


print(f"sum up to 5 : {sum_upto(5)}")
print(f"sum up to 1 : {sum_upto(1)}")

# output
# sum up to 5 : 15
# sum up to 1 : 1