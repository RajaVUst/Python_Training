def book_ticket(passenger, seat_type = "Economy", meal = "Veg"):
    print(f"passenger name is {passenger}")
    print(f"seat type is {seat_type}")
    print(f"meal preference {meal}")
book_ticket("Merin")

# output
# passenger name is Merin
# seat type is Economy
# meal preference Veg

def book_ticket(passenger, seat_type = "Economy", meal = "Veg"):
    print(f"passenger name is {passenger}")
    print(f"seat type is {seat_type}")
    print(f"meal preference {meal}")
book_ticket("Merin", meal = "Non Veg")

# output
# passenger name is Merin
# seat type is Economy
# meal preference Non Veg


def book_ticket(passenger, seat_type = "Economy", meal = "Veg"):
    print(f"passenger name is {passenger}")
    print(f"seat type is {seat_type}")
    print(f"meal preference {meal}")
book_ticket("Merin", meal="Non-Veg", seat_type="Business")

# output
# passenger name is Merin
# seat type is Business
# meal preference Non-Veg





