items = ["pen", "notebook", "pen", "eraser", "notebook", "pen", "stapler"]
item_list = items
first_three = tuple(items[:3])
unique_items = set(items)
item_count = {}

for item in items:
    if item in item_count:
        item_count[item] += 1
    else:
        item_count[item] = 1

print("List:", item_list)
print("Tuple:", first_three)
print("Set:", unique_items)
print("Dictionary:", item_count)

# Output:
# List: ['pen', 'notebook', 'pen', 'eraser', 'notebook', 'pen', 'stapler']
# Tuple: ('pen', 'notebook', 'pen')
# Set: {'stapler', 'eraser', 'pen', 'notebook'}
# Dictionary: {'pen': 3, 'notebook': 2, 'eraser': 1, 'stapler': 1}

# List: keeps all items in the original arrival order and allows duplicates
# Tuple: stores the first 3 items in a fixed, unchangeable collection
# Set: stores only unique item names and automatically removes duplicates
# Dictionary: stores each item as a key and its number of occurrences as the value
