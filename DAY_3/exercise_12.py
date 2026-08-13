n = int(input("Enter a positive whole number: "))

total = 0
while n > 0:
    total = total + (n % 10)
    n = n // 10

print(f"Sum of digits is {total}")
