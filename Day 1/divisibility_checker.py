n=int(input("enter the number:"))
divisible_by_3 = n % 3 == 0
divisible_by_5 = n % 5 == 0
divisible_by_both = divisible_by_3 and divisible_by_5
print(f"Divisible by 3: {divisible_by_3}")
print(f"Divisible by 5: {divisible_by_5}")
print(f"Divisible by both: {divisible_by_both}")