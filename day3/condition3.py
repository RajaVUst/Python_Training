num=int(input("enter the year"))

if num%400==0:
    print("It is a leap year")
elif num%100==0:
    print("not  leap year")
elif num%4==0:
    print("it is  a leap year")
else:
    print("not a leap year")