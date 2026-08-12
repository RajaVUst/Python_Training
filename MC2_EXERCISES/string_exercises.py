sentence = "   Python IS Fun to Learn!!  "
# Stripped whitespaces
clean = sentence.strip()
print(clean)
# Converted to Lowercase and Uppercase
print(clean.lower())
print(clean.upper())
# Trimmed to get first, last and first five characters
print(clean[0]) 
print(clean[-1]) 
print(clean[:5]) 
# Split words
words = clean.split() 
print(words) 
print(len(words)) 
# Replace word
print(clean.replace("Fun", "Powerful"))
# Rejoin words
print("-".join(words))  
# One line summary
print(f"Words: {len(words)} | Reversed: {clean[::-1]}") 