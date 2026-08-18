try:
    with open("ghost.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Sorry, the file was not found.")
 
# Output:
# Sorry, the file was not found.
 