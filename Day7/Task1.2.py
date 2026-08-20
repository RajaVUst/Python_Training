squares = [
    number * number
    for number in range(1, 21)
    if number % 2 == 0
]

words = ["python", "java", "c", "kotlin"]

word_lengths = {
    word: len(word)
    for word in words
}

sentence = "the quick brown fox jumps over the lazy dog"

unique_vowels = {
    character
    for character in sentence
    if character in "aeiou"
}

print("Even squares:", squares)
print("Word lengths:", word_lengths)
print("Unique vowels:", unique_vowels)

# Comprehensions were faster to write and easy to read because the logic was simple.


#output
'''
Even squares: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
Word lengths: {'python': 6, 'java': 4, 'c': 1, 'kotlin': 6}
Unique vowels: {'e', 'a', 'i', 'o', 'u'}
'''