# Part C: Positional, Default & Keyword Arguments

# Task 7
def order_summary(item, quantity=1):
    print(f"Order: {quantity} x {item}")
order_summary("Laptop")
order_summary("Laptop", 3)
# Output:
# Order: 1 x Laptop
# Order: 3 x Laptop


# Task 8
def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"Passenger: {passenger}, Seat: {seat_type}, Meal: {meal}")
book_ticket("Varsha")
book_ticket("Varsha", meal="Non-Veg")
book_ticket("Varsha", meal="Veg", seat_type="Business")
# Output:
# Passenger: Varsha, Seat: Economy, Meal: Veg
# Passenger: Varsha, Seat: Economy, Meal: Non-Veg
# Passenger: Varsha, Seat: Business, Meal: Veg


# Task 9
def total_cost(*prices):
    return sum(prices)
print(total_cost(100, 200))
print(total_cost(50, 100, 150, 200, 250))
# Output:
# 300
# 750


# Task 10
def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
print_student_info(
    name="Varsha",
    age=24,
    course="Python",
    city="Trivandrum"
)
# Output:
# name: Varsha
# age: 24
# course: Python
# city: Trivandrum