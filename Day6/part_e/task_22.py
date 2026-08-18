try:
    with open("notes.txt", "r") as f:
        content = f.read()

    print(content)

except FileNotFoundError:
    print("The file was not found.")

finally:
    print("Attempt finished")

# hello World
# Attempt finished