sentence = "  Python IS Fun to Learn!!  "

clean = sentence.strip()
print(f"stripped string {clean}")

print(clean.lower())
print(clean.upper())

print(clean[0])  # first character
print(clean[-1])  # last character
print(clean[:5])  # first five characters

words = sentence.split()
print(words)
print(len(words))

print(clean.replace('Fun','Powerful'))

print("-".join(words))

print(f"Words: {len(words)} | Reversed: {clean[::-1]}")