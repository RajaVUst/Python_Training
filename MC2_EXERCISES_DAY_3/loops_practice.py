# Multiplication table 

num = 5

for i in range(1,11):
    print(f"{i} * {num} = {i*num}")

"""
Output ->
1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50
"""

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

# 190

# While Loop Practice

num = 5

while num >= 1:
    print(num)
    num -= 1

print("Liftoff!")

"""
Output ->
10
5
4
3
2
1
Liftoff!
"""

# Right angled triangle pattern

n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

"""
Output ->
*
**
***
****
*****
"""

# Vowel Counter

text = input()

count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print(count)

"""
Output->
hello
2
"""