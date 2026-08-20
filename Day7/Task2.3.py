def broken_add_item(item, basket=[]):
    basket.append(item)
    return basket


print("Broken function:")
print(broken_add_item("apple"))
print(broken_add_item("banana"))



def add_item(item, basket=None):
    if basket is None:
        basket = []

    basket.append(item)
    return basket


print("\nFixed function:")
print(add_item("apple"))
print(add_item("banana"))


def add_permission(user, permissions={"roles": []}):
    permissions["roles"].append("admin")
    return user, permissions


print("\nMutable dictionary bug:")
print(add_permission("Alice"))
print(add_permission("Bob"))

#output

'''
Broken function:
['apple']
['apple', 'banana']

Fixed function:
['apple']
['banana']

Mutable dictionary bug:
('Alice', {'roles': ['admin']})
('Bob', {'roles': ['admin', 'admin']})
'''