numbers = range(1, 11)

cubes = [n ** 3 for n in numbers]

even_cubes = [n ** 3 for n in numbers if n % 2 == 0]

print("Cubes:", cubes)
print("Even cubes:", even_cubes)


#output:
'''Cubes: [1, 8, 27, 64, 125,
216, 343, 512, 729, 1000]
Even cubes: [8, 64, 216, 512, 1000]'''