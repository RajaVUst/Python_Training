# Part A - Guided String Walkthrough

# Step 1: Create a messy sentence
sentence = "   Python IS Fun to Learn!!   "

# Step 2: Strip whitespace
clean = sentence.strip()
print(clean)

# Step 3: Lowercase and uppercase versions
print(clean.lower())
print(clean.upper())

# Step 4: Indexing and slicing
print(clean[0])
print(clean[-1])
print(clean[:5])

# Step 5: Split into words and count
words = clean.split()
print(words)
print(len(words))

# Step 6: Replace "Fun" with "Powerful"
print(clean.replace("Fun", "Powerful"))

# Step 7: Join words with a dash
print("-".join(words))

# Step 8: f-string summary with word count and reversed sentence
print(f"Words: {len(words)} | Reversed: {clean[::-1]}")
