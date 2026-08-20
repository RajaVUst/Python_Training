def add_item(item, basket=[]):
    basket.append(item)
    return basket
 
print(add_item("apple"))
print(add_item("banana"))
 
def add_item(item, basket=None):
    if basket is None:
        basket = []
 
    basket.append(item)
    return basket
 
print(add_item("apple"))
# ['apple']
 
print(add_item("banana"))
# ['banana']
 
# The output is ['apple'] then ['apple', 'banana'] because the default list basket=[] is created only once and reused across function calls, so changes persist between calls.
 