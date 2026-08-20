def add_item(item, basket=[]):
    basket.append(item)
    return basket


print(add_item("apple"))
print(add_item("banana"))

# Output:
# ['apple']
# ['apple', 'banana']
# Reasonn: The default list basket=[] is created only once.So the same list is reused when the function is called again.

def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(add_item("apple"))
print(add_item("banana"))

# Output:
# ['apple']
# ['banana']


# Another Example
def add_name(name, names=[]):
    names.append(name)
    return names

print(add_name("John"))
print(add_name("David"))

# Output:
# ['John']
# ['John', 'David']