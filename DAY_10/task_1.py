# Task 1 - Vectorize It
# NumPy fundamentals: loop vs vectorized, boolean masking, 2D sums, stretch: timing

import numpy as np
import time

prices = [10, 25, 30, 45, 50, 55, 60, 70, 80, 90,
          15, 20, 35, 40, 65, 75, 85, 95, 100, 110]

# ─── 1. Loop-based 8% tax ─────────────────────────────────────────────────────
loop_prices = [p * 1.08 for p in prices]
print("Loop result (first 5):", loop_prices[:5])

# ─── 2. Vectorized 8% tax (no loop) ──────────────────────────────────────────
arr = np.array(prices)
vectorized_prices = arr * 1.08
print("Vectorized result (first 5):", vectorized_prices[:5])

# Verify both give identical results
print("Results match:", np.allclose(loop_prices, vectorized_prices))

# ─── 3. Boolean masking — prices above 50, no loop, no if ────────────────────
threshold = 50
above_threshold = vectorized_prices[vectorized_prices > threshold]
print(f"\nTaxed prices above {threshold}:", above_threshold)

# ─── 4. 2D array row sums and column sums ────────────────────────────────────
grid = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
print("\n2D array:\n", grid)
print("Row sums   (axis=1):", grid.sum(axis=1))   # one sum per row
print("Column sums(axis=0):", grid.sum(axis=0))   # one sum per column

# ─── Stretch: timing loop vs vectorized on 1,000,000 elements ────────────────
big_list = list(range(1, 1_000_001))
big_arr  = np.array(big_list)

start = time.perf_counter()
_ = [x * 1.08 for x in big_list]
loop_time = time.perf_counter() - start

start = time.perf_counter()
_ = big_arr * 1.08
vec_time = time.perf_counter() - start

print(f"\nLoop time:       {loop_time:.4f}s")
print(f"Vectorized time: {vec_time:.4f}s")
print(f"Speedup:         {loop_time / vec_time:.1f}x faster")
