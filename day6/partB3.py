with open("squares.txt", "w") as f:
    for number in range(1, 11):
        square = number * number
        f.write(str(square) + "\n")

total = 0

with open("squares.txt", "r") as f:
    for line in f:
        total = total + int(line.strip())

print("Total:", total)

# OUTPUT

# Total: 385
