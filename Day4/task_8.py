def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"Passenger: {passenger}")
    print(f"Seat Type: {seat_type}")
    print(f"Meal: {meal}")
book_ticket("Aiswarya")
book_ticket("Aiswarya", meal="Non-Veg")
book_ticket("Aiswarya", meal="Non-Veg", seat_type="Business")

"""
output
Passenger: Aiswarya
Seat Type: Economy
Meal: Veg
Passenger: Aiswarya
Seat Type: Economy
Meal: Non-Veg
Passenger: Aiswarya
Seat Type: Business
Meal: Non-Veg
"""