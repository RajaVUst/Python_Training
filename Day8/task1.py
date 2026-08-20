# Task 1.1 - Inventory Tracker
items = ["pen","notebook","pen","erasor","notebook","pen","stapler"]
first_batch = tuple(items[:3])
uniques = set(items)
dict_items = {}

for item in items:
    dict_items[item] = dict_items.get(item,0)+1
                                            # Output ->
print("Inventory List", items)              # Inventory List ['pen', 'notebook', 'pen', 'erasor', 'notebook', 'pen', 'stapler']
print("First batch Tuple",first_batch)      # First batch Tuple ('pen', 'notebook', 'pen')
print("Unique Items Set", uniques)          # Unique Items Set {'pen', 'stapler', 'erasor', 'notebook'} 
print("Item count Dictionary", dict_items)  # Item count Dictionary {'pen': 3, 'notebook': 2, 'erasor': 1, 'stapler': 1} 

# Task 1.2 - Comprehensions Rewrite
squares = [n*n for n in range(1,21) if n%2 == 0]
print(squares)      # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
word_lengths = {word:len(word) for word in ["python","java","c","kotlin"]}
print(word_lengths)  # {'python': 6, 'java': 4, 'c': 1, 'kotlin': 6}  
unique_vowels = {ch for ch in "the quick brown fox jumps over the lazy dog" if ch in "aeiou"}
print(unique_vowels)  # {'u','e','a','i','o}
# Comprehensions is like short form of a given code especially in one line is faster to write and is more readable

# Task 1.3 - Nested Comprehension Challenge
sentences = ["the sky is blue","python is fun","list comprehensions are handy"]
flat = [word for words in sentences for word in words.split() if len(word)>2]
print(flat)     # ['the', 'sky', 'blue', 'python', 'fun', 'list', 'comprehensions', 'are', 'handy']
unique_words = {word for words in sentences for word in words.split()}
print(unique_words)   # {'python', 'the', 'fun', 'list', 'sky', 'are', 'handy', 'comprehensions', 'is', 'blue'}

# Nested Comprehension becomes less readable when it contains multiple loops and conditions that are difficult to differentiate