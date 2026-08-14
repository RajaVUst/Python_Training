def say_hello():
    """Prints a greeting message."""
    print("Hello, Python learner!")


def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    """Prints the passenger's ticket details."""
    print(f"Passenger: {passenger}")
    print(f"Seat Type: {seat_type}")
    print(f"Meal: {meal}")


# Check docstrings
help(say_hello)
help(book_ticket)