with open(r"Day_6\Ref doc\diary.txt", "a") as f:
    f.write("I learned how to write and append files in Python.\n")
 
with open(r"Day_6\Ref doc\diary.txt", "r") as f:
    content = f.read()
 
print(content)
 
# Output:
# I learned how to read files in Python.    
# I learned how to count words in a text file.
# I learned how to iterate through file lines.
# I learned how to write and append files in Python.
 