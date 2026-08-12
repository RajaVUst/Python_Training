# Part B - Guided Hello Python Lab

# Declaring variables of different primitive data types
name = "Varsha"
age = 23
height_m = 1.65
has_coded_before = True


# Printing the data types of each variablegit status

print(type(name))
print(type(age))
print(type(height_m))
print(type(has_coded_before))


# Taking user input for favourite number
fav_str = input("Enter your favourite number: ")


# Converting the input string to integer and multiplying by 2
fav_num = int(fav_str)
print(fav_num * 2)


# Using an f-string to combine variables into a sentence
print(f"{name} is {age} years old, {height_m} meters tall, and has coded before: {has_coded_before}.")