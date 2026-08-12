sentence = " Python IS Fun to Learn!! "

# 2. Remove leading and trailing spaces
clean = sentence.strip()
print(clean)

# 3. Lowercase and uppercase versions
print(clean.lower())
print(clean.upper())

# 4. Indexing and slicing
print(clean[0])     # First character
print(clean[-1])    # Last character
print(clean[:5])    # First five characters

# 5. Split sentence into words
words = clean.split()
print(words)
print(len(words))

# 6. Replace "Fun" with "Powerful"
print(clean.replace("Fun", "Powerful"))

# 7. Join words using "-"
print("-".join(words))

# 8. Summary using f-string
print(f"Words: {len(words)} | Reversed: {clean[::-1]}")