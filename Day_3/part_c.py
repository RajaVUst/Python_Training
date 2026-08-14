#Exercise 4: Positive, negative, or zero

number = int(input("Enter a number : "))

if number < 0:
    print("It is negative")
elif number == 0:
    print("It is zero")
else:
    print("It is positive")

#Exercise 5: Even or odd 

number = int(input("Enter a number : "))

if number % 2 == 0:
    print("It is even")
else :
    print("It is odd")

#Exercise 6: Leap year checker 

year = 2004

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")

#Exercise 7: Largest of three numbers 

a = 10
b = 7
c = 77

if a > b and a > c:
    print("A is the greatest number")
elif b > a and b > c:
    print("B is the greatest number")
else:
    print("C is the greatest number")  

#Exercise 8: Simple grading system 

marks = 77
 
if marks >= 90: 
    print("Grade A") 
elif marks >= 75: 
    print("Grade B") 
elif marks >= 60: 
    print("Grade C") 
elif marks >= 40:
    print("Grade D")
else: 
    print("Grade F") 

#Exercise 9: Triangle validity check

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Not a valid triangle")