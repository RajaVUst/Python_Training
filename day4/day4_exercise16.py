# Base case:
# If n == 1, return 1.
#
# Recursive case:
# Return n + sum_upto(n - 1).

def sum_upto(n):
    if n == 1:
        return 1
    return n + sum_upto(n - 1)

print("sum_upto(5) =", sum_upto(5))
print("sum_upto(1) =", sum_upto(1))