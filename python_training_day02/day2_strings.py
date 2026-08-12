#create a messy sentence
sentence = " Python IS Fun to Learn!! "

#remove spaces
clean = sentence.strip()
print(clean)

#printing lowercase and uppercase
print(clean.lower())
print(clean.upper())

#print first character, last character, and first five characters
print(clean[0])
print(clean[-1])
print(clean[:5])

#split into words and count them
words = clean.split()
print(words)
print(len(words))

#replace "Fun" with "Powerful"
print(clean.replace("Fun", "Powerful"))

#joining the words using dash
print("-".join(words))

#print word count and reversed sentence
print(f"Words: {len(words)} | Reversed: {clean[::-1]}")