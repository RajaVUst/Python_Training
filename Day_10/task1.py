# Task 1: Vectorization and NumPy Operations

import numpy as np

prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
          110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

taxed_loop = []

for price in prices:
    taxed_loop.append(price * 1.08)

prices_np = np.array(prices)

taxed_vectorized = prices_np * 1.08

high_prices = taxed_vectorized[taxed_vectorized > 50]

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

row_sums = matrix.sum(axis=1)
col_sums = matrix.sum(axis=0)

print(taxed_loop)
print(taxed_vectorized)
print(high_prices)
print(row_sums)
print(col_sums)

# Output:
# [10.8, 21.6, 32.4, 43.2, 54.0, ..., 216.0]
# [ 10.8  21.6  32.4  43.2  54.   ... 216. ]
# [ 54.   64.8  75.6  86.4  97.2 108.  118.8 129.6 140.4 151.2
#  162.  172.8 183.6 194.4 205.2 216. ]
# [10 26 42]
# [15 18 21 24]