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