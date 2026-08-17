numbers=[]


for i in range(1,10):
    numbers.append(i**3)

print(f"cubes:{numbers}")

even_numbers_cube=[]

for i in range(1,10):
    num=i**3
    if num%2==0:
        even_numbers_cube.append(num)
    
print(f"even_cubes:{even_numbers_cube}")
    
# OUTPUT

# cubes:[1, 8, 27, 64, 125, 216, 343, 512, 729]
# even_cubes:[8, 64, 216, 512]