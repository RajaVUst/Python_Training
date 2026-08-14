# If-else

age = 20

if age>=18:
    print("You can vote")
else:
    print("NO...")

"""
Output ->
You can vote
"""

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

# A

# Combining conditions

temperature = 30
is_it_raining = True

if temperature<35 and is_it_raining:
    print("Not good for walk")
else:
    print("Good for walk")

"""
Output ->
Not good for walk
"""

# First Loop

for i in range(10):
    print(f"iterations {i}")

"""
Output ->
iterations 0
iterations 1
iterations 2
iterations 3
iterations 4
iterations 5
iterations 6
iterations 7
iterations 8
iterations 9
"""

#Loop 

for n in range(1, 11): 
    if n % 2 == 0: 
        print(f"{n} is even") 
    else: 
        print(f"{n} is odd")

"""
Output ->
1 is odd
2 is even
3 is odd
4 is even
5 is odd
6 is even
7 is odd
8 is even
9 is odd
10 is even
""" 