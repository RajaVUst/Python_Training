def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"{passenger} | Seat: {seat_type} | Meal: {meal}")
 
book_ticket("Kiran")                             
book_ticket("Meera", meal="NonVeg")                
book_ticket("Arjun", meal="Jain", seat_type="Business") 

# Output:
# Kiran | Seat: Economy | Meal: Veg
# Meera | Seat: Economy | Meal: NonVeg
# Arjun | Seat: Business | Meal: Jain