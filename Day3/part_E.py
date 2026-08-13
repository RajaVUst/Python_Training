# Exercise 16: FizzBuzz
for i in range(1,51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else: 
        print(i)

# Exercise 17: Reverse an integer
num = 5885
original = num
sum = 0
while num > 0:
    sum = sum*10 + num % 10
    num //= 10
print("Reversed number",sum)

# Exercise 18: Palindrome check for an integer
if sum == original:
    print("Palindrome")
else:
    print("Not a palindrome")

# Exercise 19: Prime number check
for i in range(2,sum-1):
    if sum % i == 0:
        print("Not a Prime")
        break
else:
    print("It's a Prime")

# Exercise 20: Print primes in a range
for i in range(2,51):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)

# Exercise 21: Factorial of a number
n = 6
fact = 1
while n>0:
    fact *= n
    n -= 1
print("Factorial is",fact)

# Exercise 22: Fibonacci series
first = 0
second = 1

for i in range(15):
    print(first)
    first,second = second,first + second

# Exercise 23: Simple currency converter
rupees = 100
currency = "GBP"

if currency == "USD":
    print("Dollars",round(rupees*0.010,2))
elif currency == "EUR":
    print("Euroes", round(rupees*0.009,2))
elif currency == "GBP":
    print("Pounds", round(rupees*0.0078,2))

# Exercise 24: Number guessing game (fixed target)
li = [4,8,23,6,15,9]
var = 6

for i in li:
    if var == i:
        print("Correct!")
        break
    elif var > i:
        print("Too low")
    else:
        print("Too high")

# Exercise 25: Pyramid of numbers
for i in range(1,var):
    for j in range(1,i+1):
        print(j, end=' ')
    print()