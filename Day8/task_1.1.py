items = ["pen", "notebook", "pen", "eraser", "notebook", "pen", "stapler"]

# List: preserves the original arrival order.
item_list = items

# Tuple: stores the first 3 items as an immutable record.
first_batch = tuple(items[:3])

# Set: removes duplicate item names.
unique_items = set(items)

# Dictionary: stores each item with its number of occurrences.
item_count = {}

for item in items:
    item_count[item] = item_count.get(item, 0) + 1

print("List:", item_list)
print("Tuple:", first_batch)
print("Set:", unique_items)
print("Dictionary:", item_count)

# OUTPUT
# List: ['pen', 'notebook', 'pen', 'eraser', 'notebook', 'pen', 'stapler']
# Tuple: ('pen', 'notebook', 'pen')
# Set: {'eraser', 'notebook', 'stapler', 'pen'}
# Dictionary: {'pen': 3, 'notebook': 2, 'eraser': 1, 'stapler': 1}
