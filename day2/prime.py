num=int(input("Enter the number to check whether it is prime or not"))
count=0
for i in range(1,num+1):
    if num % i==0:
        count=count+1

if count==2:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")