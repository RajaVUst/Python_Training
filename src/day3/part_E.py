
for number in range(1, 51):

    if number % 15 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)

n = int(input("Enter a positive whole number: "))

reversed_n = 0

while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n = n // 10

print("Reversed number:", reversed_n)

num = int(input("Enter a positive whole number: "))

original = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

if original == reversed_num:
    print("Palindrome")
else:
    print("Not a palindrome")

no = int(input("Enter a number greater than 1: "))

is_prime = True

for number in range(2, no):

    if no % number == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not Prime")

for n in range(2, 51):

    is_prime = True

    for number in range(2, n):

        if n % number == 0:
            is_prime = False
            break

    if is_prime:
        print(n)

n1 = int(input("Enter a whole number: "))

factorial = 1

for number in range(1, n1 + 1):
    factorial = factorial * number

print("Factorial:", factorial)

first = 0
second = 1

for i in range(15):

    print(first)

    next_number = first + second
    first = second
    second = next_number

amount = float(input("Enter amount in INR: "))
currency = input("Enter target currency (USD/EUR/GBP): ")

if currency == "USD":
    converted = amount * 0.010
    print("Amount in USD:", round(converted, 2))

elif currency == "EUR":
    converted = amount * 0.0091
    print("Amount in EUR:", round(converted, 2))

elif currency == "GBP":
    converted = amount * 0.0077
    print("Amount in GBP:", round(converted, 2))

else:
    print("Invalid currency")

