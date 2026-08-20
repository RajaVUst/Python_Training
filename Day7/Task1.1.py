items=[
    "pen", "notebook","pen","eraser",
    "notebook","pen","stapler"
]

arrival_order=items.copy()

first_batch=tuple(items[:3])


unique_items=set(items)

item_count={}

for item in items:
    item_count[item]=item_count.get(item,0)+1


print("Arrival order ", arrival_order)
print("First batch", first_batch)
print("Unique items", unique_items)
print("Item counts ",item_count)


#output
'''
Arrival order  ['pen', 'notebook', 'pen', 'eraser', 'notebook', 'pen', 'stapler']
First batch ('pen', 'notebook', 'pen')
Unique items {'notebook', 'eraser', 'stapler', 'pen'}
Item counts  {'pen': 3, 'notebook': 2, 'eraser': 1, 'stapler': 1}
'''