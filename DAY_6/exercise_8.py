with open("squares.txt", "w") as f:
    for n in range(1, 11):
        f.write(str(n ** 2) + "\n")

total = 0
with open("squares.txt", "r") as f:
    for line in f:
        total += int(line.strip())

print("Total of all squares:", total)
