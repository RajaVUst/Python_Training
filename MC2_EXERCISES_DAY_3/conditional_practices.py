num = 6

# Positive or negative

if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")

# Positive

# Odd or Even

if num%2==0:
    print("Even")
else:
    print("Odd")

# Even

# Leap Year

year = 2026

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

# Not a Leap Year

# Largest Number

a = 10
b = 20
c = 30

if a>b:
    if a>c:
        print("A largest")
    else:
        print("C largest")
elif b>a:
    if b>c:
        print("B largest")
    else:
        print("C largest")

# C Largest

# Grading System

score = 85

if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
elif score >= 40:
    print("D")
else:
    print("F")

# B

# Valid Triangle

a = 30
b = 20
c = 40

if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Not a valid triangle")

# Valid Triangle