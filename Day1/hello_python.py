# Store personal information
name='aiswarya'
age = 23
height_m = 1.65
has_coded_before = True

# Display the data types of the variables
print(type(name))
print(type(age))
print(type(height_m))
print(type(has_coded_before))

# Getting favourite number from the user
fav_str = input("Enter your favourite number: ")

# Convert the input from string to integer and multiply by 2
fav_num = int(fav_str)
print(fav_num * 2)

 # Display personal information using  f-string
print(f"{name} is {age} years old and {height_m}m tall.")
