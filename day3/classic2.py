num=int(input("enter the number"))

reversed=""

while num!=0:
        last=num%10
        reversed=reversed+str(last)
        num=num//10
print(reversed)