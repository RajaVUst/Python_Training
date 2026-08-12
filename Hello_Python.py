# assigned a string to the variable
name = "Senin" 
# assigned a integer to the variable 
age = 23
# assigned a float to the variable 
height_m = 1.7
# assigned a bool to the variable 
Has_coded = False
# Printed the stored values using type to identify each value's type
print(type(name), type(age), type(height_m), type(Has_coded))
# created a new variable to enter fav num
fav_str = input("enter your fav number: ")
# used typecast function int() to convert the valur from string to integer
fav_num = int(fav_str)
# Multiplied the integer value by 2 and print
print(fav_num*2)
# Displays name, age and height using f string
print(f"{name} is {age} years old and {height_m} Tall")