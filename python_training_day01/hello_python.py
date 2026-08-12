#storing basic information
name = "Deepa"
age = 22
height_m = 1.65
has_coded_before = False

#printing type of each variable
print(type(name))
print(type(age))
print(type(height_m))
print(type(has_coded_before))

#favourite number
fav_str = input("Enter your favourite number: ")

#convert string to an integer
fav_num = int(fav_str)

#multiply the number by 2
print(fav_num * 2)

#displaying information using f-string
print(f"{name} is {age} years old and {height_m}m tall.")