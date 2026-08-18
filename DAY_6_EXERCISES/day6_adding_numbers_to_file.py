with open("DAY_6_EXERCISES/squares.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{i**2}\n")

total = 0

with open("DAY_6_EXERCISES/squares.txt", "r") as f:
    for line in f:
        total += int(line.strip())

print("Total:", total)

"""
Output->
Total: 385
"""