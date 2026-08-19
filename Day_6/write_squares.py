with open("squares.txt", "w") as f:
    for number in range(1, 11):
        f.write(str(number ** 2) + "\n")

total = 0

with open("squares.txt", "r") as f:
    for line in f:
        total += int(line.strip())

print(total)

# output:
# 385