#Palindrome check for an integer
n = int(input("Enter a positive whole number: "))
temp = n
reversed_n = 0
while temp > 0:
    reversed_n = reversed_n * 10 + (temp % 10)
    temp //= 10
if n == reversed_n:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")