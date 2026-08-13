# --- Exercise 1---
whole_num = 10
decimal_num = 3.5
text = "Python"

print(f"{whole_num} is of type {type(whole_num)}")
print(f"{decimal_num} is of type {type(decimal_num)}")
print(f"{text} is of type {type(text)}")

result = whole_num / decimal_num
print(f"{whole_num} / {decimal_num} = {result}")


# --- Exercise 2 ---
sentence = "Python Readiness Training"

first_word = sentence[0:6]
print(first_word)

reversed_sentence = sentence[::-1]
print(reversed_sentence)


# --- Exercise 3 ---
a = 8
b = 12

print(a == b)
print(a != b)
print(a > b)
print(a <= b)


# --- Exercise 4 ---
num = -7

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# --- Exercise 5 ---
num = 17

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# --- Exercise 6 ---
year = 2024

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# --- Exercise 7 ---
a, b, c = 15, 42, 8

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The largest number is {largest}")


# --- Exercise 8 ---
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


# --- Exercise 9 ---
a, b, c = 5, 7, 9

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid triangle")
else:
    print("Not a valid triangle")


# --- Exercise 10 ---
n = 7

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# --- Exercise 11 ---
n = 20
total = 0

for i in range(1, n + 1):
    total = total + i

print(f"Sum of 1 to {n} is {total}")


# --- Exercise 12 ---
num = 1234
original = num
digit_sum = 0

while num > 0:
    digit_sum = digit_sum + (num % 10)
    num = num // 10

print(f"Sum of digits of {original} is {digit_sum}")


# --- Exercise 13 ---
start = 5

count = start
while count >= 1:
    print(count)
    count = count - 1

print("Liftoff!")


# --- Exercise 14 ---
n = 5

for row in range(1, n + 1):
    for col in range(row):
        print("*", end="")
    print()


# --- Exercise 15 ---
text = "Python Readiness Training"
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count = count + 1

print(f"Number of vowels: {count}")


# --- Exercise 16 ---
for n in range(1, 51):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)


# --- Exercise 17 ---
num = 1234
original = num
reversed_n = 0

while num > 0:
    reversed_n = reversed_n * 10 + (num % 10)
    num = num // 10

print(f"Reverse of {original} is {reversed_n}")


# --- Exercise 18 ---
num = 12321
original = num
temp = num
reversed_n = 0

while temp > 0:
    reversed_n = reversed_n * 10 + (temp % 10)
    temp = temp // 10

if original == reversed_n:
    print(f"{original} is a palindrome")
else:
    print(f"{original} is not a palindrome")


# --- Exercise 19 ---
num = 29
is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")


# --- Exercise 20 ---
for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


# --- Exercise 21 ---
n = 6
factorial = 1

if n == 0:
    print("0! is 1")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
    print(f"{n}! is {factorial}")


# --- Exercise 22 ---
count = 15
a, b = 0, 1

for _ in range(count):
    print(a, end=" ")
    a, b = b, a + b

print()


# --- Exercise 23 ---
amount_inr = 5000
target_currency = "USD"

usd_rate = 0.012
eur_rate = 0.011
gbp_rate = 0.0095

if target_currency == "USD":
    converted = round(amount_inr * usd_rate, 2)
elif target_currency == "EUR":
    converted = round(amount_inr * eur_rate, 2)
elif target_currency == "GBP":
    converted = round(amount_inr * gbp_rate, 2)
else:
    converted = None

if converted is not None:
    print(f"{amount_inr} INR = {converted} {target_currency}")
else:
    print("Unsupported currency")


# --- Exercise 24 ---
secret_number = 42
guesses = [10, 25, 42, 50]

for guess in guesses:
    if guess < secret_number:
        print(f"{guess}: Too low")
    elif guess > secret_number:
        print(f"{guess}: Too high")
    else:
        print(f"{guess}: Correct!")
        break


# --- Exercise 25 ---
n = 5
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()