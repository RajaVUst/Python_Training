# Exercise 6: Write a fresh file
with open("diary.txt","w") as f:
    f.write("Master class not there\nOnam Celebrations \nEnjoyyyyy\n")
    # New File created successfully

# Exercise 7: Append without overwriting
with open("diary.txt","a") as f:
    f.write("Colourful Festival")
with open("diary.txt","r") as f:
    print(f.readlines())      # ['Master class not there\n', 'Onam Celebrations \n', 'Enjoyyyyy\n', 'Colourful Festival']

# Exercise 8: Write numbers to a file
with open("squares.txt","w") as f:
    for i in range(1,11):
        f.write(f"{i**2}\n")
total = 0
with open("squares.txt","r") as f:
    for num in f:
        total += int(num.strip())
print(total)    # 385

# Exercise 9: Copy and transform a file
with open("notes.txt","r") as s, open("notes_upper.txt","w") as d:
    for i in s:
        d.write(i.upper())
    # File contents copied and transformed successfully