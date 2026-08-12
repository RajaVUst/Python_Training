sentence = input("Enter a sentence: ")

length = len(sentence)
upper = sentence.upper()
lower = sentence.lower()
reversed_sentence = sentence[::-1]
words = sentence.split()
word_count = len(words)
first_word = words[0]
last_word = words[-1]

cleaned = sentence.replace(" ", "").lower()
is_palindrome = (cleaned == cleaned[::-1])

print(f"Length: {length}")
print(f"Uppercase: {upper}")
print(f"Lowercase: {lower}")
print(f"Reversed: {reversed_sentence}")
print(f"Word count: {word_count}")
print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"Palindrome: {is_palindrome}")