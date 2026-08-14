def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"Passenger: {passenger}")
    print(f"Seat Type: {seat_type}")
    print(f"Meal: {meal}")
    print()

book_ticket("Aron")
book_ticket("Aron", meal="Non-Veg")
book_ticket("Aron", meal="Non-Veg", seat_type="Business")

'''
OUTPUT:
Passenger: Aron
Seat Type: Economy
Meal: Veg

Passenger: Aron
Seat Type: Economy
Meal: Non-Veg

Passenger: Aron
Seat Type: Business
Meal: Non-Veg
'''