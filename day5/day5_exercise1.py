cart = ["Milk", "Bread", "Eggs"]

cart.append("Rice")
cart.append("Apples")

cart.remove("Bread")

print("Original cart:", cart)
print("Sorted cart:", sorted(cart))

'''OUTPUT
Original cart: ['Milk', 'Eggs', 'Rice', 'Apples']
Sorted cart: ['Apples', 'Eggs', 'Milk', 'Rice']
'''