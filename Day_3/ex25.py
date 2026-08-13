# 25:Pyramid of numbers
n = int(input("Enter number of rows: "))

for row in range(1, n + 1):
    for num in range(1, row + 1):
        print(num, end=" ")
    print()