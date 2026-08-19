try:
    with open("notes.txt", "r") as f:
        content = f.read()

    print(content)

except FileNotFoundError:
    print("The file was not found.")

finally:
    print("Attempt finished")

# output:
# Hey there
# I am Chandrashekhar 
# And this is the 6th day of training

# Attempt finished