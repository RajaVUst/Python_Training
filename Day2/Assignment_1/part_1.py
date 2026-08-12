sentence = input("Enter a sentence: ")

clean_sentence = sentence.replace(" ", "").lower()
reversed_sentence = sentence[::-1]
words = sentence.split()

first_word = words[0]
last_word = words[-1]

is_palindrome = (clean_sentence == clean_sentence[::-1])

print(f"Length: {len(sentence)}")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Reversed: {reversed_sentence}")
print(f"Word count: {len(words)}")
print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"Palindrome: {is_palindrome}")

