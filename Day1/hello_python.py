# Step 2: Declare four variables, one of each primitive type
name = "Navya Samudrala"
age = 23
height_m = 1.65
has_coded_before = False

# Step 3: Print each variable's type to confirm Python's inference
print(type(name))
print(type(age))
print(type(height_m))
print(type(has_coded_before))

# Step 4: Ask the user for their favourite number (input() always returns a str)
fav_str = input("Enter your favourite number: ")

# Step 5: Cast the string to an int, then print it doubled
fav_num = int(fav_str)
print(fav_num * 2)

# Step 6: Combine at least three variables into one readable f-string
print(f"{name} is {age} years old and {height_m}m tall.")