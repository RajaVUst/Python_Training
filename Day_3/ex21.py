# 21: Factorial of a number
num=int(input("Enter a number: "))
fact=1
a=num
while num>=1:
    fact=fact*num
    num-=1
print(f"Factorial of number {a}:",{fact})