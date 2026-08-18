
with open("squares.txt", "w") as f:
    for n in range(1, 11):
        f.write(f"{n ** 2}\n")

with open("squares.txt") as f:
    total = sum(int(line) for line in f)
print(total)

#output
# 385