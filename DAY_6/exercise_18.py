try:
    with open("ghost.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: The file 'ghost.txt' was not found.")
