name= 'pavan'
age = 23
height = 5.4
city = 'hyderabad'
employed = True
has_coded_before = False
print(type(name))
print(type(age))
print(type(height))
print(type(has_coded_before))
fav_str = input("Enter a favourite number:")
fav_num = int(fav_str)
print(fav_num * 2)
print(f"{name} is {age} years old.")


#excercise 1
print(f" {name}")
print(f" {age}")
print(f" {city}")
print(f" {employed}")

#excercise 2
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

#excerise 3
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: ")) 
print( 'addition :', num1 + num2)
print( 'sub :', num1 - num2)
print( 'multiplying :', num1 * num2)
print( 'dividing :', num1 / num2)

#excerise 4
n=17
if n%2 == 0:
    print("even")
else:
    print("odd")

#excerise 5

temperature = float(input("Enter temperature in celsius : "))
fahrenheit = temperature * 9/5 + 32
print(f"Temperatur in celsius {temperature} converted in fahernheit {fahrenheit}")

#excersie 6
total_bill = float(input("ENter the total bill : "))
num_of_people = int(input("Enter Number of people : "))
givetip = bool(input("If you want to give tip for waiter then Yes or No : "))
tip = (10/100)*total_bill

if givetip == True:
    bill_per_person = (total_bill + tip) / num_of_people
    print(f"Each person should be pay : {bill_per_person}")
else : 
    bill_per_person = total_bill / num_of_people
    print(f"Each person should be pay : {bill_per_person}")


#excersie 7
a=5
b=10
 a,b = b,a
print('a = ', a)
print('b = ', b)
temp = a
a = b
b = temp
print('a =',a)
print('b= ',b)


#excersie 8
length = float(input("Enter height of the rectangle : "))
width = float(input("Enter width of the rectangle : "))
Area = length * width
Perimeter = 2 * (length + width)
print(f"Area of the rectangle : {Area}")
print(f"perimeter of the rectangle : {Perimeter}")


#excersie 9
print(7 // 2)
print(7 % 2)
print(2 ** 3)
print(10 > 5 and 3 > 5)
print(10 > 5 or 3 > 5)
print(not True)
print("5" + "5")
print(5 == 5.0)



#excersie 10 
product = input("Enter the product name :")
price = float(input("Enter price of the product :"))
in_stock = bool(input("Is there in stock or not : "))
if in_stock == True: 
    print(f"{product} is cost of {price:.2f} now in stock") 
else:
    print(f"{product} is cost of {price:.2f} now it is out of stock")


#excersie 11
weight = float(input("Enter weight in KG : "))
height = float(input("Enter weight in Meters : "))
BMI = weight/(height**2)
print(f"BMI of your body is : {BMI:.1f} ")


#excersie 12
n = 15
div_by_3 = (n % 3 == 0)
div_by_5 = (n % 5 == 0)
div_by_both = div_by_3 and div_by_5
print(div_by_both)

#excersie 13
amount = float(input("Enter amount in US Dollars: "))
conversion_rate = float(input("Enter conversion rate: "))

rupees = amount * conversion_rate

print(f"Indian Rupees: ₹{rupees:.2f}")

#excersie 14

maths_marks = float(input("Enter Maths marks: "))
english_marks = float(input("Enter English marks: "))
science_marks = float(input("Enter Science marks: "))

avg_marks = (maths_marks + english_marks + science_marks) / 3

has_passed = avg_marks >= 40

print(f"Average: {avg_marks:.1f} | Passed: {has_passed}")