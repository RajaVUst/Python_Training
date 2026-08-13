a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a+b>c and a+c>b and b+c>a:
    print(f"{a},{b},{c} can form a triangle")
else:
    print(f"{a},{b},{c} cannot form a triangle")