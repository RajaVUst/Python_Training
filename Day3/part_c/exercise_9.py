a = float(input("Enter the side a :"))
b = float(input("Enter the side b :"))
c = float(input("Enter the side c :"))

if a + b > c and a + c > b and b + c > a :
    print ("Valid triangle")
else:
    print("Not a valid triangle")

