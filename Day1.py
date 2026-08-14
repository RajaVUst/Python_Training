#Exercise_01
# name=input("")
# Age=int(input(""))
# city=input("")
# Employed=input("")
# print(f"Name: ",name)
# print(f"Age: ",Age)
# print(f"City: ",city)
# print(f"Employed: ",Employed)
 
#Exercise_02
# a = 10
# b = 10.0
# c = "10"
# d = 10 == 10
# e = "True"
# print(type(a)," ",type(b)," ",type(c)," ",type(d), " ",type(e))
 
#Exercise_03
# n1 = float(input("Enter first number: "))
# n2 = float(input("Enter second number: "))
# print(f"The Addition is: ",n1+n2)
# print(f"The Subtraction is: ",n1-n2)
# print(f"The Multiplication is: ",n1*n2)
# print(f"The Divison is: ",n1/n2)
 
#Exercise_04
# n = int(input("Enter the number: "))
# is_even = (n % 2 == 0)
# print(f"{n} is even: {is_even}")
 
#Exercise_05
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = celsius * 9 / 5 + 32
# print(f"{celsius:.1f}C = {fahrenheit:.1f}F")
 
 
 
#exercise 6
# bill=float(input("Enter the bill amount: "))
# split=int(input("Enter the number of people to split the bill: "))
# tip = input("wanna add 10% tip? (yes/no): ").lower() == "yes"
# if tip:
#     bill = bill * 1.1
# share = bill / split
# print(f"Each person's share: {share:.2f}")
 
#Exercise_07
# Method 1: temporary variable
# a=int(input("Enter the 1st number: "))
# b=int(input("Enter the 2nd number: "))
# print("Before the swap: ",a,b)
# temp = a
# a = b
# b = temp
# print("After the swap: ",a,b)
# Method 2: Python shortcut
# a, b = b, a
# print("After the 2nd swap: ",a,b)
 
#Exercise_08
# length = float(input("please enter the value: "))
# width = float(input("please enter the value: "))
# Area = length * width
# Perimeter = 2 * (length + width)
# print("The Area of the Rectangle with the given values are: ",Area)
# print("The perimeter of the Rectangle with the given values are: ",Perimeter)
 
#Exercise_09
# print(7 // 2)
# print(7 % 2)
# print(2 ** 3)
# print(10 > 5 and 3 > 5)
# print(10 > 5 or 3 > 5)
# print(not True)
# print("5" + "5")
# print(5 == 5.0)
 
#Exercise_10
# name = input("enter the name of the item: ")
# price = float(input("Enter the price of the value: "))
# in_stock = bool(input("is the item is available..? "))
# if in_stock:
#     print(f"{name} --> ₹{price:.2f} (In Stock)")
# else:
#     print(f"{name} --> ₹{price:.2f} (Out of Stock)")
 
#Exercise_11
# weight = float(input("Enter the value: "))
# height = float(input("Enter the value: "))
# BMI = weight / (height ** 2)
# print(f"The calculated BMI is: {BMI:.1f}")
 
#Exercise_12
# n = int(input("Enter the number: "))
# div_by_3 = (n % 3 == 0)
# div_by_5 = (n % 5 == 0)
# div_by_both = div_by_3 and div_by_5
# print(div_by_both)
 
# #Exercise_13
# USD = float(input("Enter the money in dollars:- "))
# rupees = 95.38 * USD
# print(f"{USD}$ is equals to {rupees:,.2f} in rupees.")
 
#Exercise_14
a=float(input("Enter the 1st number: "))
b=float(input("Enter the 2nd number: "))
c=float(input("Enter the 3rd number: "))
avg = (a+b+c)/3
if avg >= 40:
    print(f"Average: {avg} | Passed: {avg>=40}")
else:
    print(f"Average: {avg} | Passed: {avg>=40}")
 

 