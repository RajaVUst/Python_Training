sentence = "   Python IS Fun to Learn!!   "
clean = sentence.strip()
print(clean)

print(clean.lower())
print(clean.upper())

print(clean[0])
print(clean[-1])
print(clean[:5])

words=clean.split()
print(words)
print(len(words))

print(clean.replace("Fun","Powerful"))

print("-".join(words))

print(f"Words: {len(words)} | Reversed: {clean[::-1]}")