def total_cost(*numbers):
    print(numbers)
    return sum(numbers)

sum=total_cost(1,2,3,4)

print(f"sum={sum}")

# OUTPUT

# (1, 2, 3, 4)
# sum=10