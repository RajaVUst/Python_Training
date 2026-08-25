import numpy as np
import time

# --------------------------------------------------
# 1. Plain Python list
# --------------------------------------------------

prices = [
    10, 15, 20, 25, 30,
    35, 40, 45, 50, 55,
    60, 65, 70, 75, 80,
    85, 90, 95, 100, 110
]

# Loop-based solution
taxed_prices_loop = []

for price in prices:
    taxed_prices_loop.append(price * 1.08)

print("Loop-based:")
print(taxed_prices_loop)


# Output:
# Loop-based:
# [10.8, 16.2, 21.6, 27.0, 32.4, 37.8, 43.2, 48.6,
#  54.0, 59.4, 64.8, 70.2, 75.6, 81.0, 86.4, 91.8,
#  97.2, 102.6, 108.0, 118.8]


# --------------------------------------------------
# 2. NumPy vectorized operation
# --------------------------------------------------

price_array = np.array(prices)

taxed_prices_numpy = price_array * 1.08

print("\nNumPy:")
print(taxed_prices_numpy)


# Output:
# NumPy:
# [ 10.8  16.2  21.6  27.   32.4  37.8  43.2  48.6
#   54.   59.4  64.8  70.2  75.6  81.   86.4  91.8
#   97.2 102.6 108.  118.8]


# Check that both approaches give the same result
print("\nResults are same:")
print(np.allclose(taxed_prices_loop, taxed_prices_numpy))


# Output:
# Results are same:
# True


# --------------------------------------------------
# 3. Boolean masking
# --------------------------------------------------

threshold = 50

above_threshold = taxed_prices_numpy[taxed_prices_numpy > threshold]

print("\nTaxed prices above 50:")
print(above_threshold)


# Output:
# Taxed prices above 50:
# [ 54.   59.4  64.8  70.2  75.6  81.   86.4  91.8
#   97.2 102.6 108.  118.8]


# --------------------------------------------------
# 4. 2D NumPy array
# --------------------------------------------------

data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

row_sums = data.sum(axis=1)
column_sums = data.sum(axis=0)

print("\nRow sums:")
print(row_sums)

print("\nColumn sums:")
print(column_sums)


# Output:
# Row sums:
# [100 260 420]
#
# Column sums:
# [150 180 210 240]


# --------------------------------------------------
# Stretch goal: speed comparison
# --------------------------------------------------

large_prices = [10] * 1_000_000

start = time.perf_counter()

large_taxed_loop = []

for price in large_prices:
    large_taxed_loop.append(price * 1.08)

loop_time = time.perf_counter() - start


large_array = np.array(large_prices)

start = time.perf_counter()

large_taxed_numpy = large_array * 1.08

numpy_time = time.perf_counter() - start

print("\nLoop time:", loop_time)
print("NumPy time:", numpy_time)
print("Speedup:", loop_time / numpy_time, "times")