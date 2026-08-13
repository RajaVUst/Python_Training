n = 27

div_by_3 = n%3 == 0
div_by_5 = n%5 == 0

div_by_both = div_by_3 and div_by_5

print(f"By 3 {div_by_3}, By 5 {div_by_5}, By both {div_by_both}")