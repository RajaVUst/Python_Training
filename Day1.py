#1. Personal Information
name = "Logesh"
age = 21
city = "Trivandrum"
employed = True
 
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Employed: {employed}")
 
 
#2. Type detective
a = 10
b = 10.0
c = "10"
d = 10 == 10
e = "True"
 
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
 
 
#3. Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
 
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
 
 
#4. Even or Odd(Without if)
n=20
even = (n % 2 == 0)
print(f"{n} : {even}")
 
 
#5. Unit converter
cel = float(input("Temperature in Celsius: "))
f = cel * 9 / 5 + 32
print(f"{cel:.1f}°C is {f:.1f}°F")
 

#6. Restaurant Bill Calculator
amount = float(input("Enter total bill amount: "))
people = int(input("People splitting the bill: "))
tip = (input("Add 10% tip? (yes/no): ") == "yes")
 
tip_amount = amount * 0.10 * tip  
total_with_tip = amount + tip_amount
share = total_with_tip / people
 
print(f"Total bill: {total_with_tip:.2f}")
print(f"Each person pays: {share:.2f}")
 
 
#7. Variable Swap
a = 5
b = 10
 
#using temporary variable
temp = a
a = b
b = temp
print(f"a: {a}, b: {b}")
 
# method2
a = 5
b = 10
 
#Python multiple-assignment shortcut
a, b = b, a
print(f"a: {a}, b: {b}")
 
 
#8. Rectangle calculator
length = float(input("Rectangle length: "))
width = float(input("Rectangle width: "))
area = length * width
perimeter = 2 * (length + width)
 
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
 
 
#9.Predict the output
print(7 // 2)                  
print(7 % 2)                  
print(2 ** 3)          
print(10 > 5 and 3 > 5)      
print(10 > 5 or 3 > 5)        
print(not True)              
print("5" + "5")              
print(5 == 5.0)  
 
 
#10. Formatted Product Label
product_name = "Bat"
price = 149.0
stock = True
print(f"{product_name} — ₹{price:.2f} ({'In Stock' if stock else 'Out of Stock'})")
 
 
#11. BMI Calculator
weight = float(input("Enter weight : "))
height= float(input("Enter height : "))
 
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.1f}")
 
 
#12. Devisiblity Checker
n = 15
div_by_3 = (n % 3 == 0)
div_by_5 = (n % 5 == 0)
div_by_both = div_by_3 and div_by_5
print(f"{n} divisible by 3: {div_by_3}")
print(f"{n} divisible by 5: {div_by_5}")
print(f"{n} divisible by both: {div_by_both}")
 
 
#13. Currency Converter
usd_amount = float(input("Enter amount in USD: "))
conversion_rate = float(input("Enter conversion rate (USD to INR): "))
 
inr_amount = usd_amount * conversion_rate
print(f"${usd_amount:,.2f} = ₹{inr_amount:,.2f}")
 
 
#14. Student Report Line
score1 = float(input("Enter test score 1: "))
score2 = float(input("Enter test score 2: "))
score3 = float(input("Enter test score 3: "))
 
avg = (score1 + score2 + score3) / 3
passed = (avg >= 40)
 
print(f"Average: {avg:.1f} | Passed: {passed}")