# 19: Prime number check
num=int(input("Enter a number: "))
flag=0
for i in range(2,num):
    if num%i==0:
        flag+=1
        print(f"{num} it is not a prime number")
        break
if flag==0:
    print(f"{num} is a prime number")