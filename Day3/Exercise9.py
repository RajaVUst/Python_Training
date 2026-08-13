#Triangle validity check
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if (a + b > c) and (b + c > a) and (a + c > b):
    print("Valid triangle")
else:
    print("Not a valid triangle")