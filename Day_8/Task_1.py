# Task 1.1 - Inventory Tracker

items = [
    "pen",
    "notebook",
    "pen",
    "eraser",
    "notebook",
    "pen",
    "stapler"
]

# List preserves arrival order and duplicates
arrival_order = items.copy()

# Tuple creates an immutable record of the first batch
first_batch = tuple(items[:3])

# Set stores only unique item names
unique_items = set(items)

# Dictionary counts occurrences of each item
item_counts = {}

for item in items:
    item_counts[item] = item_counts.get(item, 0) + 1

print("Task 1.1")
print("Arrival Order List:", arrival_order)
print("First Batch Tuple:", first_batch)
print("Unique Items Set:", unique_items)
print("Item Counts Dict:", item_counts)

# List: preserves order and duplicates
# Tuple: immutable record that should not change
# Set: automatically removes duplicates
# Dict: maps item names to counts efficiently

print()


# Task 1.2 - Comprehensions Rewrite

# Original loop rewritten as a list comprehension
squares = [n * n for n in range(1, 21) if n % 2 == 0]

# Original loop rewritten as a dict comprehension
word_lengths = {
    word: len(word)
    for word in ["python", "java", "c", "kotlin"]
}

# Original loop rewritten as a set comprehension
unique_vowels = {
    ch
    for ch in "the quick brown fox jumps over the lazy dog"
    if ch in "aeiou"
}

print("Task 1.2")
print("Squares:", squares)
print("Word Lengths:", word_lengths)
print("Unique Vowels:", unique_vowels)

# Comprehensions are usually faster to write for simple transformations.
# Loops can be easier to read when the logic becomes more complex.

print()


# Task 1.3 - Nested Comprehension Challenge

sentences = [
    "the sky is blue",
    "python is fun",
    "list comprehensions are handy"
]

# Flat list of words longer than 2 characters
long_words = [
    word
    for sentence in sentences
    for word in sentence.split()
    if len(word) > 2
]

# Set of unique words (case-insensitive)
unique_words = {
    word.lower()
    for sentence in sentences
    for word in sentence.split()
}

print("Task 1.3")
print("Words Longer Than 2 Characters:")
print(long_words)

print("\nUnique Words:")
print(unique_words)

#Output
'''Task 1.1
Arrival Order List: ['pen', 'notebook', 'pen', 'eraser', 'notebook', 'pen', 'stapler']
First Batch Tuple: ('pen', 'notebook', 'pen')
Unique Items Set: {'stapler', 'notebook', 'eraser', 'pen'}
Item Counts Dict: {'pen': 3, 'notebook': 2, 'eraser': 1, 'stapler': 1}

Task 1.2
Squares: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
Word Lengths: {'python': 6, 'java': 4, 'c': 1, 'kotlin': 6}
Unique Vowels: {'o', 'e', 'a', 'i', 'u'}

Task 1.3
Words Longer Than 2 Characters:
['the', 'sky', 'blue', 'python', 'fun', 'list', 'comprehensions', 'are', 'handy']

Unique Words:
{'blue', 'python', 'sky', 'is', 'are', 'list', 'the', 'comprehensions', 'handy', 'fun'}'''