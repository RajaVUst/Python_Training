def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"passenger name:{passenger},seat type={seat_type},meal={meal}")
    
book_ticket("Bonny")
book_ticket("Bonny",meal="Non-Veg")
book_ticket("Bonny",meal="Non-Veg",seat_type="First class")    

# OUTPUT

# passenger name:Bonny,seat type=Economy,meal=Veg
# passenger name:Bonny,seat type=Economy,meal=Non-Veg
# passenger name:Bonny,seat type=First class,meal=Non-Veg