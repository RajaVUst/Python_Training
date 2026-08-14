def show_square(number):
    """Prints the square of the given number."""
    print(number ** 2)

def total_cost(*prices):
    """Returns the sum of any number of prices passed in."""
    return sum(prices)

show_square(6)
print(total_cost(100, 250, 50))
help(show_square)
help(total_cost)

# Output:
# 36
# 400
# Help on function show_square in module __main__:
#
# show_square(number)
#     Prints the square of the given number.
#
# Help on function total_cost in module __main__:
#
# total_cost(*prices)
#     Returns the sum of any number of prices passed in.