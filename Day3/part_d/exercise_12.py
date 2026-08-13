n = int(input("Enter a whole number :"))

total = 0
while n >0:
    digit = n % 10 
    total += digit
    n = n // 10

print(f"Sum is {total}")


