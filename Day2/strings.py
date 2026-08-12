# Part A - Guided String

# Step 1: Create a messy sentence
sentence = "   Python IS Fun to Learn!!   "

# Step 2: Remove leading and trailing spaces
clean = sentence.strip()
print("Cleaned Sentence:", clean)

# Step 3: Print lowercase and uppercase versions
print("Lowercase:", clean.lower())
print("Uppercase:", clean.upper())

# Step 4: Print first character, last character, and first five characters
print("First Character:", clean[0])
print("Last Character:", clean[-1])
print("First Five Characters:", clean[:5])

# Step 5: Split into words and count them
words = clean.split()
print("Words List:", words)
print("Word Count:", len(words))

# Step 6: Replace 'Fun' with 'Powerful'
print("Updated Sentence:", clean.replace("Fun", "Powerful"))

# Step 7: Join words with dashes
print("Joined Sentence:", "-".join(words))

# Step 8: Print summary with word count and reversed sentence
print(f"Words: {len(words)} | Reversed: {clean[::-1]}")