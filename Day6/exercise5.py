total_words=0

with open("notes.txt","r") as f:
    for line in f:
        total_words+=len(line.split())

print(total_words)

#output
'''
110
'''