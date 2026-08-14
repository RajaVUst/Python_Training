n = 6
factorial = 1
if n == 0:
    print("0! is 1")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
    print(f"{n}! is {factorial}")