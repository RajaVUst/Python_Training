cubes=[x**3 for x in range(1,11)]
even_cubes=[x**3 for x in range(1,11) if x%2==0]
print(cubes)
print(even_cubes)
#output
"""
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
[8, 64, 216, 512, 1000]
"""