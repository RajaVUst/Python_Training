# Exercise 12 - Sum of Digits
number = 1234
digit_sum = 0
while number > 0:
    digit_sum += number % 10
    number //= 10

print(f"Sum of Digits: {digit_sum}")