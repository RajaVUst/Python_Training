# Multiplication table 
num = 5

for i in range(1,11):
    print(f"{i} * {num} = {i*num}")

# Sum of whole numbers

num = 20
sum = 0

for i in range(1,num):
    sum+=i
print(sum)

# Sum of individual digits

num = 1234
sum = 0

while num>0:
    digit = num%10
    sum+=digit
    num = num//10

print(sum)

# While Loop Practice

num = 5

while num >= 1:
    print(num)
    num -= 1

print("Liftoff!")

# Right angled triangle pattern

n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# Vowel Counter

text = input()

count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print(count)