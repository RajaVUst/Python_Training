try:
    with open("ghost.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Sorry, the file could not be found.")
    
"""
OUTPUT:
  File "c:\training\python_training\Python_Training\day6\day6_exercise18.py", line 7
    OUTPUT:
           ^
SyntaxError: invalid syntax
"""