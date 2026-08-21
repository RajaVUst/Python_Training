def add_item(item, basket=[]):
    basket.append(item)
    return basket
print(add_item("apple"))
print(add_item("banana"))
def add_item_fixed(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))
def add_task(task, task_list=[]):
    task_list.append(task)
    return task_list
print(add_task("Study Python"))
print(add_task("Practice Sets"))

# output:
# ['apple']
# ['apple', 'banana']
# ['apple']
# ['banana']
# ['Study Python']
# ['Study Python', 'Practice Sets']