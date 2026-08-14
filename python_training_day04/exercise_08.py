def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"Passenger: {passenger}")
    print(f"Seat Type: {seat_type}")
    print(f"Meal: {meal}")
    print()

book_ticket("Deepa")

book_ticket("Deepa", meal="Non-Veg")

book_ticket("Deepa", meal="Vegan", seat_type="Business")


#output:
'''Passenger: Deepa
Seat Type: Economy
Meal: Veg

Passenger: Deepa
Seat Type: Economy
Meal: Non-Veg

Passenger: Deepa
Seat Type: Business
Meal: Vegan
'''