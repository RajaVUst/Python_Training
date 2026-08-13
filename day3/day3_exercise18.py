# Take input from the user
n = int(input("Enter a positive whole number: "))
# store the input in a temp variable
temp = n

reversed_n = 0

# Reverse the number
while n > 0:
    reversed_n = reversed_n * 10 + (n % 10)
    n = n // 10

# Check if number is palindrome
if temp == reversed_n:
    print("Palindrome")
else:
    print("Not a palindrome")