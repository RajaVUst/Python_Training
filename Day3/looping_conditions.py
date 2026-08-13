
# Step 1 - A single condition
age = 20
if age >= 18:
    print("You can vote")

# Step 2 - Adding an else
age = 15
if age >= 18:
    print("You can vote")
else:
    print("Not old enough yet")

# Step 3 - Chaining with elif
marks = 67
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

# Step 4 - Combining conditions
temperature = 33
is_raining = False
if temperature > 30 and not is_raining:
    print("Good day for a walk")
else:
    print("Maybe stay in")

# Step 5 - A first loop
for i in range(1, 6):
    print(f"Iteration {i}")

# Step 6 - Loop plus condition
for n in range(1, 11):
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")