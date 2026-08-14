#Exercise 16: FizzBuzz

for i in range(1, 51):
   if i % 15 == 0:
        print("Fiz*Buzz")
   elif i % 3 == 0:
        print("Fizz")
   elif i % 5 == 0:
      print("Buzz")
   else:
    print(i)

#Exercise 17: Reverse an Integer
n = int(input("Enter a number: "))

reversed_n = 0

while n > 0:
    reversed_n = reversed_n * 10 + (n % 10)
    n //= 10

print("Reversed number =", reversed_n)

#Exercise 18: Palindrome Check for an Integer

n = int(input("Enter a number: "))

original = n
reversed_n = 0

while n > 0:
    reversed_n = reversed_n * 10 + (n % 10)
    n //= 10

if original == reversed_n:
    print("Palindrome")
else:
    print("Not a palindrome")


#Exercise 19: Prime Number Check

n = int(input("Enter a number greater than 1: "))

is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")

#Exercise 20: Print Primes in a Range

for num in range(2, 51):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)

#Exercise 21: Factorial of a Number

n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial =", factorial)


#Exercise 22: Fibonacci Series

a = 0
b = 1

for i in range(15):
    print(a, end=" ")
    a, b = b, a + b


#Exercise 23: Simple Currency Converter

amount_inr = float(input("Enter amount in INR: "))
currency = input("Enter target currency (USD/EUR/GBP): ").upper()

if currency == "USD":
    converted = amount_inr / 83
    print(f"USD {converted:.2f}")

elif currency == "EUR":
    converted = amount_inr / 90
    print(f"EUR {converted:.2f}")

elif currency == "GBP":
    converted = amount_inr / 105
    print(f"GBP {converted:.2f}")

else:
    print("Invalid currency")