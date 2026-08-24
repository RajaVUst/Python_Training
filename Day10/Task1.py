# Day 10 - Task 1

import numpy as np
from time import perf_counter

# Plain Python list containing 20 prices
prices = [
    12, 25, 39, 45, 50,
    57, 63, 72, 81, 95,
    110, 125, 140, 160, 180,
    210, 240, 275, 320, 400
]

# 1. Loop-based calculation
loop_taxed_prices = []

for price in prices:
    taxed_price = price + (price * 8 / 100)
    loop_taxed_prices.append(taxed_price)

print("Loop-based taxed prices:")
print(loop_taxed_prices)


# 2. NumPy vectorized calculation
prices_array = np.array(prices, dtype=float)

vectorized_taxed_prices = prices_array * 1.08

print("\nVectorized taxed prices:")
print(vectorized_taxed_prices)


# Check that both results are identical
print(
    "\nAre both results identical?",
    np.allclose(loop_taxed_prices, vectorized_taxed_prices)
)


# 3. Boolean masking
threshold = 50

prices_above_threshold = vectorized_taxed_prices[
    vectorized_taxed_prices > threshold
]

print(f"\nTaxed prices above {threshold}:")
print(prices_above_threshold)


# 4. Two-dimensional NumPy array
numbers = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("\n2D array:")
print(numbers)

# axis=1 calculates across the columns of each row
row_sums = numbers.sum(axis=1)

# axis=0 calculates down the rows of each column
column_sums = numbers.sum(axis=0)

print("\nRow sums:")
print(row_sums)

print("\nColumn sums:")
print(column_sums)

#output
'''
Loop-based taxed prices:
[12.96, 27.0, 42.12, 48.6, 54.0, 61.56, 68.04, 77.76, 87.48, 102.6, 118.8, 135.0, 151.2, 172.8, 194.4, 226.8, 259.2, 297.0, 345.6, 432.0]

Vectorized taxed prices:
[ 12.96  27.    42.12  48.6   54.    61.56  68.04  77.76  87.48 102.6
 118.8  135.   151.2  172.8  194.4  226.8  259.2  297.   345.6  432.  ]

Are both results identical? True

Taxed prices above 50:
[ 54.    61.56  68.04  77.76  87.48 102.6  118.8  135.   151.2  172.8
 194.4  226.8  259.2  297.   345.6  432.  ]

2D array:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

Row sums:
[10 26 42]

Column sums:
[15 18 21 24]
'''