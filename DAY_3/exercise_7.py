a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>b:
    if a>c:
        print(f"{a} is larger")
    else:
         print(f"{c} is larger")   
else:
    if b>c:
        print(f"{b} is larger")
    else:
        print(f"{c} is larger")   

