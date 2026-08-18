try:
    with open("notes.txt", "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("File not found")

finally:
    print("Attempt finished")

#     output
#     Hello World
# I am learning Python
# Today is Day 6
# Attempt finished