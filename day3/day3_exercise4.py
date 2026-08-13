# input a number
num = int(input("Enter a number: "))

# check if number is positive, negative or zero
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")