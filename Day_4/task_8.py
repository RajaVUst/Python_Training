def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"Passenger: {passenger}")
    print(f"Seat Type: {seat_type}")
    print(f"Meal: {meal}")

book_ticket("Rahul")
book_ticket("Priya", meal="Non-Veg")
book_ticket("Arjun", meal="Jain", seat_type="Business")

# output:
# Passenger: Rahul
# Seat Type: Economy
# Meal: Veg
# Passenger: Priya
# Seat Type: Economy
# Meal: Non-Veg
# Passenger: Arjun
# Seat Type: Business
# Meal: Jain