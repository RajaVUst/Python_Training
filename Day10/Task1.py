import numpy as np
import time
 
# Product prices
prices = [
    10, 15, 20, 25, 30,
    35, 40, 45, 50, 55,
    60, 65, 70, 75, 80,
    85, 90, 95, 100, 105
]
 
# 1. Loop-based version
taxed_loop = []
 
for price in prices:
    taxed_loop.append(price * 1.08)
 
print("Loop-based result:")
print(taxed_loop)
 
# 2. Vectorized NumPy version
prices_np = np.array(prices)
 
taxed_vectorized = prices_np * 1.08
 
print("\nVectorized result:")
print(taxed_vectorized)
 
# Acceptance check
print("\nResults identical:",
      np.allclose(taxed_loop, taxed_vectorized))
 
# 3. Boolean masking (threshold = 50)
threshold = 50
 
high_prices = taxed_vectorized[taxed_vectorized > threshold]
 
print("\nTaxed prices > 50:")
print(high_prices)
 
# 4. Small 2D array
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
 
row_sums = arr_2d.sum(axis=1)
col_sums = arr_2d.sum(axis=0)
 
print("\n2D Array:")
print(arr_2d)
 
print("\nRow sums:")
print(row_sums)
 
print("\nColumn sums:")
print(col_sums)
 
# Stretch Goal
large_list = list(range(1_000_000))
 
start = time.perf_counter()
loop_result = [x * 1.08 for x in large_list]
loop_time = time.perf_counter() - start
 
large_array = np.array(large_list)
 
start = time.perf_counter()
vector_result = large_array * 1.08
vector_time = time.perf_counter() - start
 
speedup = loop_time / vector_time
 
print(f"\nLoop time: {loop_time:.5f} sec")
print(f"Vectorized time: {vector_time:.5f} sec")
print(f"Speedup: {speedup:.2f}x")
 
# Output
"""
Loop-based result:
[10.8, 16.200000000000003, 21.6, 27.0, 32.400000000000006, 37.800000000000004, 43.2, 48.6, 54.0, 59.400000000000006, 64.80000000000001, 70.2, 75.60000000000001, 81.0, 86.4, 91.80000000000001, 97.2, 102.60000000000001, 108.0, 113.4]
 
Vectorized result:
[ 10.8  16.2  21.6  27.   32.4  37.8  43.2  48.6  54.   59.4  64.8  70.2
  75.6  81.   86.4  91.8  97.2 102.6 108.  113.4]
 
Results identical: True
 
Taxed prices > 50:
[ 54.   59.4  64.8  70.2  75.6  81.   86.4  91.8  97.2 102.6 108.  113.4]
 
2D Array:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
 
Row sums:
[10 26 42]
 
Column sums:
[15 18 21 24]
 
Loop time: 0.05287 sec
Vectorized time: 0.00354 sec
Speedup: 14.92x
"""
 