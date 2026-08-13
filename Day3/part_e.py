# Part E - Combined Logic: Classic Problems

# Exercise 16 - FizzBuzz
for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Exercise 17 - Reverse an Integer
number = 1234
original_number = number
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
print(f"Original Number: {original_number}")
print(f"Reversed Number: {reversed_number}")

# Exercise 18 - Palindrome Check
number = 12321
original_number = number
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
if original_number == reversed_number:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Exercise 19 - Prime Number Check
number = 17
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{number} is Prime")
else:
    print(f"{number} is Not Prime")

# Exercise 20 - Print Primes in a Range
for number in range(2, 51):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number)

# Exercise 21 - Factorial
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# Exercise 22 - Fibonacci Series
a = 0
b = 1
for _ in range(15):
    print(a)
    a, b = b, a + b

# Exercise 23 - Currency Converter
amount_in_inr = 1000
target_currency = "USD"
if target_currency == "USD":
    converted_amount = amount_in_inr / 83
elif target_currency == "EUR":
    converted_amount = amount_in_inr / 90
elif target_currency == "GBP":
    converted_amount = amount_in_inr / 105
else:
    converted_amount = None
if converted_amount is not None:
    print(f"{amount_in_inr} INR = {round(converted_amount, 2)} {target_currency}")
else:
    print("Unsupported Currency")

# Exercise 24 - Number Guessing Game
secret_number = 25
guesses = [10, 30, 20, 25, 40]
for guess in guesses:
    if guess < secret_number:
        print(f"{guess}: Too Low")
    elif guess > secret_number:
        print(f"{guess}: Too High")
    else:
        print(f"{guess}: Correct!")
        break

# Exercise 25 - Pyramid of Numbers
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()