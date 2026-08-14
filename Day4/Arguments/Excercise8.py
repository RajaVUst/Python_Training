# book_ticket()

def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print("Passenger:", passenger)
    print("Seat:", seat_type)
    print("Meal:", meal)

# only passenger
book_ticket("Logesh")

#change only meal
book_ticket("Logesh", meal="Non-Veg")

#change both using keywords
book_ticket("Logesh", meal="Non-Veg", seat_type="Business")

# Output:
# Passenger: Logesh
# Seat: Economy
# Meal: Veg
# Passenger: Logesh
# Seat: Economy
# Meal: Non-Veg
# Passenger: Logesh
# Seat: Business
# Meal: Non-Veg
