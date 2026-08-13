# Exercise 10: Multiplication table
n = 14

for i in range(1,11):
    print(f"{n} x {i} = {n*i}") 

# Exercise 11: Sum of first N natural numbers
sum = 0
for i in range(n+1):
    sum+=i
print(f"Sum of first {n} natural nos is {sum}")

# Exercise 12: Sum of digits
num = 3609
sd = 0
while num>0:
    sd+= num % 10;
    num //= 10
print("Sum of digits:",sd)

# Exercise 13: Countdown with a while loop
while n>0:
    print(n)
    n-=1
else:
    print("Liftoff!")

# Exercise 14: Right-angled triangle pattern
num = 5
for i in range(1,num+1):
    for j in range(i):
        print("*",end=' ')
    print()

# Exercise 15: Vowel counter
word = "your first class"
count = 0
for ch in word:
    if ch in 'aeiou':
        count+=1
print(f"Vowels count {count}")