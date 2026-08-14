def total_cost(*prices):
    return sum(prices)

result1 = total_cost(100, 200)
result2 = total_cost(50, 100, 150, 200, 250)

print("Total for 2 prices:", result1)
print("Total for 5 prices:", result2)


#output:
'''Total for 2 prices: 300
Total for 5 prices: 750'''