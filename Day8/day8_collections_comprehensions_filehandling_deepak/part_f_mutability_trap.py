def add_item(item, basket=[]):
    basket.append(item)
    return basket

print(add_item("apple"))
print(add_item("banana"))
# Output:
# ['apple']
# ['apple', 'banana']   <- mutable default reused across calls, not reset

def add_item_fixed(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(add_item_fixed("apple"))
print(add_item_fixed("banana"))
# Output:
# ['apple']
# ['banana']

def register_user(name, all_users={}):
    all_users[name] = "active"
    return all_users

print(register_user("alice"))
print(register_user("bob"))
# Output:
# {'alice': 'active'}
# {'alice': 'active', 'bob': 'active'}   <- alice leaks into bob's call