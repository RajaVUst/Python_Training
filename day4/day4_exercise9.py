# method to calculate the sum of prices
def total_cost(*prices):
    return sum(prices)

# With 2 prices
print(total_cost(100, 250))

# With 5 prices
print(total_cost(50, 75, 125, 200, 300))

'''
OUTPUT:
350
750
'''