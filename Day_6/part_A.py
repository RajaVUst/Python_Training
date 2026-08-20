# Exercise 1: Read the whole file 

with open('notes.txt', "r") as f:
    content = f.read()
    print(content)
    print(len(content))

print('-----------------')
# Output
# hello world
# learning python
# 27

# Exercise 2: Read just the first line 

with open('notes.txt', "r") as f:
    first = f.readline().strip()
    print(first)

print('-----------------')

# output 
# hello world    

# Exercise 3: Read all lines into a list 

with open('notes.txt', "r") as f:
    list_of = f.readlines()
    print(len(list_of))
    print(list_of)

print('-----------------')

# Output
# 2
# ['hello world\n', 'learning python']

#Exercise 4: Line-by-line iteration 

with open('notes.txt', "r") as f:
    for line in f:
        clean_line = line.strip()
        if not clean_line:
            continue
        print(clean_line.upper())
print('-----------------')
   
#output 

# HELLO WORLD
# LEARNING PYTHON

# Exercise 5: Count words in a file 

with open('notes.txt', "r") as f:
    text = f.read()
    word = text.split()
    print(len(word))

print('-----------------')
 # output 
 # 4 


 