num =int(input("enter the number:"))
original = num
reversed_n = 0
while num > 0:
    reversed_n = reversed_n * 10 + (num % 10)
    num = num // 10
print(f"Reverse of {original} is {reversed_n}")