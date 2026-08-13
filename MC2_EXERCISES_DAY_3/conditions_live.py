# If-else

age = 20

if age>=18:
    print("You can vote")
else:
    print("NO...")

# Chaining with elif

grade = 90

if grade<50:
    print("D")
elif grade<70:
    print("C")
elif grade<90:
    print("B")
else:
    print("A")

# Combining conditions

temperature = 30
is_it_raining = True

if temperature<35 and is_it_raining:
    print("Not good for walk")
else:
    print("Good for walk")

# First Loop

for i in range(10):
    print(f"iterations {i}")

#Loop 

for n in range(1, 11): 
    if n % 2 == 0: 
        print(f"{n} is even") 
    else: 
        print(f"{n} is odd") 