# Task 7
def order_summary(item, quantity=1):
    print(f"{item} of {quantity} quantity")
                                # Output
order_summary("Indian Flag")    # Indian Flag of 1 quantity
order_summary("Ballons",16)     # Ballons of 16 quantity

# Task 8
def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"{passenger} booked {seat_type} Seat with {meal} meals")
                                        # Output
book_ticket("Arsha")                    # Arsha booked Economy Seat with Veg meals
book_ticket("Reni",meal = "Non-Veg")    # Reni booked Economy Seat with Non-Veg meals
book_ticket(seat_type = "Business",meal = "Veg", passenger = "Raja")    # Raja booked Business Seat with Veg meals

# Task 9
def total_cost(*prices):
    return sum(prices)
                                      # Output
print(total_cost(49,199))             # 248
print(total_cost(20,60,99,299,300))   # 778

# Task 10
def print_student_info(**details):  # Output
    print(details)                  # {'id': 219, 'name': 'Menon', 'course': 'Python', 'section': 'B'}
    for key,value in details.items():
        print(key,":",value)        # id :219
                                    # name : Menon
                                    # course : Python
                                    # section : B

print_student_info(id = 219, name = "Menon",course = "Python", section = "B")