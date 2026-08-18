# Exercise 18: Catch a Missing File

print("Exercise 18")

try:
    with open("ghost.txt", "r") as f:
        content = f.read()

except FileNotFoundError:
    print("Sorry, the file does not exist.")

print()


# Exercise 19: Catch a Bad Conversion

print("Exercise 19")

test_value = "abc"

try:
    number = int(test_value)
    print("Converted value:", number)

except ValueError:
    print("Invalid number. Please enter a valid integer.")

print()


# Exercise 20: Multiple Except Blocks

print("Exercise 20")

num1 = "10"
num2 = "0"

try:
    a = int(num1)
    b = int(num2)

    result = a / b
    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter numeric values only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

print()


# Exercise 21: Use Else

print("Exercise 21")

try:
    with open("notes.txt", "r") as f:
        content = f.read()

except FileNotFoundError:
    print("File not found.")

else:
    print("File loaded successfully.")
    print("File length:", len(content))

print()


# Exercise 22: Use Finally for Cleanup Logging

print("Exercise 22 - Existing File")

try:
    with open("notes.txt", "r") as f:
        content = f.read()
        print("Read successful.")

except FileNotFoundError:
    print("File not found.")

finally:
    print("Attempt finished")

#outptu
'''Exercise 18
Sorry, the file does not exist.

Exercise 19
Invalid number. Please enter a valid integer.

Exercise 20
Cannot divide by zero.

Exercise 21
File loaded successfully.
File length: 282

Exercise 22 - Existing File
Read successful.
Attempt finished'''