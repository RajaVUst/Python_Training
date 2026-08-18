try:
    with open(r"Day_6\Ref doc\notes.txt", "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("File not found.")

finally:
    print("Attempt finished")

# Output:
# File not found.
# Attempt finished

# Output:
# Hello World
# Hello Python
# Attempt finished