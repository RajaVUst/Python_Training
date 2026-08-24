#task1                                                                  
import numpy as np
prices = [12, 25, 30, 45, 55, 60, 75, 80, 22, 18,
          95, 110, 40, 35, 65, 70, 28, 50, 85, 100]
 
# PART 1: LOOP-BASED APPROACH
taxed_prices_loop = []
for price in prices:
    taxed_prices_loop.append(price * 1.08)
print("PART 1 OUTPUT")
print(taxed_prices_loop)
print()
'''
PART 1 OUTPUT
[12.96, 27.0, 32.4, 48.6, 59.4, 64.8, 81.0, 86.4,
23.76, 19.44, 102.6, 118.8, 43.2, 37.8, 70.2,
75.6, 30.24, 54.0, 91.8, 108.0]'''
 
 
# PART 2: NUMPY VECTORIZED APPROACH
prices_array = np.array(prices)
taxed_prices_vectorized = prices_array * 1.08
print("PART 2 OUTPUT")
print(taxed_prices_vectorized)
print()
print("Results identical:")
print(np.allclose(taxed_prices_loop, taxed_prices_vectorized))
print()
high_prices = taxed_prices_vectorized[taxed_prices_vectorized > 50]
print("Taxed prices above 50:")
print(high_prices)
print()
data = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
row_sums = data.sum(axis=1)
column_sums = data.sum(axis=0)
print("2D Array:")
print(data)
print()
print("Row sums:")
print(row_sums)
print()
print("Column sums:")
print(column_sums)
'''
PART 2 OUTPUT
[ 12.96  27.    32.4   48.6   59.4   64.8   81.
  86.4   23.76  19.44 102.6  118.8   43.2   37.8
  70.2   75.6   30.24  54.    91.8  108.  ]
 
Results identical:
True
 
Taxed prices above 50:
[ 59.4  64.8  81.   86.4 102.6 118.8  70.2
  75.6  54.   91.8 108. ]
 
2D Array:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
 
Row sums:
[10 26 42]
 
Column sums:
[15 18 21 24]
'''
 
#note
'''
The loop-based approach applies the 8% tax by processing
each price individually using a for loop.
 
The NumPy vectorized approach applies the same tax to the
entire array with a single expression, eliminating the need
for an explicit loop.
 
The loop-based and vectorized results are identical, as
verified using np.allclose().
 
Boolean masking selects only the taxed prices greater than
50 without using any loop or if statement.
 
The 2D NumPy array demonstrates aggregation:
.sum(axis=1) calculates row sums and
.sum(axis=0) calculates column sums.
 
Vectorization is one of NumPy's key advantages because it
makes code shorter, cleaner, and significantly faster for
large numerical datasets.
'''