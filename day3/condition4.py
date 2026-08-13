# largest of 3 numbers 
num1=int(input("enter the number1"))
num2=int(input("enter the number2"))
num3=int(input("enter the number3"))

if num1>=num2 and num1>=num3:
    print(f"{num1} is greater")
elif num2>=num1 and num2>=num3:
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")

