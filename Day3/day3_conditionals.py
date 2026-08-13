# Step 1 - A single condition
age = 20

if age >= 18:
    print("You can vote")


# Step 2 - Adding an else
age = 15

if age >= 18:
    print("You can vote")
else:
    print("Not old enough yet")


# Step 3 - Chaining with elif
marks = 67

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# Step 4 - Combining conditions
temperature = 33
is_raining = False

if temperature > 30 and not is_raining:
    print("Good day for a walk")
else:
    print("Maybe stay in")


# Step 5 - A first loop
for i in range(1, 6):
    print(f"Iteration {i}")


# Step 6 - Loop plus condition
for n in range(1, 11):
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

#Exercise 4 — Positive, negative, or zero
num = -7

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#Exercise 5 — Even or odd
n = 23

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#Exercise 6 — Leap year checker
year = 2024

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

#Exercise 7 — Largest of three numbers
a = 12
b = 45
c = 30

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

#Exercise 8 — Simple grading system
score = 82

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

#Exercise 9 — Triangle validity check
a = 5
b = 7
c = 9

if a + b > c and b + c > a and a + c > b:
    print("Valid triangle")
else:
    print("Not a valid triangle")