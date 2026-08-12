#This is the details of the user assigned to variables
name = "Hari" 
age = 22 
height_m = 1.70
has_coded_before = True 

#This is to print type of the variables
print(type(name)) 
print(type(age)) 
print(type(height_m)) 
print(type(has_coded_before)) 

#This is to input the favourite number of the user and print it
fav_num = int(input("Enter your favourite number: "))
print(fav_num) 

#This is to print the details of the user using f-string
print(f"{name} is {age} years old and {height_m}m tall.") 