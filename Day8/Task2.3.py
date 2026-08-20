
def add_item(item, basket=[]):
    basket.append(item)
    return basket


print("Buggy version:")
print(add_item("apple"))
print(add_item("banana"))

# Why this happens: default argument values are evaluated ONCE, when the
# function is defined -- not each time the function is called. So
# basket=[] creates a single list object reused (and mutated) on every
# call that doesn't pass its own basket. Each call's .append() adds to
# the SAME list, so the second call sees the leftover item from the first.


def add_item_fixed(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


print("\nFixed version:")
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))

# One more example of the same class of bug
def tag_as_processed(record, seen=None):
    if seen is None:
        seen = {}
    seen[record["id"]] = True
    return seen


order_1 = {"id": 1}
order_2 = {"id": 2}
log = {}
tag_as_processed(order_1, log)
tag_as_processed(order_2, log)
print("\nShared log dict (mutated in place across calls):", log)

# If a caller expected log to be untouched after passing it in, this would
# be a surprise -- dicts/lists are passed by reference, so mutating them
# inside a function mutates the caller's original object too.

# OUTPUT:
# Buggy version:
# ['apple']
# ['apple', 'banana']
#
# Fixed version:
# ['apple']
# ['banana']
#
# Shared log dict (mutated in place across calls): {1: True, 2: True}
