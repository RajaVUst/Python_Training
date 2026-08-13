name = "Elon Musk"
age = 55
city = "Texas"
employed = False

print(f"Name : {name} \n Age : {age} \n City : {city}\n Employed : {employed}")

a = 10
b = 10.0
c = "10"
d = 10 == 10
e = "True"

print(f"a : {type(a)}\n b : {type(b)}\n c : {type(c)}\n d : {type(d)}\n e : {type(e)}\n" )

fav_num1 = float(input("Enter your most favourite number : "))
fav_num2 = float(input("Enter your second most favourite number : "))

print(f"Addition : {fav_num1 + fav_num2} \n Subtraction : {fav_num1 - fav_num2} \n Multiplication : {fav_num1 * fav_num2} \n Division : {fav_num1 / fav_num2} \n ")

n = 99
is_even = (n % 2 == 0)
print(f"{n} is even: {is_even}")

temp = float(input("Enter the temperature in your room : "))
temp_f = temp * (9/5) + 32
print(f"The temperature in celsius is {temp:.1f} and in fahrenheit is {temp_f:.1f}")

total_bill = float(input("Enter the total bill cost : "))
people_count = int(input("Enter the number of people splitting the bill : " ))
add_tip = input("Do you want to add a tip ? (yes / no)")
tip_bool = add_tip == "yes"

total_amount = total_bill

if tip_bool== True:
    total_amount = total_bill +  (total_bill / 10)
    
split = total_amount / people_count
print(f"Each has to pay {split} rupees")
