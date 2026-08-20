# Predicted output BEFORE running:
#   ['apple']
#   ['apple', 'banana']
# Reason: the default list [] is created ONCE when the function is defined,
# not on every call. All calls without an explicit basket share the same object.

def add_item(item, basket=[]):
    basket.append(item)
    return basket

print(add_item("apple"))
print(add_item("banana"))

# --- Fixed version: use None as sentinel, create a fresh list each call ---
def add_item_fixed(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print("\nFixed:")
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))

# --- Own mutability bug example ---
# Bug: two "separate" user records silently share the same tags list
def create_user(name, tags={}):
    tags[name] = "active"
    return tags

u1 = create_user("alice")
u2 = create_user("bob")
print("\nMutability bug — both calls share the same dict:", u1, u2)
# u1 and u2 are the SAME dict object, so u1 shows bob's entry too
