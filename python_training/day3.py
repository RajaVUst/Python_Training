
#Exercise 1
# whole = 10
# decimal = 2.5
# text = "Python"

# print(f"{whole} is of type {type(whole)}")
# print(f"{decimal} is of type {type(decimal)}")
# print(f"{text} is of type {type(text)}")

# result = whole / decimal
# print(f"Division result: {result}")


#exercise 2
# text = "Python Readiness Training"

# print(text[0:6])
# print(text[::-1])






# #exercise 3
# a = 10
# b = 20

# print(a == b)
# print(a != b)
# print(a > b)
# print(a <= b)




# age = 20 
 
# if age >= 18: 
#     print("You can vote") 






# age = 15 
 
# if age >= 18: 
#     print("You can vote") 
# else: 
#     print("Not old enough yet") 


# marks = 67 
 
# if marks >= 90: 
#     print("Grade A") 
# elif marks >= 75: 
#     print("Grade B") 
# elif marks >= 60: 
#     print("Grade C") 
# else: 
#     print("Grade D") 


# temperature = 33 
# is_raining = False 





 
# if temperature > 30 and not is_raining: 
#     print("Good day for a walk") 
# else: 
#     print("Maybe stay in") 



# for i in range(1, 6): 
#     print(f"Iteration {i}") 






# for n in range(1, 11): 
#     if n % 2 == 0: 
#         print(f"{n} is even") 
#     else: 
#         print(f"{n} is odd") 






#exercise 4

# num = float(input("Enter a number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")




#exercise 5

# num = int(input("Enter a whole number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


#exercise 6
# year = int(input("Enter year: "))

# if year % 400 == 0:
#     print("Leap year")
# elif year % 100 == 0:
#     print("Not a leap year")
# elif year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")


#exercise 7

# a = input("Enter a: ")
# b = input("Enter b: ")
# c = input("Enter c: ")

# if a >= b and a >= c:
#     print("Largest:", a)
# elif b >= a and b >= c:
#     print("Largest:", b)
# else:
#     print("Largest:", c)


#exercise 8
# marks = float(input("Enter marks: "))

# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 60:
#     print("Grade C")
# elif marks >= 40:
#     print("Grade D")
# else:
#     print("Grade F")



#exercise 9
# side1=int(input("Enter side 1: "))
# side2=int(input("Enter side 2: "))
# side3=int(input("Enter side 3: "))
# if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
#     print("Valid triangle")
# else:
#     print("Invalid triangle")



#exercise 10

# n= int(input("enter a number: "))
# for i in range (1,11):
#     #print(f"{n} * {i} = {n*i}")  
#     print(str(n) + " * " + str(i) + " = " + str(n * i))




#exercise 11
total=0
# n=int(input("enter a number"))
# for i in range(1,n+1):
#     total=total+i
#     print(total)
# print(total)



#exercise 12



# n = int(input("Enter a number: "))

# total = 0

# while n > 0:
#     digit = n % 10
#     total = total + digit
#     n = n // 10

# print("Sum:", total)


#exercise 13
# n=int(input("Enter a number: "))
# while n>=1:
#     print(n)
#     n=n-1
# print(n)




# exercise 14
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()


#exercise 15

# text=input("enter words:")
# count=0
# for i in text:
#     if i.lower() in "aeiou":
#         count= count+1
# print("number of vowels",count)



#exercise 16


# for i in range(1, 51):

#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


#exercise 17

# n = int(input("Enter number: "))

# n = 0

# while n > 0:
#     digit = n % 10
#     n = n * 10 + digit
#     n = n // 10

# print("Reversed_string:", n)




# exercise 18

n=int(input("number"))
original =n
reverse=0
while n>0:
    digit =n%10
    reverse=reverse*10+digit
    n=n//10
if original==reverse:
    print("palaindrome")
else:
    print("not palaindrome")







































