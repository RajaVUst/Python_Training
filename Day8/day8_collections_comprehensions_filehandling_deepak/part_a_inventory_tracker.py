items = ["pen", "notebook", "pen", "eraser", "notebook", "pen", "stapler"]

arrival_order = list(items)                
first_batch = tuple(items[:3])               
unique_items = set(items)                    
item_counts = {}                             
for item in items:
    item_counts[item] = item_counts.get(item, 0) + 1

print(arrival_order)
print(first_batch)
print(unique_items)
print(item_counts)
# Output:
# ['pen', 'notebook', 'pen', 'eraser', 'notebook', 'pen', 'stapler']
# ('pen', 'notebook', 'pen')
# {'stapler', 'notebook', 'pen', 'eraser'}
# {'pen': 3, 'notebook': 2, 'eraser': 1, 'stapler': 1}