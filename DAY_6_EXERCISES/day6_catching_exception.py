try:
    with open("ghost.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Sorry, the file was not found.")

"""
Output->
Sorry, the file was not found.
"""