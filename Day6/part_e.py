from constants import NOTES_FILE
# Exercise 18: Catch a missing file
try:
    with open("ghost.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found. Please check the file name.")
# Output:
# File not found. Please check the file name.


# Exercise 19: Catch a bad conversion
value = "abc"
try:
    number = int(value)
    print(number)
except ValueError:
    print("Invalid number. Please enter a valid integer.")
# Output:
# Invalid number. Please enter a valid integer.


# Exercise 20: Multiple except blocks
num1 = "10"
num2 = "0"
try:
    result = int(num1) / int(num2)
    print("Result:", result)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
# Output:
# Cannot divide by zero.


# Exercise 21: Use else
try:
    with open(NOTES_FILE, "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File loaded successfully")
    print("Length:", len(content))
# Output:
# File loaded successfully
# Length: 105


# Exercise 22: Use finally for cleanup logging
# Test with an existing file
try:
    with open(NOTES_FILE, "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Attempt finished")
# Output:
# Attempt finished


# Test with a missing file
try:
    with open("missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Attempt finished")

# Output:
# File not found.
# Attempt finished