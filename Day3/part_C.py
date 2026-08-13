# Exercise 4: positive, negative or zero
num = -5
if num>0:
    print("positive")
elif num == 0:
    print("zero")
else:
    print("negative")

# Exercise 5: Even or odd
n = 37
if n%2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 6: Leap year checker
year = 2012

if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

# Exercise 7: Larget of three numbers
a,b,c = 12,56,38

if a>b and a>c:
    print(a," is maximum") 
elif b>c and b>a:
    print(f"{b} is maximum")
else:
    print(c," is maximum")

# Exercise 8: Simple grading system
score = 97
if score >=90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
elif score >= 40:
    print("D")
else:
    print("E")

# Exercise 9: Triangle validity check
if a+b>c or b+c>a or a+c>b:
    print("Valid triangle")
else:
    print("Not a valid triangle")