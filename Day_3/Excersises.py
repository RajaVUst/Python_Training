# Python Readiness Training
# Master Class 2 - Conditionals and Loops


# -----------------------------
# Part A - Warm Up
# -----------------------------

# Exercise 1: Type and operator refresher

whole_number = 10
decimal_number = 2.5
text = "Python"

print(f"{whole_number} is of type {type(whole_number)}")
print(f"{decimal_number} is of type {type(decimal_number)}")
print(f"{text} is of type {type(text)}")

print(whole_number / decimal_number)


# Exercise 2: String slicing

my_string = "Python Readiness Training"

print(my_string[:6])
print(my_string[::-1])


# Exercise 3: Comparison practice

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a <= b)


# -----------------------------
# Part B - Conditionals
# -----------------------------

# Step 1

age = 20

if age >= 18:
    print("You can vote")


# Step 2

age = 15

if age >= 18:
    print("You can vote")
else:
    print("Not old enough yet")


# Step 3

marks = 67

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# Step 4

temperature = 33
is_raining = False

if temperature > 30 and not is_raining:
    print("Good day for a walk")
else:
    print("Maybe stay in")


# Step 5

for i in range(1, 6):
    print(f"Iteration {i}")


# Step 6

for n in range(1, 11):
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")


# -----------------------------
# Part C - Conditionals Practice
# -----------------------------

# Exercise 4: Positive, negative or zero

number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Exercise 5: Even or odd

number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Exercise 6: Leap year

year = 2024

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# Exercise 7: Largest of three numbers

a = 25
b = 10
c = 18

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


# Exercise 8: Grading system

score = 82

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 60:
    print("Grade C")
elif score >= 40:
    print("Grade D")
else:
    print("Grade F")


# Exercise 9: Triangle validity

a = 5
b = 6
c = 7

if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Not a valid triangle")


# -----------------------------
# Part D - Loops
# -----------------------------

# Exercise 10: Multiplication table

n = 7

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# Exercise 11: Sum of first N numbers

n = 10
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)


# Exercise 12: Sum of digits

n = 1234
total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Sum of digits:", total)


# Exercise 13: Countdown

n = 5

while n >= 1:
    print(n)
    n = n - 1

print("Liftoff!")


# Exercise 14: Right-angled triangle

n = 5

for row in range(1, n + 1):
    for star in range(row):
        print("*", end=" ")
    print()


# Exercise 15: Vowel counter

text = "Python Readiness Training"
count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count = count + 1

print("Number of vowels:", count)


# -----------------------------
# Part E - Combined Logic
# -----------------------------

# Exercise 16: FizzBuzz

for n in range(1, 51):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)


# Exercise 17: Reverse an integer

n = 1234
reversed_n = 0

while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n = n // 10

print("Reversed number:", reversed_n)


# Exercise 18: Palindrome check

n = 12321
original = n
reversed_n = 0

while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n = n // 10

if original == reversed_n:
    print("Palindrome")
else:
    print("Not a palindrome")


# Exercise 19: Prime number check

n = 29
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(n, "is prime")
else:
    print(n, "is not prime")


# Exercise 20: Print primes from 2 to 50

for n in range(2, 51):

    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n)


# Exercise 21: Factorial

n = 5
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("Factorial:", factorial)


# Exercise 22: Fibonacci series

first = 0
second = 1

for i in range(15):
    print(first, end=" ")

    next_number = first + second
    first = second
    second = next_number

print()


# Exercise 23: Currency converter

amount = 10000
currency = "USD"

if currency == "USD":
    converted = amount / 83
    print("USD:", round(converted, 2))

elif currency == "EUR":
    converted = amount / 90
    print("EUR:", round(converted, 2))

elif currency == "GBP":
    converted = amount / 105
    print("GBP:", round(converted, 2))

else:
    print("Currency not supported")
