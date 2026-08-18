try:
    with open("../part_A/notes.txt", "r") as f:
        content = f.read()

except FileNotFoundError:
    print("File not found.")

finally:
    print("Attempt finished")



#output:
'''Attempt finished'''