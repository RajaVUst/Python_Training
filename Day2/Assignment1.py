#String Manipulation Script
sentence = input("Enter a sentence: ")

print("Length:", len(sentence))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Reversed:", sentence[::-1])

words = sentence.split()
print("Word count:", len(words))
print("First word:", words[0])
print("Last word:", words[-1])

cleaned = sentence.replace(" ", "").lower()
palindrome = cleaned == cleaned[::-1]
print("Palindrome:", palindrome)