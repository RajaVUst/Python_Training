import numpy as np

prices = [
    10, 15, 20, 25, 30,
    35, 40, 45, 50, 55,
    60, 65, 70, 75, 80,
    85, 90, 95, 100, 120
]


#  Loop-based approach
taxed_prices_loop = []

for price in prices:
    taxed_price = price * 1.08
    taxed_prices_loop.append(taxed_price)

print("Loop-based result:")
print(taxed_prices_loop)


#  NumPy vectorized approach
prices_array = np.array(prices)

taxed_prices_numpy = prices_array * 1.08

print("\nNumPy vectorized result:")
print(taxed_prices_numpy)


# Check that both results are the same
print("\nResults are identical:")
print(np.allclose(taxed_prices_loop, taxed_prices_numpy))


#  Boolean masking
threshold = 50

above_threshold = taxed_prices_numpy[taxed_prices_numpy > threshold]

print("\nTaxed prices above 50:")
print(above_threshold)


#  2D NumPy array
data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

row_sums = data.sum(axis=1)

column_sums = data.sum(axis=0)

print("\n2D Array:")
print(data)

print("\nRow sums:")
print(row_sums)

print("\nColumn sums:")
print(column_sums)




# Loop-based result:
# [10.8, 16.200000000000003, 21.6, 27.0, 32.400000000000006, 37.800000000000004, 43.2, 48.6, 54.0, 59.400000000000006, 64.80000000000001, 70.2, 75.60000000000001, 81.0, 86.4, 91.80000000000001, 97.2, 102.60000000000001, 108.0, 129.60000000000002]

# NumPy vectorized result:
# [ 10.8  16.2  21.6  27.   32.4  37.8  43.2  48.6  54.   59.4  64.8  70.2
#   75.6  81.   86.4  91.8  97.2 102.6 108.  129.6]

# Results are identical:
# True

# Taxed prices above 50:
# [ 54.   59.4  64.8  70.2  75.6  81.   86.4  91.8  97.2 102.6 108.  129.6]

# 2D Array:
# [[ 10  20  30  40]
#  [ 50  60  70  80]
#  [ 90 100 110 120]]

# Row sums:
# [100 260 420]

# Column sums:
# [150 180 210 240]