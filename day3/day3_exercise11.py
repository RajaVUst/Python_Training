# input a number
n = int(input("Enter a number: "))

# initialize sum to 0
sum = 0

# print the sum of numbers from 1 to n
for i in range(n+1):
    # add the value of n to sum
    sum = sum + i

# print the total
print(sum)