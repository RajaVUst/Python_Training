
items = ["pen", "notebook", "pen", "eraser", "notebook", "pen", "stapler"]


item_list = items.copy()

first_batch = tuple(items[:3])

unique_items = set(items)

item_count = {}

for item in items:
    item_count[item] = item_count.get(item, 0) + 1

print("List:", item_list)
print("Tuple:", first_batch)
print("Set:", unique_items)
print("Dictionary:", item_count)

# Output:
# List: ['pen', 'notebook', 'pen', 'eraser', 'notebook', 'pen', 'stapler']
# Tuple: ('pen', 'notebook', 'pen')
# Set: {'pen', 'notebook', 'eraser', 'stapler'}
# Dictionary: {'pen': 3, 'notebook': 2, 'eraser': 1, 'stapler': 1}