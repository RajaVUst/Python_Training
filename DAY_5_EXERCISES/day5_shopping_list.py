cart = ["rice", "barley", "wheat"]
cart.append("kerosene")
cart.append("maize")

sorted_list = sorted(cart)

print(cart)
cart.remove("rice")
print(cart)
print(sorted_list)

"""
Output->
['rice', 'barley', 'wheat', 'kerosene', 'maize']
['barley', 'wheat', 'kerosene', 'maize']
['barley', 'kerosene', 'maize', 'rice', 'wheat']
"""