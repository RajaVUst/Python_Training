# name="surendra"
# age=24
# height=5.8
# code_before=True
# print(type(name))
# print(type(age))
# print(type(height))
# print(type(code_before))


# fav_number="10"
# fav=int(fav_number)
# print(fav*2)



# name="surendra"
# city="trivandrum"
# age=23
# print(f"my name is {name}. am from {city} city, i am {age }years old ")


#exe-1
# name="surendra"
# age=23
# city="hyd"
# employed=True
# print(f"Name:{name}")
# print(f"Age:{age}")
# print(f"City:{city}")
# print(f"Employed:{employed}")

#exe-------------2
# a=10
# b=10.0
# c="10"
# d=10 == 10
# e="True"
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))


#exe-------------3
# num1=float(input("Enter first number: "))
# num2=float(input("Enter second number: "))
# add=num1+num2
# sub=num1-num2
# mul=num1*num2
# div=num1/num2
# print(f"Addition of two number ={add}")
# print(f"Substarction of two number ={sub}")
# print(f"MUltification of two number ={mul}")
# print(f"Division of two number ={div}")

#exe--------------4
# n=int(input("Enter number: "))
# if n%2==0:
#     print("even")
# else:
#     print("odd")    


#exe----------5

# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = celsius * 9 / 5 + 32
# print(f"Celsius: {celsius:.1f}C, Fahrenheit: {fahrenheit:.1f}F")

#exe-----------------6
# total_bill=float(input("Enter the bill:"))
# total_per=int(input("Enter total persons:"))
# wants_tip=input("Do you want to add 10 % tip? (yes/no)").lower()=="yes"
# if wants_tip:
#     total_bill=total_bill*1.10
# share=total_bill/total_per
# print(f"each person share {share:.2f}")











#exe---------7
# a=10
# b=20
# temp=a
# a=b
# b=temp
#a,b=b,a
# print("a=",a)
# print("b=",b)


#exe-------------8
# length=float(input("Enter the length:"))
# width=float(input("Enter the width:"))
# area=(length*width)
# perimeter=2*(length*width)
# print(f"Area of the rectangle: {area}")
# print(f"Perimeter of the rectangle: {perimeter}")


#exe-------------9
# print(7 // 2) 
# print(7 % 2) 
# print(2 ** 3) 
# print(10 > 5 and 3 > 5) 
# print(10 > 5 or 3 > 5) 
# print(not True) 
# print("5" + "5") 
# print(5 == 5.0) 


#exe----------------10
# name="notebok"
# price=149.000088
# in_stock=False
# print(f"{name}-{price:.2f}rs ({"In stock" if in_stock else "out of stock"})")



#exe------11
# weight=float(input("Enter weight: "))
# height=float(input("Enter height: "))
# bmi=weight/(height**2)
# print(f"BMI={bmi:.1f}")



#exe----------12
# n = int(input("Enter teh number: ")) 
# div_by_3 = (n % 3 == 0) 
# div_by_5 = (n % 5 == 0) 
# div_by_both = div_by_3 and div_by_5 
# print(f"The given number is divisible by 3 : {div_by_3}")
# print(f"The given number is divisible by 5 : {div_by_5}")
# print(f"The given number is divisible by 3 & 5 : {div_by_both}")

#exe---------13
# amount=float(input("enter amount in US dollars:"))
# rate=float(input ("Enter rate cnversion:"))
# rupees=amount * rate
# print(f"Indian Rupees: {rupees:,.2f}rs")



#exe------------14
# score1=float(input("enter score 1:"))
# score2=float(input("enter score 2:"))
# score3=float(input("enter score 3:"))
# average=(score1+score2+score3)/3
# has_passed=average>=40
# print(f"Average:{average}| Has passed:{has_passed}")