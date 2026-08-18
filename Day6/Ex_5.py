word_count = 0
 
with open(r"C:\training\Python_Training\Day_6\Ref doc\notes.txt", "r") as f:
    for line in f:
        word_count += len(line.split())
 
print("Total words:", word_count)
 
# Output:
# Total words: 4
 