# Task 1.1 - Inventory Tracker
items = ["pen", "notebook", "pen", "eraser", "notebook", "pen", "stapler"]
inventory_list = items.copy()
first_batch = tuple(items[:3])
unique_items = set(items)
item_counts = {}
for item in items:
    item_counts[item] = item_counts.get(item, 0) + 1

print("List:", inventory_list)
print("Tuple:", first_batch)
print("Set:", unique_items)
print("Dictionary:", item_counts)

# Output:
# List: ['pen', 'notebook', 'pen', 'eraser', 'notebook', 'pen', 'stapler']
# Tuple: ('pen', 'notebook', 'pen')
# Set: {'pen', 'notebook', 'eraser', 'stapler'}
# Dictionary: {'pen': 3, 'notebook': 2, 'eraser': 1, 'stapler': 1}


# Task 1.2 - Comprehensions Rewrite
squares = [n * n for n in range(1, 21) if n % 2 == 0]
print("Squares:", squares)
word_lengths = {
    word: len(word)
    for word in ["python", "java", "c", "kotlin"]
}
print("Word Lengths:", word_lengths)
unique_vowels = {
    ch
    for ch in "the quick brown fox jumps over the lazy dog"
    if ch in "aeiou"
}
print("Unique Vowels:", unique_vowels)
# Output:
# Squares: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
# Word Lengths: {'python': 6, 'java': 4, 'c': 1, 'kotlin': 6}
# Unique Vowels: {'a', 'e', 'i', 'o', 'u'}


# Reflection
# Comprehensions felt faster to write because they need fewer lines.
# For simple operations, comprehensions were also easy to read back.
# Loops may be easier to understand when the logic becomes complex.


# Task 1.3 - Nested Comprehension Challenge
sentences = [
    "the sky is blue",
    "python is fun",
    "list comprehensions are handy"
]
long_words = [
    word
    for sentence in sentences
    for word in sentence.split()
    if len(word) > 2
]
print("Long Words:", long_words)
# Output:
# Long Words:
# ['the', 'sky', 'blue', 'python', 'fun',
#  'list', 'comprehensions', 'are', 'handy']
unique_words = {
    word.lower()
    for sentence in sentences
    for word in sentence.split()
}

print("Unique Words:", unique_words)
# Output:
# Unique Words:
# {'the', 'sky', 'is', 'blue', 'python',
#  'fun', 'list', 'comprehensions', 'are', 'handy'}


# Checkpoint Answer
# A nested comprehension becomes less readable when it contains
# multiple loops and several conditions.
#
# Example:
# result = [
#     x * y
#     for x in range(10)
#     for y in range(10)
#     if x % 2 == 0
#     if y % 3 == 0
#     if x + y > 5
# ]
#
# In this case, regular nested loops would be easier to read and maintain.