# input the number of rows in the pyramid
n = int(input("Enter the number of rows: "))

# loop through the rows
for row in range(1, n + 1):
    for num in range(1, row + 1):
        # space between each character in a row
        print(num, end=" ")
    # line break
    print()