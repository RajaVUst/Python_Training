def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(passenger,seat_type,meal)

book_ticket('pass1')
book_ticket(passenger='pass2',seat_type="first class")
book_ticket(passenger='pass3',seat_type='first class',meal='Vege')

#Output
"""pass1 Economy Veg
pass2 first class Veg
pass3 first class Vege"""