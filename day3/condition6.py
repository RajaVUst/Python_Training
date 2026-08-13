a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Not a valid triangle")