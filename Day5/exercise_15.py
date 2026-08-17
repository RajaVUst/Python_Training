cubes = [n ** 3 for n in range(1, 11)]
even_cubes = [n ** 3 for n in range(1, 11) if n % 2 == 0]
print(cubes)
print(even_cubes)

# output
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# [8, 64, 216, 512, 1000]
