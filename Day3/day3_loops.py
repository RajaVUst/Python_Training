#Exercise 10 — Multiplication table
n = 7

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

#Exercise 11 — Sum of first N natural numbers
n = 10
total = 0

for i in range(1, n + 1):
    total = total + i

print(total)

#Exercise 12 — Sum of digits
n = 1234
total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print(total)

#Exercise 13 — Countdown with a while loop
n = 5

while n >= 1:
    print(n)
    n = n - 1

print("Liftoff!")

#Exercise 14 — Right-angled triangle pattern
n = 5

for i in range(1, n + 1):
    print("*" * i)

#Exercise 15 — Vowel counter
text = "Python Readiness Training"
vowel_count = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowel_count = vowel_count + 1

print(vowel_count)