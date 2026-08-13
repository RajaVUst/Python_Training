# Exercise 14 - Right-Angled Triangle Pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()