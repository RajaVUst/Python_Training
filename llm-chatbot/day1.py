
# exercise 1
# name=input("enter name")
# age=int(input("enter age"))
# city=input("enter city")
# is_employed=input()
# print(f"my name is: {name}, my age is: {age}, i am from: {city}, my employment status is: {is_employed}")
# print("My name is:", name, "My age is:", age, "I am from:", city,"My employment status is:", is_employed)
# print("my name is: {}, my age is: {}, i am from: {}, my employment status is: {}".format(name, age, city, is_employed))
# profile = str.format("my name is: {}, my age is: {}, i am from: {}, my employment status is: {}", name, age, city, is_employed)
# print(profile)

#exercise 2
# a = 10 
# b = 10.0 
# c = "10" 
# d = 10 == 10 
# e = "True" 

# print(type(a))
# print(type(b))          
# print(type(c))
# print(type(d))
# print(type(e))


#exercise 3
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))


# print(f"addition: {num1+num2}")
# print(f"subtraction: {num1-num2}")
# print(f"multiplication: {num1*num2}")
# print(f"division: {num1/num2}")


#exercise 4
# n = int(input("Enter a number: ")) 
# is_even = (n % 2 == 0) 
# print(f"{n} is even: {is_even}") 


#exercise 5
# celsius = float(input("Enter temperature in Celsius: "))

# fahrenheit = celsius * 9/5+32

# print(f"{celsius:.1f}C = {fahrenheit:.1f}F")



#exercise 6
# bill=float(input("Enter the bill amount: "))
# split=int(input("Enter the number of people to split the bill: "))
# tip = input("Do you want to add a 10% tip? (yes/no): ").lower() == "yes"

# if tip:
#     bill = bill * 1.10
# share = bill / split
# print(f"Each person's share: {share:.2f}")

#exercise 7






#exercise 8
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))      
# area = length * width
# perimeter = 2 * (length + width)
# print(f"Area: {area}")
# print(f"Perimeter: {perimeter}")



#exercise 9

# print(7 // 2) 
# print(7 % 2) 
# print(2 ** 3) 
# print(10 > 5 and 3 > 5) 
# print(10 > 5 or 3 > 5) 
# print(not True) 
# print("5" + "5") 
# print(5 == 5.0) 




#exercise 10
#item=input("Enter the item name: ")
#price=float(input("Enter the price of the item: "))
#status=bool(input("Enter the status of the item (available/sold out): ").lower() == "available")

#print(f"Item: {item}, Price: {price:.2f}, Status: {'Available' if status else 'Sold Out'}")





#exercise 11

#height=float(input("Enter your height in meters: "))
#weight=float(input("Enter your weight in kilograms: "))
#bmi=weight/(height**2)
#print(f"Your BMI is: {bmi:.1f}")



#exercise 12

#n = 15
#div_by_3 = (n % 3 == 0) 
#div_by_5 = (n % 5 == 0) 
#div_by_both = div_by_3 and div_by_5 
#print("Divisible by 3", div_by_3)
#print("Divisible by 5", div_by_5)
#print("Divisible by both", div_by_both)

#exercise 13
#amount=float(input("Enter the amount in US Dollars: "))
#conversion_rate=float(input("Enter the conversion rate to your local currency: "))
#local_currency=amount*conversion_rate
#print(f"Amount in local currency: {local_currency:.2f}")

#exercise 14
score1 = float(input("Enter first score: "))
score2 = float(input("Enter second score: "))
score3 = float(input("Enter third score: "))
average = (score1 + score2 + score3) / 3
has_passed = average >= 40
print(f"Average: {average:.1f} | Passed: {has_passed}")



