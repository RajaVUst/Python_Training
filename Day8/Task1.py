from collections import Counter
items = ["pen", "notebook", "pen", "eraser", "notebook", "pen", "stapler"]
tuple1=tuple(items[:3])
set_of_items=set(items)
dict_of_items=Counter(items)
print(items)
print(tuple1)
print(set_of_items)
print(dict_of_items)
#Output
"""
['pen', 'notebook', 'pen', 'eraser', 'notebook', 'pen', 'stapler']
('pen', 'notebook', 'pen')
{'notebook', 'eraser', 'pen', 'stapler'}
Counter({'pen': 3, 'notebook': 2, 'eraser': 1, 'stapler': 1})
"""
#tuple is immutable so first batch record is saved and set is for unique elements and dictionary is for frequency
