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


# output:
# List: ['pen', 'notebook', 'pen', 'eraser', 'notebook', 'pen', 'stapler']
# Tuple: ('pen', 'notebook', 'pen')
# Set: {'notebook', 'stapler', 'eraser', 'pen'}
# Dictionary: {'pen': 3, 'notebook': 2, 'eraser': 1, 'stapler': 1}


