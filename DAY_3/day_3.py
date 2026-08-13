#1
num1=int(input("enter the  whole number:"))
num2=float(input("enter  decimal number:"))
sentence=input("enter the senterce:")
divide=num1/num2
print(f"Whole number :{num1}| {type(num1)}")
print(f"Decimal number :{num2}| {type(num2)}")
print(f"Senyence :{sentence}| {type(sentence)}")
print(f"Division :{divide}| {type(divide)}")


#2
text="Python Readiness Training" 
print(f'{text[:6]}')
print(text[::-1])

#3
a=int(input("enetr tehe first number"))
b=int(input("enter the second number"))
is_equal=(a==b)
a_not_equal_b=(a!=b)
a_greater_b=a>b
a_les_b=a<=b
print(f"A equal b:{is_equal}")
print(f"A not equal b:{a_not_equal_b}")
print(f"a is gretaer than b:{a_greater_b}")
print(f"a is less than b:{a_les_b}")


#4
n=int(input("Enter the number:"))
if n>0:
    print("POsitive number")
elif n<0:
    print("Negative number")    
else:
    print("zero")    


#5
n=int(input("Enter a number"))
if n%2==0:
    print("even number")
else:
    print("Odd number")    


#6
year=int(input("Enter the year:"))
if (year%4==0) and (year%100!=0) or (year%400==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not leap year")    


#7
a=int(input("enter the value"))
b=int(input("enter the value"))
c=int(input("enter the value"))
if a>b and a>c:
    print(f"{a} is greater")
elif b>a and b>c:
    print(f"{b} is greater ")  
else:
    print(f"{c} is greater")      



#8
score=int(input("Enter the score:"))

if score>=90:
    print("A grade")
elif score>=75:
    print("B grade")
elif score>=60:
    print("c grade")
elif score>=40:
    print("D grade") 
else :
    print("Fail")       


 #9
a,b,c=map(int,input("enter the values").split())
if a+b>c and b+c>a and a+c>b:
    print("valid triangle")
else:
    print("Not valid traingle")    

#10
n=int(input("Enter the number:"))
for i in range(1,11):
    print(f"{n} X {i}= {n*i}")


#11
n= int(input("Enter the number:"))
add=0
for num in range(1,n+1):
    add+=num
print(add)

#12
n=int(input("Enter the number:"))#1234
total=0
while n>0:
    digit=n%10
    total=total+digit
    n=n//10
print(total)    



#13
n =int(input("ENter the number:"))
while n>=1:
    print(n)
    n-=1
print("liftofff")    


#14
n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()   


#15
word=input("ENter the word")
count=0
vowel="aeiou"
for i in word.lower():
    if i in vowel:
        count+=1
print(count)        



#16
num=int(input())
for n in range(num):
    if  n%3==0 and n%5==0:
        print("FizzBUzz")
    elif n%5==0:
        print("Buzz")
    elif n%3==0 :
        print("FIZ")
    else:
        print("NOt DIvisible")    


#17
num=int(input("Enter the number"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev) 


#18
num=int(input("Enter the number"))
rev=0
original=num
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if original==rev:
    print(f"{original} is palindrome")
else:
    print(f"{num} is not palindrome")        

#19
num=int(input("Enter the number:"))
count=0
for i in range(1, num+1):
    if num%i==0:
        count+=1

if count==2:
    print("Prime number")
else:
    print("Not prime")            

#20
for num in range(2, 50):
    count=0
    for i in range(1, num+1):
        if num % i==0:
            count+=1
    if count==2:
        print(f"{num}")            
    
#21


num=int(input("ENter the number"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)    

#22
a=0
b=1
for i in range(10):
    print(a)
    c=a+b
    a=b
    b=c


#23
amount=float(input("ENter indian rupees:"))
counrency=input("Enter the counrency")
con=counrency.upper()
if con=="USD":
    result=amount/83
    print(f"{result:.2f} USD")
elif con=="EUR":
    result=amount/90
    print(f"{result:.2f} EUR")
elif con=="GBP":
    result=amount/93
    print(f"{result:.2f} GBP")
else:
    print("Invalid currency")


#24
secret_number = 7
guesses = list(map(int,input().split()))

for guess in guesses:
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct!")
        break



#25
n=int(input())
for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end="")
    print()   