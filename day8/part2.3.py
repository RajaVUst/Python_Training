def add_item(item, basket=[]):
    basket.append(item)
    return basket

print(add_item("apple"))
print(add_item("banana"))


# PREDICTED OUTCOME 
# apple 
# apple banana

# OUTPUT

# ['apple']
# ['apple', 'banana']