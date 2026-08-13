sentence = input("Enter a sentence: ")

words = sentence.split()
cleaned = sentence.replace(" ", "").lower()

print(f"Total length: {len(sentence)}")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Reversed: {sentence[::-1]}")
print(f"Word count: {len(words)}")
print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")
print(f"Palindrome: {cleaned == cleaned[::-1]}")