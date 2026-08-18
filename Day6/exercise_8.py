with open("squares.txt", "w") as f:
    for i in range(1, 11):
        f.write(str(i * i) + "\n")
total = 0
with open("squares.txt", "r") as f:
    for line in f:
        total += int(line)
print(total)

# output
# 385