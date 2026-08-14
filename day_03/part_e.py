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