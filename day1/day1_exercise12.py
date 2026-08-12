# store a value in a variable
n = 20

# check if the number is divisible by 3, 5, or both
div_by_3 = (n % 3 == 0)
div_by_5 = (n % 5 == 0)
div_by_both = div_by_3 and div_by_5

# print the results
print(f"{n} is divisible by 3: {div_by_3}")
print(f"{n} is divisible by 5: {div_by_5}")
print(f"{n} is divisible by both 3 and 5: {div_by_both}")