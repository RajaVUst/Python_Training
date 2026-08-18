# Exercise 18: Catch a missing file
try:
    with open("ghost.txt","r") as f:
        reader = f.readlines()
except FileNotFoundError:
    print("Please check your file name")
# Output -> Please check your file name

# Exercise 19: Catch a bad coversion
try:
    text = input("enter id: ")
    int(text)
except ValueError:
    print("enter only numbers")     # enter only numbers

# Exercise 20: Multiple except blocks
try:
    a = int(input("Enter number1: "))
    b = int(input("enter number2: "))
    print(a/b)
except ValueError:
    print("bad numbers")        # bad numbers
except ZeroDivisionError:
    print("dividing by zero")   # dividing by zero

# Exercise 21: Use else
try:
    with open("squares.txt","r") as f:
        reader = f.readlines()
except FileNotFoundError:
    print("sorry not found that file")
else:
    print("File loaded successfully",len(reader))    # File loaded successfully 10

# Exercise 22: Use finally for cleanup logging
try:
    with open("shabanam.txt","r") as f:
        f.read()
except FileNotFoundError:
    print("Not found")      # Not found
finally:
    print("Attempt finished")   # Attempt finished