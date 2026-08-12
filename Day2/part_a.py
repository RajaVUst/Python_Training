sentence = "    Python IS Fun to Learn!!   "
print(sentence)

# removing unwanted space
clean = sentence.strip()
print(clean)

#lowercase
print(clean.lower())

#uppercase
print(clean.upper())

#indexing and slicing
print(clean[0])
print(clean[8])
print(clean[:5])
print(clean[7:11])
print(clean[8:])
print(clean [-4:])


#split
word = clean.split()
print(word)
print(len(word))

#replace

print(clean.replace("Fun", "Powerful"))

#join
print("-".join(word))

#reverse
print(clean[::-1])

#fstring
print(f"Words : {len(word)} | Reversed: {clean[::-1]}")