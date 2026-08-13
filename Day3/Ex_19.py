num=int(input("Enter a number: "))
temp=0
for i in range(2,num):
    if num%i==0:
        temp+=1
        print(f"{num} is not a prime number")
        break
if temp==0:
    print(f"{num} is a prime number")