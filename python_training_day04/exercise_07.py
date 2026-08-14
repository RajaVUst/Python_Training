def order_summary(item, quantity=1):
    print(f"Item: {item}")
    print(f"Quantity: {quantity}")

order_summary("Notebook")
order_summary("Pen", 5)


#output:
'''Item: Notebook
Quantity: 1
Item: Pen
Quantity: 5'''