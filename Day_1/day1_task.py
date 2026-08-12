 
#Q1 Personal Info Card
name = "Shashi"
age = 23
city = "Mysore"
is_employed = True
 
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Employed: {is_employed}")
 
 
#Q2 Type Detective
a = 10          
b = 10.0        
c = "10"      
d = 10 ==10    
e = "True"      
print(type(a), type(b), type(c), type(d), type(e))
 
#Q3 Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
 
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")
 
#Q4 Even or Odd (without if)
n = 17
is_even = (n % 2 == 0)
print(f"{n} is even: {is_even}")
 
#Q5 Unit Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius:.1f}°C is {fahrenheit:.1f}°F")
 
#Q6 Restaurant Bill Splitter
total_bill = float(input("Enter total bill: "))
num_people = int(input("Enter number of people: "))
wants_tip = (input("Add 10% tip? (yes/no): ") == "yes")
 
final_bill = total_bill * 1.10 if wants_tip else total_bill
share = final_bill / num_people
 
print(f"Each person pays: {share:.2f}")
 
#Q7 Variable Swap
a = 5
b = 10
 
temp = a
a = b
b = temp
print(a, b)  
 
a, b = b, a
print(a, b)  
 
#Q8 Rectangle Calculator
length = float(input("Enter length: "))
width = float(input("Enter width: "))
 
area = length * width
perimeter = 2 * (length + width)
 
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
 
 
#Q9 Predict the Output
print(7 // 2)              
print(7 % 2)                
print(2 ** 3)                
print(10 > 5 and 3 > 5)      
print(10 > 5 or 3 > 5)        
print(not True)              
print("5" + "5")              
print(5 == 5.0)              
 
#Q10 Formatted Product Label
name = "Notebook"
price = 149.0
in_stock = True
 
print(f"{name} — ₹{price:.2f} ({'In Stock' if in_stock else 'Out of Stock'})")
 
#Q11 BMI Calculator
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))
 
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.1f}")
 
#Q12 Divisibility Checker
n = 15
div_by_3 = (n % 3 == 0)
div_by_5 = (n % 5 == 0)
div_by_both = div_by_3 and div_by_5
 
print(f"Divisible by 3: {div_by_3}")
print(f"Divisible by 5: {div_by_5}")
print(f"Divisible by both: {div_by_both}")
 
#Q13 Currency Converter
usd_amount = float(input("Enter amount in USD: "))
rate = float(input("Enter conversion rate: "))
 
inr_amount = usd_amount * rate
print(f"${usd_amount:,.2f} = ₹{inr_amount:,.2f}")
 
#Q14 Student Report Line
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
 
average = (score1 + score2 + score3) / 3
has_passed = (average >= 40)
 
print(f"Average: {average:.1f} | Passed: {has_passed}")
 