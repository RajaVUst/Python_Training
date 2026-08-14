def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"Passenger: {passenger}")
    print(f"Seat: {seat_type}")
    print(f"Meal: {meal}")
    print()


book_ticket("Saikiran")
book_ticket("Saikiran","premium economy","Hindu non veg")

'''
Passenger: Saikiran
Seat: Economy
Meal: Veg

Passenger: Saikiran
Seat: premium economy
Meal: Hindu non veg
'''