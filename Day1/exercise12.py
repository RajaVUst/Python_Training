n = 15
div_by_3 = (n % 3 == 0)
div_by_5 = (n % 5 == 0)
div_by_both = div_by_3 and div_by_5
print(f"Divisible by 3: {div_by_3}")
print(f"Divisible by 5: {div_by_5}")
print(f"Divisible by both: {div_by_both}")