def sum_upto(n):
    if n == 1:
        return 1
    return n + sum_upto(n - 1)

print(sum_upto(5))  # Expected: 15
print(sum_upto(1))  # Expected: 1
