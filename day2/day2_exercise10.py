# store the string in a variable
text = "the quick brown fox"

# store the starting index of word brown in a variable
starting_index = text.find("brown")

# replace the string brown with red and store it in a new variable
new_text = text.replace("brown", "red")

print(f"Original text: {text}")
print(f"Starting index of 'brown': {starting_index}")
print(f"New text after replacement: {new_text}")