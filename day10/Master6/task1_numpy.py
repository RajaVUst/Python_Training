import numpy as np

prices = [20, 35, 40, 55, 60, 75, 80, 95, 100, 120,
          25, 45, 65, 85, 105, 125, 30, 50, 70, 90]

# adding tax using a normal loop
taxed_prices_loop = []
for price in prices:
    taxed_prices_loop.append(price * 1.08)

# adding the same tax using numpy
prices_array = np.array(prices)
taxed_prices_numpy = prices_array * 1.08

print("Loop result:", taxed_prices_loop)
print("Numpy result:", taxed_prices_numpy)
print("Both results are same:", np.allclose(taxed_prices_loop, taxed_prices_numpy))

above_70 = taxed_prices_numpy[taxed_prices_numpy > 70]
print("Taxed prices above 70:", above_70)

numbers = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("Row sums:", numbers.sum(axis=1))
print("Column sums:", numbers.sum(axis=0))


# OUTPUT

# Loop result: [21.6, 37.800000000000004, 43.2, 59.400000000000006, 64.80000000000001, 81.0, 86.4, 102.60000000000001, 108.0, 129.60000000000002, 27.0, 48.6, 70.2, 91.80000000000001, 113.4, 135.0, 32.400000000000006, 54.0, 75.60000000000001, 97.2]
# Numpy result: [ 21.6  37.8  43.2  59.4  64.8  81.   86.4 102.6 108.  129.6  27.   48.6
#   70.2  91.8 113.4 135.   32.4  54.   75.6  97.2]
# Both results are same: True
# Taxed prices above 70: [ 81.   86.4 102.6 108.  129.6  70.2  91.8 113.4 135.   75.6  97.2]
# Row sums: [10 26 42]
# Column sums: [15 18 21 24]
