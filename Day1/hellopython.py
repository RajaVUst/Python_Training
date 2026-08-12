name = "saikiran"
age = 19
height_m = 1.75
has_coded_before = False

print(type(name))
print(type(age))
print(type(height_m))
print(type(has_coded_before))


# Ask the user for their favourite number
fav_str = input("Enter your favourite number: ")


# Convert the input from string to integer and multiply it by 2
fav_num = int(fav_str)
print(fav_num * 2)


# Combine multiple variables using an f-string
print(f"{name} is {age} years old and {height_m}m tall.")