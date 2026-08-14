number =int(input("enter the number:"))
sum = 0
while number > 0:
    rem = number % 10
    sum = sum + rem
    number = number//10
print(f"The sum of digit is {sum}")