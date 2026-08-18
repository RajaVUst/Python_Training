# Write squares to the file
with open("day6/squares.txt", "w") as f:
    for n in range(1, 11):
        f.write(f"{n ** 2}\n")

# Read the numbers back and calculate the total
total = 0

with open("day6/squares.txt", "r") as f:
    for line in f:
        total += int(line.strip())

print(total)

"""
OUTPUT:
385
"""