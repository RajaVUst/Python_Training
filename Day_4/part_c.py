#task 7
def order_summary(item, quantity=1):
    print(f"{item} , {quantity}")

order_summary("Pen")
order_summary("Pen", 5)

#output
'''Pen , 1
Pen , 5'''

#task 8
def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"name : {passenger}, seat_type : {seat_type}, meal : {meal}")

book_ticket("JS")
book_ticket("JJS", meal = "Non-veg")
book_ticket("JS", meal = "Egg", seat_type = "First class") 

#output
'''name : JS, seat_type : Economy, meal : Veg
name : JJS, seat_type : Economy, meal : Non-veg
name : JS, seat_type : First class, meal : Egg'''

#task 9
def total_cost(*prices):
    print(sum(prices))

total_cost(1,2)
total_cost(1,6,5,7,8)

#output
'''3
27'''

#task 10

def print_student_info(**details):
    print(details)   # details is a dict
    for key, value in details.items():
        print(f"{key}: {value}")
 
print_student_info(name="Jay", age=19, degree="BE", place="NYC")

#output
'''{'name': 'Jay', 'age': 19, 'degree': 'BE', 'place': 'NYC'}
name: Jay
age: 19
degree: BE
place: NYC'''


