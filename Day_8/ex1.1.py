items = ["pen", "notebook", "pen", "eraser", "notebook", "pen", "stapler"]

# List: preserves the original arrival order and allows duplicates.
arrival_order = list(items)

# Tuple: stores the first 3 items as an immutable "first batch" record.
first_batch = tuple(items[:3])

# Set: keeps only unique item names, removing duplicates automatically.
unique_items = set(items)

# Dictionary: maps each item to the number of times it was received.
item_counts = {}
for item in items:
    item_counts[item] = item_counts.get(item, 0) + 1

print("List (arrival order):", arrival_order)
print("Tuple (first batch):", first_batch)
print("Set (unique items):", unique_items)
print("Dict (item counts):", item_counts)

# Output:
# List (arrival order): ['pen', 'notebook', 'pen', 'eraser', 'notebook', 'pen', 'stapler']
# Tuple (first batch): ('pen', 'notebook', 'pen')
# Set (unique items): {'eraser', 'stapler', 'notebook', 'pen'}
# Dict (item counts): {'pen': 3, 'notebook': 2, 'eraser': 1, 'stapler': 1}  