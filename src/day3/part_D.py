
n = int(input("Enter a number : "))

for i in range(1 , 11):
    print(f"{i} * {n} = {i*n}")

total = 0;

for i in range(1 , n+1):
    total = total + i
print(f"The total is {total}")

num = int(input("Enter a positive whole number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of digits:", sum)

n1 = int(input("Enter the starting number: "))

while n1 >= 1:
    print(n1)
    n1 = n1 - 1

print("Liftoff!")

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):

    for j in range(i):
        print("*", end="")

    print()

text = input("Enter a word or sentence: ")

count = 0

for ch in text:

    if ch.lower() in "aeiou":
        count = count + 1

print("Number of vowels:", count)
