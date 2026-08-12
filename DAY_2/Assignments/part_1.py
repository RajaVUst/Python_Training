sentence = input("Enter a sentence: ")

cleaned = sentence.replace(" ", "").lower()

print(f"Total length: {len(sentence)}")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Reversed: {sentence[::-1]}")
print(f"Word count: {len(sentence.split())}")
print(f"First word: {sentence.split()[0]}")
print(f"Last word: {sentence.split()[-1]}")
print(f"Palindrome: {cleaned == cleaned[::-1]}")