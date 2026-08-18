# Day 6 - Exercise 18
try:
    with open("ghost.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("The requested file was not found.")


#output
'''
The requested file was not found.
'''
