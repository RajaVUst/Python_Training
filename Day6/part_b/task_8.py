with open("squares.txt", "w") as f:
    for number in range(1, 11):
        square = number ** 2
        f.write(str(square) + "\n")

with open("squares.txt", "r") as f:
    total = 0

    for line in f:
        total += int(line.strip())

print("Total:", total)


# Total: 385
