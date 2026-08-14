# Task 7: Order Summary
def order_summary(item, quantity=1):
    print(f"{quantity} x {item}")

order_summary("Notebook")
order_summary("Pen", 5)
# Output:
# 1 x Notebook
# 5 x Pen


# Task 8: Book Ticket
def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"{passenger} - {seat_type} - {meal}")

book_ticket("Navya")
book_ticket("Navya", meal="Non-Veg")
book_ticket("Navya", meal="Non-Veg", seat_type="Business")
# Output:
# Navya - Economy - Veg
# Navya - Economy - Non-Veg
# Navya - Business - Non-Veg


# Task 9: Total Cost 
def total_cost(*prices):
    return sum(prices)

print(total_cost(100, 200))
print(total_cost(10, 20, 30, 40, 50))
# Output:
# 300
# 150


# Task 10: Print Student Info 
def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_student_info(name="Navya", age=23, course="Python", city="Hyderabad")
# Output:
# name: Navya
# age: 23
# course: Python
# city: Hyderabad