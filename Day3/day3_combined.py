#Exercise 16 — FizzBuzz
for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#Exercise 17 — Reverse an integer
n = 1234
reversed_n = 0

while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n = n // 10

print(reversed_n)

#Exercise 18 — Palindrome check for an integer
n = 12321
original = n
reversed_n = 0

while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n = n // 10

is_palindrome = (original == reversed_n)
print(is_palindrome)

#Exercise 19 — Prime number check
n = 29
is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

print(is_prime)

#Exercise 20 — Print primes in a range
for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

#Exercise 21 — Factorial of a number
n = 5
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print(factorial)

#Exercise 22 — Fibonacci series
a = 0
b = 1

for i in range(15):
    print(a)
    a, b = b, a + b

#Exercise 23 — Simple currency converter
amount_inr = 1000
target_currency = "USD"

if target_currency == "USD":
    result = round(amount_inr / 83, 2)
elif target_currency == "EUR":
    result = round(amount_inr / 90, 2)
elif target_currency == "GBP":
    result = round(amount_inr / 105, 2)
else:
    result = None

print(result)