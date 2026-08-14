def order_summary(item, quantity=1):
    print(f"Order: {quantity} x {item}")
 
order_summary("Notebook")
order_summary("Pen", 5)

# Output:
# Order: 1 x Notebook
# Order: 5 x Pen