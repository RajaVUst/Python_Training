# 9: Triangle validity check
a=int(input("Enter side1: "))
b=int(input("Enter side2: "))
c=int(input("Enter side3: "))

if a+b>c and b+c>a and a+c>b:
    print(f"Triangle with lengths{a,b,c} is a valid triangle")
else:
    print("It is an Invalid Triangle")