with open(r"C:\training\Python_Training\Day_6\Ref doc\squares.txt", "w") as f:
    for i in range(1, 11):
        f.write(str(i ** 2) + "\n")

total = 0

with open(r"C:\training\Python_Training\Day_6\Ref doc\squares.txt", "r") as f:
    for line in f:
        total += int(line.strip())

print("Total:", total)

# Output:
# Total: 385