#Exercise 10: Multiplication Table
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

#Exercise 11: Sum of First N Natural Numbers
n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)

#Exercise 12: Sum of Digits

n = int(input("Enter a positive number: "))

digit_sum = 0

while n > 0:
    digit_sum += n % 10
    n //= 10

print("Sum of digits =", digit_sum)

#Exercise 13: Countdown with a While Loop

n = int(input("Enter starting number: "))

while n >= 1:
    print(n)
    n -= 1

print("Liftoff!")


#Exercise 14: Right-Angled Triangle Pattern

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

#Exercise 15: Vowel Counter

text = input("Enter a word or *entence: ")

count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Vowel count =", count)