# Part 1 - String Manipulation Script
sentence = input("Enter a sentence: ")

print("\n----- String Analysis -----")
print(f"Length: {len(sentence)}")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Reversed: {sentence[::-1]}")

words = sentence.split()

print(f"Word Count: {len(words)}")
print(f"First Word: {words[0]}")
print(f"Last Word: {words[-1]}")

clean_sentence = sentence.replace(" ", "").lower()
is_palindrome = clean_sentence == clean_sentence[::-1]

print(f"Palindrome: {is_palindrome}")