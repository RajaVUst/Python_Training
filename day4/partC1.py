def order_summary(item,quantity=1):
    print(f"item:{item},quantity:{quantity}")
    
order_summary("Oneplus")
order_summary("Chocolate",10)
order_summary(quantity=20,item="watch")


# OUTPUT
# item:Oneplus,quantity:1
# item:Chocolate,quantity:10
# item:watch,quantity:20