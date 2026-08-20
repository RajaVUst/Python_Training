# List comprehension: squares of even numbers from 1-20
# Comprehension felt faster to write and easier to read for simple filters like this
squares = [n * n for n in range(1, 21) if n % 2 == 0]

# Dict comprehension: word -> its length
word_lengths = {word: len(word) for word in ["python", "java", "c", "kotlin"]}

# Set comprehension: unique vowels from a sentence
unique_vowels = {ch for ch in "the quick brown fox jumps over the lazy dog" if ch in "aeiou"}

print("Even squares:", squares)
print("Word lengths:", word_lengths)
print("Unique vowels:", unique_vowels)
