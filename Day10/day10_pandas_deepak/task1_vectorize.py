# Perform vectorized operations with NumPy
import numpy as np
 
prices = [
    10, 20, 30, 40, 50,
    60, 70, 80, 90, 100,
    15, 25, 35, 45, 55,
    65, 75, 85, 95, 105
]
 
taxed_prices_loop = []
 
for price in prices:
    taxed_price = price * 1.08
    taxed_prices_loop.append(taxed_price)
 
print("Taxed prices using loop:")
print(taxed_prices_loop)
prices_array = np.array(prices)
taxed_prices_numpy = prices_array * 1.08
 
print("\nTaxed prices using NumPy:")
print(taxed_prices_numpy)
above_50 = taxed_prices_numpy[taxed_prices_numpy > 50]
print("\nTaxed prices above 50:")
print(above_50)
 
numbers = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
 
row_sums = numbers.sum(axis=1)
column_sums = numbers.sum(axis=0)
 
print("\nArray:")
print(numbers)
print("\nRow sums:")
print(row_sums)
print("\nColumn sums:")
print(column_sums)
 
 
# Output:
# Taxed prices using loop:
# [10.8, 21.6, 32.400000000000006, 43.2, 54.0, 64.80000000000001, 75.60000000000001, 86.4, 97.2, 108.0, 16.200000000000003, 27.0, 37.800000000000004, 48.6, 59.400000000000006, 70.2, 81.0, 91.80000000000001, 102.60000000000001, 113.4]
 
# Taxed prices using NumPy:
# [ 10.8  21.6  32.4  43.2  54.   64.8  75.6  86.4  97.2 108.   16.2  27.
#   37.8  48.6  59.4  70.2  81.   91.8 102.6 113.4]
 
# Taxed prices above 50:
# [ 54.   64.8  75.6  86.4  97.2 108.   59.4  70.2  81.   91.8 102.6 113.4]
 
# Array:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
 
# Row sums:
# [10 26 42]
 
# Column sums:
# [15 18 21 24]