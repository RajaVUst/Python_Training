value = input("Enter a number: ")

try:
    number = int(value)
    print("Number:", number)

except ValueError:
    print("Invalid input. Please enter a valid number.")

# Enter a number: 24
# Number: 24


# Enter a number: abc
# Invalid input. Please enter a valid number.