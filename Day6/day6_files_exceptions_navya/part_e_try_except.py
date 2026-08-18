# Exercise 18 - Catch a missing file
try:
    with open("ghost.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found, please check the filename")
# Output: File not found, please check the filename


# Exercise 19 - Catch a bad conversion
value = "abc"

try:
    number = int(value)
except ValueError:
    print("That's not a valid number")
# Output: That's not a valid number


# Exercise 20 - Multiple except blocks
num1 = "20"
num2 = "0"

try:
    a = int(num1)
    b = int(num2)
    result = a / b
    print(result)
except ValueError:
    print("Please enter valid numbers")
except ZeroDivisionError:
    print("Cannot divide by zero")
# Output: Cannot divide by zero


# Exercise 21 - Use else
try:
    with open("notes.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
else:
    print("File loaded successfully")
    print(len(content))
# Output:
# File loaded successfully
# 187


# Exercise 22 - Use finally for cleanup logging
try:
    with open("notes.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Attempt finished")
# Output:
# Attempt finished

try:
    with open("ghost.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Attempt finished")
# Output:
# File not found
# Attempt finished