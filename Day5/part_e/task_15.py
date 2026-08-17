cubes = [n ** 3 for n in range(1, 11)]
print("Cubes:", cubes)

even_cubes = [n ** 3 for n in range(1, 11) if n % 2 == 0]
print("Even cubes:", even_cubes)


# Cubes: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# Even cubes: [8, 64, 216, 512, 1000]