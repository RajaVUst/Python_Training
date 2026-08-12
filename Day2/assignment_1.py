
sentence = input("Enter a sentence: ")

# 1. Total length
print(f"Total length: {len(sentence)}")

# 2. Uppercase and lowercase
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")

# 3. Reversed sentence
print(f"Reversed: {sentence[::-1]}")

# 4. Word count
words = sentence.split()
print(f"Word count: {len(words)}")

# 5. First word and last word
print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")

# 6. Palindrome check
cleaned = sentence.replace(" ", "").lower()
is_palindrome = (cleaned == cleaned[::-1])
print(f"Palindrome: {is_palindrome}")