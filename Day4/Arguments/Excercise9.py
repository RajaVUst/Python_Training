# *args — total cost

def total_cost(*prices):
    total = 0
    for price in prices:
        total = total + price

    return total

print(total_cost(100, 200))
print(total_cost(10, 20, 30, 40, 50))

# Output:
# 300
# 150