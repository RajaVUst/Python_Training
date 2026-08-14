def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(passenger)
    print(seat_type)
    print(meal)
book_ticket("yesh")
book_ticket("yesh",meal="non-veg")
book_ticket("yesh",seat_type="Ac",meal="chinese")

#output
"""yesh
Economy
Veg
yesh
Economy
non-veg
yesh
Ac
chinese"""