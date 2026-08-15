def total_cost(*prices):
    """This is Sum Of all the prices:"""
    return sum(prices)

print(total_cost.__doc__)
print(total_cost(10,20))
print(total_cost(10,20,30,40,50))

#output
# This is Sum Of all the prices:
# 30
# 150



def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    """
    This is A 
    train coach detail,
    How Many people are there and about there seat Type and what they want to have in their meal..

    """
    print(f"Number of Passanger are {passenger} and seat type is {seat_type} and preffered meal that is {meal}")

print(book_ticket.__doc__)
book_ticket(passenger=1)
book_ticket(passenger=1,meal="Non-Veg")
book_ticket(passenger=3, meal="Veg", seat_type="Genaral")


#output
#
#     This is A 
#     train coach detail,
#     How Many people are there and about there seat Type and what they want to have in their meal..
#
#
# Number of Passanger are 1 and seat type is Economy and preffered meal that is Veg
# Number of Passanger are 1 and seat type is Economy and preffered meal that is Non-Veg
# Number of Passanger are 3 and seat type is Genaral and preffered meal that is Veg



def reset_score():
    score = 0
    # 'score' is a local variable — it is created only inside this function
    # and exists only while the function is running.

reset_score()
# Once the function finishes executing, 'score' is destroyed —
# Python removes it from memory since it's no longer needed.

print(score)
# This line throws NameError: name 'score' is not defined
# because 'score' was never created outside the function.
# Local variables cannot be accessed from outside their function.

