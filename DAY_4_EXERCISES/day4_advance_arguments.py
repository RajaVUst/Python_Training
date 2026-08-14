# Default value of argument

def order_summary(item, quantity=1):
    print(f"{item} with quantity {quantity}")

order_summary("Rice")
order_summary("Mango", 5)

"""
Output ->
Rice with quantity 1
Mango with quantity 5
"""

# Multiple arguments

def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"Passenger: {passenger}, Seat Type: {seat_type}, Meal: {meal}")

book_ticket("Pranav")
book_ticket("Pranav", meal="Non-Veg")
book_ticket("Pranav", meal="Vegan", seat_type="Business")

"""
Output ->
Passenger: Pranav, Seat Type: Economy, Meal: Veg
Passenger: Pranav, Seat Type: Economy, Meal: Non-Veg
Passenger: Pranav, Seat Type: Business, Meal: Vegan
"""

# Using *args

def total_cost(*prices):
    return sum(prices)

print("Total (2 prices):", total_cost(100, 250))
print("Total (5 prices):", total_cost(50, 75, 100, 125, 150))

"""
Output ->
Total (2 prices): 350
Total (5 prices): 500
"""

# Using kwargs

def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_student_info(
    name="Pranav",
    age=24,
    course="Python",
    city="Trivandrum"
)

"""
Output ->
name: Pranav
age: 24
course: Python
city: Trivandrum
"""