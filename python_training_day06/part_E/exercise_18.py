try:
    with open("ghost.txt", "r") as f:
        content = f.read()

except FileNotFoundError:
    print("File not found.")


#output:  File not found.