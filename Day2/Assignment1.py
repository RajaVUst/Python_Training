#String Manipulation Script
sentence = input("Enter a sentence: ")

print(f"Length: {len(sentence)}")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Reversed: {sentence[::-1]}")

words = sentence.split()
print(f"Word count: {len(words)}")
print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")

cleaned = sentence.replace(" ", "").lower()
is_palindrome = (cleaned == cleaned[::-1])
print(f"Is palindrome: {is_palindrome}")