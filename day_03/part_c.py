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
