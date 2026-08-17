cubes = [number ** 3 for number in range(1, 11)]

even_cubes = [
    number ** 3
    for number in range(1, 11)
    if number % 2 == 0
]

print("Cubes:", cubes)
print("Even cubes:", even_cubes)

'''
output
Score 84 has grade B.


'''