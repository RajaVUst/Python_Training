#Exercise 1   Personal Info Card 
name="yesh"
city="hyderabad"
age=22
employed=True
print(f"Hi, I'm {name}")
print("I am from {}".format(city))
message=str.format("I am {0} years old",age)
print(message)

#Exercise 2  Type Detective
a = 10 
b = 10.0 
c = "10" 
d = 10 == 9
e = "True" 
print(type(d))

#Exercise 3   Simple Calculator
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
print(f"The sum of {num1} and {num2} is {num1+num2}")
print(f"The difference of {num1} and {num2} is {num1-num2}")
print(f"The product of {num1} and {num2} is {num1*num2}")
print(f"The division of {num1} and {num2} is {num1/num2}")


#Exercise 4    Even or Odd (without if)
n=10
is_even = n % 2 == 0
print(f"The number {n} is even: {is_even}")
is_odd = n % 2 != 0
print(f"The number {n} is odd: {is_odd}")


#Exercise 5   Unit Converter
celcius=float(input("Enter temperature in Celsius:"))
fahrenheit=(celcius*9/5)+32
print(f"{celcius:.1f} degree Celsius is equal to {fahrenheit:.1f} degree Fahrenheit")


#Exercise 6    Restaurant Bill Splitter
total_bill=float(input("Enter total bill amount:"))
tip=total_bill*0.10
wants_tip=(input("Do you want to add a tip? (yes/no):")=="yes")
if wants_tip:
    total_bill+=tip
    print(f"Tip amount: {tip:.2f}")
print(f"Total amount: {total_bill:.2f}")


#Exercise 7    Variable Swap
a=5
b=10
temp=a
a=b
b=temp
print("After swapping: a =", a, "b =", b)
a,b=b,a
print("After swapping: a =", a, "b =", b)

#Exercise 8    Rectangle Calculator
length=float(input("Enter the length of the rectangle: "))
width=float(input("Enter the width of the rectangle: "))
print("Area of the rectangle is: ", length*width)
print("Perimeter of the rectangle is: ", 2*(length+width))


#Exercise 9    Predict the Output 
print(7 // 2) 
print(7 % 2) 
print(2 ** 3) 
print(10 > 5 and 3 > 5) 
print(10 > 5 or 3 > 5) 
print(not True) 
print("5" + "5") 
print(5 == 5.0) 


#Exercise 10  Formatted Product Label
name='notebook'
price=149.00000
in_stock=True
print(f"{name}-${price:.2f}{'In_Stock' if in_stock else 'Out of Stock'}")


#Exercise 11   BMI Calculator
weight=float(input("Enter the weight in kg: "))
height=float(input("Enter the height in m: "))
bmi=weight/(height**2)
print("BMI is: ", bmi)

#Exercise 12    Divisibility Checker
n = 15 
div_by_3 = (n % 3 == 0) 
div_by_5 = (n % 5 == 0) 
div_by_both = div_by_3 and div_by_5
print(f"Number {n} is divisible by 3: {div_by_3}")
print(f"Number {n} is divisible by 5: {div_by_5}")
print(f"Number {n} is divisible by both 3 and 5: {div_by_both}")

#Exercise 13   Currency Converter 
amount_in_usdollars = float(input("Enter the amount in US dollars: "))
exchange_rate = float(input("Enter the exchange rate (1 USD to target currency): "))
amount_in_target_currency = amount_in_usdollars * exchange_rate
print(f"Amount in target currency: {amount_in_target_currency:.2f}")

#Exercise 14   Student Report Line
test1=float(input("Enter the first number: "))
test2=float(input("Enter the second number: "))
test3=float(input("Enter the third number: "))
average=(test1+test2+test3)/3
has_passed=average>=40
print("Average score: ", average)
print("Has passed: ", has_passed)