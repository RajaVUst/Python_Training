# Exercise 18 - Catch a missing file
try:
    with open("ghost.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("That file doesn't exist -- skipping it.")
# Output: That file doesn't exist -- skipping it.

# Exercise 19 - Catch a bad conversion
test_value = "abc"
try:
    number = int(test_value)
except ValueError:
    print("That wasn't a valid number.")
# Output: That wasn't a valid number.

# Exercise 20 - Multiple except blocks
def divide(a_str, b_str):
    try:
        a = int(a_str)
        b = int(b_str)
        result = a / b
    except ValueError:
        print("One of the inputs is not a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"{a} / {b} = {result}")

divide("10", "2")
divide("10", "0")
divide("ten", "2")
# Output:
# 10 / 2 = 5.0
# Cannot divide by zero.
# One of the inputs is not a valid number.

# Exercise 21 - Use else
try:
    with open("notes.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File missing -- using empty data instead.")
    content = ""
else:
    print("File loaded successfully")
    print(len(content))
# Output:
# File loaded successfully
# 205

# Exercise 22 - Use finally for cleanup logging
def read_file_with_logging(path):
    try:
        with open(path, "r") as f:
            content = f.read()
        print(f"Read {len(content)} characters from {path}")
    except FileNotFoundError:
        print(f"{path} does not exist.")
    finally:
        print("Attempt finished")

read_file_with_logging("notes.txt")
read_file_with_logging("missing_file.txt")
# Output:
# Read 205 characters from notes.txt
# Attempt finished
# missing_file.txt does not exist.
# Attempt finished