n = int(input("Enter a whole number: "))

factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print(f"{n}! = {factorial}")
