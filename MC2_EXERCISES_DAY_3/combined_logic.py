#FizzBuzz

for i in range(1,51):
    if i%3==0:
        if i%5==0:
            print("FuzzBuzz")
        else:
            print("fuzz")
    elif i%5==0:
        if i%3==0:
            print("FuzzBuzz")
        else:
            print("Buzz")
    else:
        print(i)

# Reverse a number

n = 54332

reversed_n = 0

while n > 0:
    reversed_n = reversed_n * 10 + (n % 10)
    n = n // 10

print(reversed_n)

# Check paliendrome

num = "123456"

reversed = num[::-1]

if(num==reversed):
    print("Paliendrome")
else:
    print("Not Paliendrome")

# Print Primes in a range

for n in range(2, 51):
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n)

# Check Prime  

n = 7654
is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not Prime")

# Factorial of a number

n = 5

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial)

# Fibonacci Numbers

num = 15

a = 0
b = 1

print(a, b, end=" ")

for i in range(2, num):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

# Currency Converter

amount_inr = 150
currency = "USD"

if currency == "USD":
    converted = amount_inr / 85
elif currency == "EUR":
    converted = amount_inr / 98
elif currency == "GBP":
    converted = amount_inr / 115
else:
    print("Invalid currency")
    converted = None

if converted is not None:
    print(round(converted, 2))