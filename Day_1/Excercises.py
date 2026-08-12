# Exercise_01

name = input("")
age = int(input(""))
city = input("")
employed = input("")

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Employed:", employed)


# Exercise_02

integer_value = 10
float_value = 10.0
string_value = "10"
boolean_value = 10 == 10
string_boolean = "True"

print(type(integer_value), type(float_value), type(string_value), type(boolean_value), type(string_boolean))


# Exercise_03

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

print("The Addition is:", first_number + second_number)
print("The Subtraction is:", first_number - second_number)
print("The Multiplication is:", first_number * second_number)
print("The Division is:", first_number / second_number)


# Exercise_04

number = int(input("Enter the number: "))

is_even = number % 2 == 0

print(f"{number} is even: {is_even}")


# Exercise_05

celsius_temperature = float(input("Enter temperature in Celsius: "))

fahrenheit_temperature = celsius_temperature * 9 / 5 + 32

print(f"{celsius_temperature:.1f}C = {fahrenheit_temperature:.1f}F")


# Exercise_06

bill_amount = float(input("Enter the bill amount: "))
number_of_people = int(input("Enter the number of people to split the bill: "))

add_tip = input("Wanna add 10% tip? (yes/no): ").lower() == "yes"

if add_tip:
    bill_amount = bill_amount * 1.1

amount_per_person = bill_amount / number_of_people

print(f"Each person's share: {amount_per_person:.2f}")


# Exercise_07

first_number = int(input("Enter the 1st number: "))
second_number = int(input("Enter the 2nd number: "))

print("Before the swap:", first_number, second_number)

temporary_value = first_number
first_number = second_number
second_number = temporary_value

print("After the swap:", first_number, second_number)

first_number, second_number = second_number, first_number

print("After the 2nd swap:", first_number, second_number)


# Exercise_08

rectangle_length = float(input("Please enter the length: "))
rectangle_width = float(input("Please enter the width: "))

rectangle_area = rectangle_length * rectangle_width
rectangle_perimeter = 2 * (rectangle_length + rectangle_width)

print("The Area of the Rectangle is:", rectangle_area)
print("The Perimeter of the Rectangle is:", rectangle_perimeter)


# Exercise_09

print(7 // 2)
print(7 % 2)
print(2 ** 3)
print(10 > 5 and 3 > 5)
print(10 > 5 or 3 > 5)
print(not True)
print("5" + "5")
print(5 == 5.0)


# Exercise_10

item_name = input("Enter the name of the item: ")
item_price = float(input("Enter the price of the item: "))

item_available = bool(input("Is the item available..? "))

if item_available:
    print(f"{item_name} --> ₹{item_price:.2f} (In Stock)")
else:
    print(f"{item_name} --> ₹{item_price:.2f} (Out of Stock)")


# Exercise_11

body_weight = float(input("Enter the weight: "))
body_height = float(input("Enter the height: "))

body_mass_index = body_weight / (body_height ** 2)

print(f"The calculated BMI is: {body_mass_index:.1f}")


# Exercise_12

number = int(input("Enter the number: "))

divisible_by_three = number % 3 == 0
divisible_by_five = number % 5 == 0

divisible_by_both = divisible_by_three and divisible_by_five

print(divisible_by_both)


# Exercise_13

dollar_amount = float(input("Enter the money in dollars: "))

exchange_rate = 95.38
rupee_amount = exchange_rate * dollar_amount

print(f"{dollar_amount}$ is equal to ₹{rupee_amount:,.2f}")


# Exercise_14

first_number = float(input("Enter the 1st number: "))
second_number = float(input("Enter the 2nd number: "))
third_number = float(input("Enter the 3rd number: "))

average_value = (first_number + second_number + third_number) / 3

if average_value >= 40:
    print(f"Average: {average_value:.2f} | Passed: True")
else:
    print(f"Average: {average_value:.2f} | Passed: False")