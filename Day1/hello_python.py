name = "Aditi"
age = 24
height_m = 1.65
has_coded_before = False

# Type of each variable
print(type(name))
print(type(age))
print(type(height_m))
print(type(has_coded_before))


# Get the user's favourite number
fav_str = input("Enter your favourite number:")

# Convert the favourite number from string to integer
fav_num = int(fav_str)
print("favourite number is :",fav_num)

# Multiply the converted number by 2
print("favourite number multiply by 2 :",fav_num * 2)

# Displaying  personal information using an f-string
print(f"{name} is {age} years old and {height_m}m tall.")

print("{2} is {0} years old and {1}m tall.".format(name, age, height_m))
print("{} is {} years old and {}m tall.".format(name, age, height_m))

info = str.format("{} is {} years old and {}m tall", name, age, height_m)
print(info)