with open("squares.txt", "w") as f:
    for number in range(1, 11):
        f.write(f"{number ** 2}\n")

total = 0

with open("squares.txt", "r") as f:
    for line in f:
        total += int(line.strip())

print("Total of squares:", total)

#output
'''
Total of squares: 385
'''