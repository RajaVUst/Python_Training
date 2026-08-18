value = input("Enter a number: ")
try:
    number = int(value)
    print(number)
except ValueError:
    print("Please enter a valid number")

#     output
#     Enter a number: abc
# Please enter a valid number