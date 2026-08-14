def order_summary(item, quantity=1):
    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
order_summary("Laptop")
order_summary("Mouse", 3)

"""
output
Item: Laptop
Quantity: 1
Item: Mouse
Quantity: 3
"""