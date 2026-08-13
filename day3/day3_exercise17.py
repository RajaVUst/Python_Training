# Take input from the user
n = int(input("Enter a positive whole number: "))

reversed_n = 0

# Reverse the number
while n > 0:
    reversed_n = reversed_n * 10 + (n % 10)
    n = n // 10

# Display the result
print("Reversed number:", reversed_n)