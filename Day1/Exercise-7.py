# Exercise 7 — Variable Swap
first_val = 5
second_val = 10
holder = first_val
first_val = second_val
second_val = holder
first_val, second_val = second_val, first_val
print(first_val)
print(second_val)