# input n
n = int(input("Enter a number: "))

# outer loop to traverse through each row
for i in range(n):
# inner loop through traverse through columns
    for j in range(i+1):
        print("*", end="")
    print()