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


# Task 1.2 - Comprehensions Rewrite
squares = [n * n for n in range(1, 21) if n % 2 == 0]
word_lengths = {
    word: len(word)
    for word in ["python", "java", "c", "kotlin"]
}
unique_vowels = {
    ch
    for ch in "the quick brown fox jumps over the lazy dog"
    if ch in "aeiou"
}
print("Squares of even numbers:", squares)
print("Word lengths:", word_lengths)
print("Unique vowels:", unique_vowels)

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
unique_words = {
    word.lower()
    for sentence in sentences
    for word in sentence.split()
}

print("Words longer than 2 characters:", long_words)
print("Unique words:", unique_words)

# Output.
# result = [x * y
#           for x in range(10)
#           for y in range(10)
#           if x % 2 == 0
#           if y % 3 == 0
#           if x + y > 5]
