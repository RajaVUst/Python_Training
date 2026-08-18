# Write numbers to a file

with open("Day6/squares.txt", "w") as f:
    for number in range(1, 11):
        square = number * number
        f.write(str(square) + "\n")


total = 0
with open("Day6/squares.txt", "r") as f:

    for line in f:
        number = int(line.strip())
        total = total + number
print("Total:", total)


# Output:
# Total: 385