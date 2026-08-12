# Part 1 - String Manipulation

sentence = input("Enter a sentence: ")

# Total character count
character_count = len(sentence)

# Uppercase and lowercase
uppercase_sentence = sentence.upper()
lowercase_sentence = sentence.lower()

# Reverse sentence
reversed_sentence = sentence[::-1]

# Word count
words = sentence.split()
word_count = len(words)

# First and last words
first_word = words[0]
last_word = words[-1]

# Palindrome check
cleaned_sentence = sentence.replace(" ", "").lower()
is_palindrome = cleaned_sentence == cleaned_sentence[::-1]

print()
print("=== Sentence Analysis ===")

print(f"Character count: {character_count}")
print(f"Uppercase: {uppercase_sentence}")
print(f"Lowercase: {lowercase_sentence}")
print(f"Reversed: {reversed_sentence}")
print(f"Word count: {word_count}")
print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"Palindrome: {is_palindrome}")