# Default argument

def order_summary(item, quantity=1):
    print("Item:", item)
    print("Quantity:", quantity)

order_summary("Laptop")
order_summary("Pen", 5)

# Output:
# Item: Laptop
# Quantity: 1
# Item: Pen
# Quantity: 5