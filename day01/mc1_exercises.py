# 1 Declaring four variables with different data types
name="Anu"
age=23
city = "Raichur"
employed = True
print(f"My name is {name}")
print(f"My age is {age}")
print(f"I live in {city}")
print(f"Am I employed? {employed}")

# 2 printing the type of varibales declared.
a = 10 
b = 10.0 
c = "10" 
d = 10 == 10 
e = "True" 
print(type(a),type(b),type(c),type(d),type(e))

# 3 Simple calculator
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))
print(f"Addition = {num1 + num2}")
print(f"Subtraction = {num1 - num2}")
print(f"Multiplication = {num1 * num2}")
print(f"Division = {num1 / num2}")

# 4 Even or Odd (without if)  
n = 17 
is_even = (n % 2 == 0) 
print(f"{n} is even: {is_even}") 

# 5 Unit Converter  
temperature = float(input("Enter temperature in Celsius: "))
fahrenheit = (temperature * 9/5) + 32
print(f"{temperature:.1f}°C is equal to {fahrenheit:.1f}°F")

# 6 Resturant Bill splitter
total_bill = float(input("Enter total bill amount: "))
num_people = int(input("Enter number of people: "))
wants_tip=input("Do you want to add 10% tip? (yes/no):").lower() == "yes"
tip = total_bill * 0.10 * wants_tip
final_bill = total_bill + tip
bill_per_person = final_bill / num_people
print(f"Each person should pay: {bill_per_person:.2f}")

# 7 Variable swap
# method 1
a = 10
b = 5
temp = a
a = b
b = temp
print(a,b)
# method 2
a=10
b=5
a,b=b,a
print(a,b)

# 8 Rectangular calculator
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area of the rectangle is :{area}")
print(f"Perimeter of the rectangle is:{perimeter}")

# 9 Predict the output
print(7 // 2) 
print(7 % 2) 
print(2 ** 3) 
print(10 > 5 and 3 > 5) 
print(10 > 5 or 3 > 5) 
print(not True) 
print("5" + "5") 
print(5 == 5.0) 

# 10 Formatted product label
name = "Dairy Milk"
price = 149.00
in_stock = True
print(f" The product {name} costs Rs.{price:.2f} is {'In Stock' if in_stock else 'Out of Stock'}")

# 11 BMI calculator
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.1f}")

# 12  Divisibility Checker  
n = 15 
div_by_3 = (n % 3 == 0) 
div_by_5 = (n % 5 == 0) 
div_by_both = div_by_3 and div_by_5 
print(f"Divisible by 3: {div_by_3}")
print(f"Divisible by 5: {div_by_5}")
print(f"Divisible by both: {div_by_both}")

# 13 Currency Converter
amount = float(input("Enter amount in us dollars: "))
conversion_rate = float(input("Enter conversion rate to Indian currency: "))
converted_amount = amount * conversion_rate
print(f"{amount:.2f} USD is equal to {converted_amount:.2f} in Indian currency.")

# 14 Student Report Line
score1=float(input("Enter score  1: "))
score2=float(input("Enter score  2: "))
score3=float(input("Enter score  3: "))
average_score = (score1 + score2 + score3) / 3
has_passed = average_score >= 40
print(f"Average Score: {average_score:.1f} | passed: {has_passed}")