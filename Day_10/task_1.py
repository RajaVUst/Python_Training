import numpy as np
import time

# --------------------------------------------------
# 1. Plain Python list of 20 product prices
# --------------------------------------------------
prices = [
    12.99, 25.50, 8.75, 45.00, 60.25,
    18.40, 72.10, 34.99, 15.50, 99.99,
    22.75, 56.80, 41.25, 10.00, 85.60,
    29.95, 67.30, 14.49, 52.20, 38.75
]

tax_rate = 0.08

# --------------------------------------------------
# 2. Loop-based version
# --------------------------------------------------
taxed_prices_loop = []

for price in prices:
    taxed_prices_loop.append(price * (1 + tax_rate))

print("Loop-based taxed prices:")
print(taxed_prices_loop)

# --------------------------------------------------
# 3. NumPy vectorized version
# --------------------------------------------------
prices_np = np.array(prices)

taxed_prices_vectorized = prices_np * (1 + tax_rate)

print("\nVectorized taxed prices:")
print(taxed_prices_vectorized)

# Verify both methods produce identical results
are_equal = np.allclose(
    taxed_prices_loop,
    taxed_prices_vectorized
)

print("\nResults identical?", are_equal)

# --------------------------------------------------
# 4. Boolean masking (no loop, no if statement)
# --------------------------------------------------
threshold = 50

high_prices = taxed_prices_vectorized[
    taxed_prices_vectorized > threshold
]

print(f"\nTaxed prices above {threshold}:")
print(high_prices)

# --------------------------------------------------
# 5. Small 2D NumPy array
# --------------------------------------------------
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

row_sums = matrix.sum(axis=1)
column_sums = matrix.sum(axis=0)

print("\n2D Array:")
print(matrix)

print("\nRow sums:")
print(row_sums)

print("\nColumn sums:")
print(column_sums)

# --------------------------------------------------
# Stretch Goal
# --------------------------------------------------
n = 1_000_000

large_list = list(range(n))
large_array = np.array(large_list)

# Loop timing
start = time.perf_counter()

loop_result = []
for value in large_list:
    loop_result.append(value * 1.08)

loop_time = time.perf_counter() - start

# Vectorized timing
start = time.perf_counter()

vectorized_result = large_array * 1.08

vector_time = time.perf_counter() - start

speedup = loop_time / vector_time

print("\nPerformance Comparison")
print(f"Loop time: {loop_time:.6f} seconds")
print(f"Vectorized time: {vector_time:.6f} seconds")
print(f"Speedup: {speedup:.2f}x")