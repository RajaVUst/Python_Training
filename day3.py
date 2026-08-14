# Q1
whole_number = 10
decimal_number = 2.5
text = "Python"

print(f"{whole_number} is of type {type(whole_number)}")
print(f"{decimal_number} is of type {type(decimal_number)}")
print(f"{text} is of type {type(text)}")
print(f"Division Result: {whole_number / decimal_number}")

# Q2
training = "Python Readiness Training"

print(training[0:6])
print(training[::-1])

# Q3
a = 15
b = 10

print(a == b)
print(a != b)
print(a > b)
print(a <= b)

# Q4
num = -5

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Q5
n = 12

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q6
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Q7
a = 45
b = 78
c = 21

if a >= b and a >= c:
    print(f"Largest: {a}")
elif b >= a and b >= c:
    print(f"Largest: {b}")
else:
    print(f"Largest: {c}")

# Q8
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

# Q9
a = 5
b = 6
c = 7

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Not a Valid Triangle")

# Q10
n = 5

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Q11
n = 10
total = 0

for i in range(1, n + 1):
    total += i

print(f"Sum = {total}")

# Q12
n = 1234
sum_digits = 0

while n > 0:
    sum_digits += n % 10
    n //= 10

print(f"Sum of Digits = {sum_digits}")

# Q13
count = 5

while count >= 1:
    print(count)
    count -= 1

print("Liftoff!")

# Q14
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

# Q15
text = "Python Readiness Training"
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print(f"Vowel Count: {count}")

# Q16
for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Q17
n = 1234
original = n
reverse = 0

while n > 0:
    reverse = reverse * 10 + (n % 10)
    n //= 10

print(f"Reverse of {original} = {reverse}")

# Q18
n = 12321
original = n
reverse = 0

while n > 0:
    reverse = reverse * 10 + (n % 10)
    n //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# Q19
n = 17
is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not Prime")

# Q20
for num in range(2, 51):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")

print()

# Q21
n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Factorial = {factorial}")

# Q22
a = 0
b = 1

for i in range(15):
    print(a, end=" ")
    a, b = b, a + b

print()

# Q23
amount_inr = 1000
currency = "USD"

if currency == "USD":
    converted = amount_inr / 83
elif currency == "EUR":
    converted = amount_inr / 90
elif currency == "GBP":
    converted = amount_inr / 105
else:
    converted = None

if converted is not None:
    print(f"{amount_inr} INR = {round(converted, 2)} {currency}")
else:
    print("Unsupported Currency")

# Q24
secret_number = 25
guesses = [10, 18, 25, 40]

for guess in guesses:
    if guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too Low")
    else:
        print("Correct!")
        break

# Q25
rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()