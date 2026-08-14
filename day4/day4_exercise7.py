def order_summary(item, quantity=1):
    print(f"Item: {item}, Quantity: {quantity}")


# Call with only item
order_summary("Pizza")

# Call with both arguments
order_summary("Burger", 3)

'''
OUTPUT:
Item: Pizza, Quantity: 1
Item: Burger, Quantity: 3
'''