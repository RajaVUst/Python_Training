items = ["pen", "notebook", "pen", "eraser", "notebook", "pen", "stapler"]

my_list=items

print(my_list)

tuple_of_three_items=tuple(my_list[:3])

print(tuple_of_three_items)

set_of_unique=set(items)

print(set_of_unique)

item_dict={}

for item in items:
    item_dict[item]=item_dict.get(item,0)+1

print(item_dict)

# OUTPUT
# ['pen', 'notebook', 'pen', 'eraser', 'notebook','pen', 'stapler']
# ('pen', 'notebook', 'pen')
# {'pen', 'stapler', 'eraser', 'notebook'}
# {'pen': 3, 'notebook': 2, 'eraser': 1, 'stapler': 1}
