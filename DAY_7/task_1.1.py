items = ["pen", "notebook", "pen", "eraser", "notebook", "pen", "stapler"]

# List: preserves arrival order, allows duplicates
arrival_list = list(items)

# Tuple: immutable snapshot of first 3 items
first_batch = tuple(items[:3])

# Set: only unique names, order doesn't matter
unique_items = set(items)

# Dict: count occurrences — fast key-based lookup per item
item_count = {}
for item in items:
    item_count[item] = item_count.get(item, 0) + 1

print("List (arrival order):", arrival_list)
print("Tuple (first batch):", first_batch)
print("Set (unique items):", unique_items)
print("Dict (item counts):", item_count)
