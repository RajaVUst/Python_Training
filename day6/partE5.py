files = ["read.txt", "ghost.txt"]

for filename in files:
    print(f"Reading {filename}:")
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("The file could not be found.")
    finally:
        print("Attempt finished")

# OUTPUT

# Reading read.txt:
# hello  i am bonny residing in this file
# Attempt finished
# Reading ghost.txt:
# The file could not be found.
# Attempt finished
