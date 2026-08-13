n = int(input("Enter a positive whole number: "))

original = n
reversed_n = 0
while n > 0:
    reversed_n = reversed_n * 10 + (n % 10)
    n = n // 10

print(f"Reversed: {reversed_n}")
