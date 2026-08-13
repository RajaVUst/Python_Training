# input length of three sides
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# check if the sides can form a valid triangle
if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Not a valid triangle")