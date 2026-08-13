# input three numbers
a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")

# if-block to find the greatest of the three numbers
if a>b>c or a>c>b:
    print(f"{a} is greater.")
elif b>a>c or b>c>a:
    print(f"{b} is greater.")
else:
    print(f"{c} is greater.")