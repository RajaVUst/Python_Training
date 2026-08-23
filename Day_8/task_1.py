
# Task 1.1 — Inventory Tracker

items = ["pen", "notebook", "pen", "eraser", "notebook", "pen", "stapler"]

arrival_list = items

first_batch = tuple(items[:3])
print(first_batch)

unique_items = set(items)
item_count = {}
for item in items:
    item_count[item] = item_count.get(item,0)+1

print(item_count)    

print('-------------------------------------------------------------------------------------')
# output
#('pen', 'notebook', 'pen')
#{'pen': 3, 'notebook': 2, 'eraser': 1, 'stapler': 1}

# Task 1.2

squares = [n * n for n in range(1, 21) if n % 2 == 0]
print(squares)
word_lengths = {word: len(word) for word in ["python", "java", "c", "kotlin"]}
print(word_lengths)
unique_vowels = {ch for ch in "the quick brown fox jumps over the lazy dog" if ch in "aeiou"}
print(unique_vowels)


squares = []
for n in range(1, 21):
    if n % 2 == 0:
        squares.append(n * n)

word_lengths = {}
for word in ["python", "java", "c", "kotlin"]:
    word_lengths[word] = len(word)

unique_vowels = set()
for ch in "the quick brown fox jumps over the lazy dog":
    if ch in "aeiou":
        unique_vowels.add(ch)

squares = [n * n for n in range(1, 21) if n % 2 == 0]

word_lengths = {word: len(word) for word in ["python", "java", "c", "kotlin"]}

unique_vowels = {ch for ch in "the quick brown fox jumps over the lazy dog" if ch in "aeiou"}


# the comperhension method is easy and faster compared to loop version 

# Task 1.3 — Nested Comprehension Challenge 

sentences = ["the sky is blue", "python is fun", "list comprehensions are handy"] 
long_words = [word for sentence in sentences for word in sentence.split() if len(word) > 2]
print(long_words)
unique_words = {word.lower() for sentence in sentences for word in sentence.split()}
print(unique_words)
 # Nwsted comprehension becomes less readable when it contains multiple loops and more than one condition

 # output

#  ['the', 'sky', 'blue', 'python', 'fun', 'list', 'comprehensions', 'are', 'handy']
# {'blue', 'python', 'the', 'sky', 'fun', 'list', 'comprehensions', 'handy', 'is', 'are'}


# Task 4.3 — Capstone: Robust CSV → JSON Converter

import csv

customer_totals = {}
statuses = set()

with open("order.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        try:
            amount = float(row["amount"])
        except (ValueError, TypeError):
            print(
                f"Invalid amount for customer {row['customer']} "
                f"(order {row['order_id']}). Skipping now."
            )
            continue

        customer = row["customer"]
        customer_totals[customer] = customer_totals.get(customer, 0) + amount
        statuses.add(row["status"])

print(customer_totals)
print(statuses)