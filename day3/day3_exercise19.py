# input a number
n = int(input("Enter a whole number: "))

# flag variable
is_prime = True

if n == 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

# print whether number is prime or not
if is_prime == True:
    print("Prime number")
else:
    print("Not prime")