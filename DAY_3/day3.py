##exercise 1
number = int(input("Enter a whole number : "))
decimal = float(input("Enter a decimal number : "))
text = input("Enter name :")
result = number/decimal
print(f"{number} is of type {type(number)}")
print(f"{decimal} is of type {type(decimal)}")
print(f"{text} is of type {type(text)}")
print(f"result when number is divided with decimal : {result:.2f}")


# exercise 2

Strrr = "Python Readiness Training"
print(Strrr[0:6])
print(Strrr[::-1])

#Exercise 3

a = int(input("Enter any number : "))
b= int(input ("ENter another number : "))
print("a == b : ",a == b)
print("a > b : " ,a > b)
print ("a < b : ", a < b )
print("a != b : ", a != b)
print("a <= b : ", a <= b)

#Exercise 4

num = int(input("Enter any number : "))
if num>0:
    print(f"{num} is positive number")
elif num == 0:
    print(f"{num} is Zero")
else:
    print(f"{num} is negative number")

#Exercise 5

num = int(input("Enter any number : "))
if num%2 == 0:
    print(f"{num} is Even number")
else:
    print(f"{num} is odd number")


#Exercise 6

year = int(input("Enter Year : "))
if year%4 == 0 and (year%100 != 0 or year%400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


#Exercise 7
a,b,c = map(int,input("Enter Three numbers : ").split())
if a>b and a>c:
    print(f"{a} a is greater that {b} , {c}")
elif b>a and b>c:
    print(f"{b} b is greater that {a} , {c}")
else:
    print(f"{c} c is greater that {a} , {b}")


EExercise 8

score = int(input("Enter score : "))
if score>=90:
    print("Your grade is A")
elif 90>score>=75:
    print("Your grade is B")
elif 75>score>=60:
    print("Your grade is C")
elif 60>score>=40:
    print("Your grade is D")
else:
    print("Your grade is F")


#exercise 9

a,b,c = map(int,input("Enter Three side length of the triangle : ").split())
if a+b>c and a+c>b and b+c>a:
    print("Valid triangle")
else:
    print("Not a valid triangle")

#exercise 10

num = int(input("Enter any number : "))
for i in range(11):
    prod = num*i
    print(f"{num} * {i} = {prod}" ) 

#exercise 11

num = int(input("Enter any number : "))
sum = 0
for i in range(num+1):
    sum = i + sum
print(f"sum of {num} whole number:  {sum}" ) 

#exercise 12

num = int(input("Enter any number : "))
sum = 0
while num>0:
    b = num%10
    sum = sum + b
    num = num//10
print(f"sum of all digits : {sum}")


#exercise 13
num = int(input("Enter any number : "))
while num>=1:
    print(num)
    num = num-1
print("Liftoff!")


excersie 14

num = int(input("Enter no.of rows : "))
for i in range(num+1):
    for j in range(i):
        print('*',end='')
    print()

i = num
while i>=1:
    for j in range(i):
        print('*',end='')
    print()
    i = i-1


#exercise 15

sentence = input("Enter any sentence for vowel count : ")
vowel = 'aeiouAEIOU'
count=0
for i in sentence:
    if i in vowel:
        count += 1
print("count of vowels in sentence or word : ",count)


#exerscie 16
for i in range(1,51):
    if i%3 == 0 and i%5 == 0:
        print(f"{i} is FizzBuzz")
    elif i%3 == 0:
        print(f"{i} is Fizz")
    elif i%5 == 0:
        print(f"{i} is Buzz")
    else:
        print("Not divisble")


#exercise 17

num  = int(input("Enter any number : "))
reverse = 0
while num>=1:
    digit = num%10
    reverse = reverse*10 +digit
    num = num//10
print("reverse of given number : ",reverse)

#exercise 18
num  = int(input("Enter any number : "))
og = num
reverse = 0
while num>=1:
    digit = num%10
    reverse = reverse*10 +digit
    num = num//10
if reverse == og:
    print(f"{og} is palindrome")
else:
    print(f"{og} is not a palindrome")

#exercise 19

num =  int(input("Enter a number : "))
count = 0
for i in range(1,num+1):
    if num%i == 0:
        count += 1
if count==2:
    print("It is prime number")
else:
    print("It is not a prime number")


#excersie 20
num =  int(input("Enter a number : "))

for i in range(1,num+1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
    if count==2:
        print(f"{i} It is prime number")
    else:
        print(f"{i} It is not a prime number")


#exercise 21

num =  int(input("Enter a number : "))
og = num
factorial = 1
while num>=1:
    factorial = factorial*num
    num = num-1
print(f" factorial of number {og} : {factorial}")

#excerise 22
a = 0
b = 1
for i in range(15):
    print(a , end=' ')
    a,b = b,a+b


#exercise 23

amount = int(input("Enter amount : "))
convertion =  input("Which country currency you want to convert USD, EUR, or GBP :")
con = convertion.lower()
if con == 'usd':
    con_amount = amount/90
    print(f"amount converted to USD : {con_amount:.2f}")
elif con == 'eur':
    con_amount = amount/105
    print(f"amount converted to EUR : {con_amount:.2f}")
elif con == 'gbp':
    con_amount = amount/120
    print(f"amount converted to EUR : {con_amount:.2f}")
else: 
    print("Incorrect target country currency")


#exercise 24

secret_number = 7

guesses = [3, 10, 5, 7, 9]

for guess in guesses:
    if guess > secret_number:
        print(f"{guess} → Too high")
    elif guess < secret_number:
        print(f"{guess} → Too low")
    else:
        print(f"{guess} → Correct!")
        break


#exercise 25:

num = int(input("Enter number rows : "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end='')
    print()









