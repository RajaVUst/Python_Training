a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a>b and a>c:
    print(f"a that is {a} is the largest number")
elif b>a and b>c:
    print(f"b that is {b} is the largest number")
else:
    print(f"c that is {c} is the largest number")