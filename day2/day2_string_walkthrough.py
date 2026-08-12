sentence = "   Python IS Fun to Learn!!   "
stripped_sentence = sentence.strip()
print(stripped_sentence)

print(stripped_sentence.upper())
print(stripped_sentence.lower())

print(stripped_sentence[0])
print(stripped_sentence[-1])
print(stripped_sentence[:5])

words = stripped_sentence.split()
print(words)
print(len(words))

print(stripped_sentence.replace("Fun", "Powerful"))

print("-".join(words))

print(f"Words: {len(words)} | Reversed: {stripped_sentence[::-1]}")