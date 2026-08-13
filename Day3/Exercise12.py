#Sum of digits
n = int(input("Enter a positive whole number: "))
temp = n
digit_sum = 0
while temp > 0:
    digit_sum += temp % 10
    temp //= 10
print(f"Sum of digits of {n} = {digit_sum}")