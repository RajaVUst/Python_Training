name = "Shoaib"
age = 24
height_m = 1.65
has_coded_before = False

print(type(name))
print(type(age))
print(type(height_m))
print(type(has_coded_before))

fav_str = input("Enter your favourite number: ")
fav_num = int(fav_str)
print(fav_num * 2)

print(f"{name} is {age} years old and {height_m}m tall.")


#Q1
p_name = "Shoaib"
p_age = 24
p_city = "Chennai"
p_is_employed = True

print(f"Name: {p_name}")
print(f"Age: {p_age}")
print(f"City: {p_city}")
print(f"Employed: {p_is_employed}")

#Q2
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

#Q3
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")


#Q4
n = 17
is_even = (n % 2 == 0)
print(f"{n} is even: {is_even}")


#Q5
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius:.1f}C is equal to {fahrenheit:.1f}F")


#Q6
bill_amount = float(input("Enter total bill amount: "))
num_people = int(input("Enter number of people splitting: "))
wants_tip = (input("Add 10% tip? (yes/no): ") == "yes")

if wants_tip:
    bill_amount = bill_amount * 1.10

share = bill_amount / num_people
print(f"Each person pays: {share:.2f}")


#Q7
a = 5
b = 10

temp = a
a = b
b = temp
print(f"Method 1 -> a: {a}, b: {b}")

a = 5
b = 10

a, b = b, a
print(f"Method 2 -> a: {a}, b: {b}")


#Q8
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")


#Q9
print(7 // 2)
print(7 % 2)
print(2 ** 3)
print(10 > 5 and 3 > 5)
print(10 > 5 or 3 > 5)
print(not True)
print("5" + "5")
print(5 == 5.0)


#Q10
product_name = "Notebook"
price = 149.0
in_stock = True

print(f"{product_name} — ₹{price:.2f} ({'In Stock' if in_stock else 'Out of Stock'})")


#Q11
weight_kg = float(input("Enter your weight in kg: "))
height_m2 = float(input("Enter your height in metres: "))

bmi = weight_kg / (height_m2 ** 2)
print(f"Your BMI is: {bmi:.1f}")


#Q12
n = 15
div_by_3 = (n % 3 == 0)
div_by_5 = (n % 5 == 0)
div_by_both = div_by_3 and div_by_5

print(f"Divisible by 3: {div_by_3}")
print(f"Divisible by 5: {div_by_5}")
print(f"Divisible by both: {div_by_both}")


#Q13
usd_amount = float(input("Enter amount in USD: "))
rate = float(input("Enter conversion rate (USD to INR): "))

inr_amount = usd_amount * rate
print(f"${usd_amount:,.2f} = ₹{inr_amount:,.2f}")


#Q14
score1 = float(input("Enter first test score: "))
score2 = float(input("Enter second test score: "))
score3 = float(input("Enter third test score: "))

average = (score1 + score2 + score3) / 3
has_passed = (average >= 40)

print(f"Average: {average:.1f} | Passed: {has_passed}")