
input_num = int(input("Enter a number : "))
if input_num > 0 :
    print("The number is positive")
elif input_num < 0:
    print("The number is negative ")
else :
    print("The number is zero")

num = 91;

if num % 2 == 0 :
    print("The number is even")
else :
    print("The number is odd")

input_year = int(input("Enter a year : "))

if input_year % 4 == 0 :
    if input_year % 100 == 0 :
        if input_year % 400 == 0 :
            print("This is a leap year")
        else : 
            print("This is not a leap year")
    else :
        print("This is a leap year")
else : 
    print("This is not a leap year")

a = 23
b = 42
c = 69

if a > b :
    if a > c :
        print("a is greatest")
    else : 
        print("c is greatest")
else : 
    if b > c :
        print("b is greatest")
    else :
        print("c is greatest")  

marks = int(input("Enter your marks: "))

if marks >= 90 :
    print("Grade : A")
elif marks > 74 :
    print("Grade : B")
elif marks > 59 :
    print("Grade : C")
elif marks > 39 :
    print("Grade : D")
else :
    print("Grade : F")

side1 = int(input("Enter the length of triangle : "))
side3 = int(input("Enter the length of triangle : "))
side2 = int(input("Enter the length of triangle : "))

if (side1 + side2) > side3 and side2 + side3 > side1 and side1 + side3 > side2 :
    print("this is a valid triangle")
else : 
    print("This is not a valid triangle")

 
