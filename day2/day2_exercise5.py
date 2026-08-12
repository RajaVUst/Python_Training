# store string in a variable
title = "  My First   Python Project!!  "

# store the cleaned version of the string in a new variable
clean = title.strip().lower().replace("!!","").replace(" ","_")

# print the cleaned string
print(clean)