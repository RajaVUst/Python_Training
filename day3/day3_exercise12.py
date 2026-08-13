# input a number
num = int(input("Enter a number: "))

while num != 0:
    rem = num % 10
    sum = sum + rem
    num = num // 10

# print the result
print(sum)