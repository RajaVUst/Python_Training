value = input("Enter a number: ")

try:
    number = int(value)
    print(number)

except ValueError:
    print("Please enter a valid integer.")

# output:
# Enter a number: 1.2
# Please enter a valid integer.
# PS C:\Users\308239\Python> 12
# 12