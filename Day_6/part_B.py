# Exercise 6: Write a fresh file 

with open('diary.txt', "w") as f:
    f.write('Learned how to create funtion.\n')
    f.write('Learned about list, tuple, dict.\n')
    f.write('Learned about statements.\n')

# Exercise 7: Append without overwriting 

with open('diary.txt', "a") as f:
    f.write('Learned read and write.\n')
with open('diary.txt', "r") as f:
    text = f.read()
    print(text)    
print('-----------------')
# output 
# Learned how to create funtion.
# Learned about list, tuple, dict.
# Learned about statements.
# Learned read and write.


# Exercise 8: Write numbers to a ffile 

with open('squares.txt', "w") as f:
    for i in range(1,11):
        f.write(str(i ** 2)+ "\n")
with open('squares.txt', "r") as f:
   total = 0
   for line in f :
       total += int(line.strip())
print(total)  
print('-----------------')
# Output
# 385 

    # Exercise 9: Copy and transform a file 

with open('notes.txt', "r") as source, open('notes_upper.txt', "w") as dest:
    for item in source:
        dest.write(item.upper())
with open('notes_upper.txt', "r") as f:
    display = f.readlines()
    print(display)       