num=int(input("enter the number"))
temp=num

reversed=""

while num!=0:
        last=num%10
        reversed=reversed+str(last)
        num=num//10
reversed_num=int(reversed)

if reversed_num==temp:
        print("Palindrome")
else:
    print("Not palindrome")
