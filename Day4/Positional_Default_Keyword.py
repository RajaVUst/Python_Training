def order_summary(item, quantity=1):
    print(f"The iten name is {item} and qunatity is {quantity}")

order_summary("Bottle")
order_summary("Laptop",2)

#output
#The iten name is Bottle and qunatity is 1
#The iten name is Laptop and qunatity is 2

def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"Number of Passanger are {passenger} and seat type is {seat_type} and preffered meal that is {meal}")

book_ticket(passenger=1)
book_ticket(passenger=1,meal="Non-Veg")
book_ticket(passenger=3, meal="Veg", seat_type="Genaral")

# Output:
# Number of Passanger are 1 and seat type is Economy and preffered meal that is Veg
# Number of Passanger are 1 and seat type is Economy and preffered meal that is Non-Veg
# Number of Passanger are 3 and seat type is Genaral and preffered meal that is Veg


def total_cost(*prices):
    return sum(prices)

print(total_cost(10,20))
print(total_cost(10,20,30,40,50))

#output
#30
#150


def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_student_info(
    name="Harsh",
    age=22,
    course="Python",
    city="Trivandrum"
)

# Output:
# name: Harsh
# age: 22
# course: Python
# city: Trivandrum
