# Task 7
def order_summary(item, quantity=1):
    print(f'item = {item}, quantity = {quantity}')
order_summary('horlicks')  
order_summary('iphone', 1)

# output

# item = horlicks, quantity = 1
# item = iphone, quantity = 1

# Task 8

def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f'{passenger}, {seat_type}, {meal}')
book_ticket('arun')
book_ticket('senin',meal = 'non veg')
book_ticket('akshay', seat_type='business', meal='non veg' )

#output

# arun, Economy, Veg
# senin, Economy, non veg
# akshay, business, non veg

# Task 9

def total_cost(*prices):
    return sum(prices)
print('Total of two prices:' , total_cost(10, 20))
print('Total of five prices:', total_cost(10, 20, 10, 5, 5))

#output 

# Total of two prices: 30
# Total of five prices: 50

# Task 10

def print_student_info(**details):
    for key, value in details.items():
        print(f'{key}: {value}')

print_student_info(name='anu', roll_n0='28', batch='2026')