# Exercise 1: Read the whole file
f = open("notes.txt", "r")
content= f.read()       # Output :
print(len(content))     # 88

# Exercise 2: Read just the first line
line = f.readline().strip()
print(line)         # This is Python Refresher Trainee

# Exercise 3: Read all lines into a list
lines = f.readlines()
print(len(lines))   # 4
print(lines)        # ['This is Python Refresher Trainee\n', 'Practicing the Exercises \n', 'Self Studying\n', 'Happy Onam!!!!!']

# Exercise 4: Line-by-line iteration
for line in f:
    clean_line = line.strip()
    if not clean_line:
        continue
    print(clean_line.upper())
""" 
Output ->
THIS IS PYTHON REFRESHER TRAINEE
PRACTICING THE EXERCISES
SELF STUDYING
HAPPY ONAM!!!!!
"""

# Exercise 5: Count words in a file
count = 0
for word in f:
    count += len(word.split())
print("Total number of words",count)    # Total number of words 12
f.close()