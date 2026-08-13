# Take input from the user
n = int(input("Enter a whole number: "))

# initialize variable to 1
factorial = 1

# iterate through loop and multiply with the existing product
for i in range(1, n + 1):
    factorial *= i

# print the factorial
print("Factorial:", factorial)