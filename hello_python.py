# Declaring four variables with different data types
name="Anu"
age=23
height = 5.11
has_coded_before = False

# Printing the data types of the variables
print(type(name))
print(type(age))
print(type(height))
print(type(has_coded_before))

# Taking user input for favorite number
fav_str=input("Enter your favorite number: ")

# Converting the input string to an integer
fav_num=int(fav_str)
print(fav_num)

# 
print(f"{name} is {age} years old and {height}m tall")