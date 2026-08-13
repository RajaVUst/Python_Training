num=int(input("enter the number"))
sum=0
while num!=0:
    last_dig=num%10
    sum+=last_dig
    num=num//10

print(sum)