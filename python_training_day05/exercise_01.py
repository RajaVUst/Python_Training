cart = ["milk", "bread", "eggs"]

cart.append("rice")
cart.append("sugar")

cart.remove("bread")

print("Original cart:", cart)
print("Sorted cart:", sorted(cart))


#output:
'''Original cart: ['milk', 'eggs', 'rice', 'sugar']
Sorted cart: ['eggs', 'milk', 'rice', 'sugar']'''