#PART A
#2
# def sqaure_number(n):
#     return n* n
# number=int(input("enetr the number:"))
# result=sqaure_number(number)
# print(result)    

#PART-B
#4
# def mul(a,b):
#     return a*b
# a,b=map(int,input("Enter a and b values:").split())
# result=mul(a,b)
# print(result)

#5
# def is_even_print(n):
#     if n%2==0:
#         print(f"{n} is the even number")
#     else:
#         print(f"{n} is the odd number") 
# n=int(input("Enter the number:"))
# result=is_even_print(n)


# def is_even_return(n):
#     if n% 2==0:
#         return True
#     else:
#         return False
# n=int(input("Enter the input:"))
# result=is_even_return(n)
# print(result)            


#6
# def celsius_to_fahrenheit(cel):
#     return cel * 9 / 5 + 32

# print(f"celsius_to_fahrenheit(0) -> {celsius_to_fahrenheit(0)}")   
# print(f"celsius_to_fahrenheit(0) -> {celsius_to_fahrenheit(37)}")   
# print(f"celsius_to_fahrenheit(0) -> {celsius_to_fahrenheit(100)}")   


#PART C
#7
# def order_summary(item, quantity=1):
#     return f"Item:{item}, Quantity:{quantity}"
# result=order_summary("book")
# print(result)    

# result=order_summary("book",5)
# print(result)    


# #8
# def  book_ticket(passenger, seat_type="Economy", meal="Veg") :
#     return f" Passenger:{passenger},  Seat Type:{seat_type},  Meal: {meal}"
# result=book_ticket(passenger="surendra")
# print(result)
# result=book_ticket(passenger="surendra",meal="Nonveg")
# print(result)
# result=book_ticket(passenger="surendra", seat_type="Normal", meal="Non veg")
# print(result)



#9

# def total_cost(*prices):
#     total =0
#     for price in prices:
#         total+=price
#     return total

# print(total_cost(1,2,6,7,5,5,5,5,))    


#10

# def print_student_info(**details):
#     for key, value in details.items():
#         print(f"{key}:{value}")

# print_student_info(name="surendra", age=23,course="pyhton", city="hyd")


#11
# def add(a,b):
#     """addition of two number"""
#     return a+b

# def mul(a,b):
#     """product of two numbers"""
#     return a*b    
# print(add(20,20))
# print(add.__doc__)    


# print(mul(10,78))
# print(mul.__doc__)


# help(add)
# help(mul)


#12
# def reset_score():
#     score=0
#     print(score)
# reset_score()

# print(score)    


#13
# total_attempts=0
# def log_attempt():
#     global total_attempts
#     total_attempts+=1
#     return total_attempts

# print(log_attempt())    
# print(log_attempt())  
# print(log_attempt())  
# print(log_attempt())  


# print(f"Total final attempts:{total_attempts}")


#14
# cube=lambda n:n*n*n
# n=int(input("enter the number"))
# print(cube(n))


#15
# def countdown(n):
#     if n==0:
#         print("Liftoff")
#     else:
#         print(n)
#         countdown(n-1)    
# countdown(10)      

#16
# def re_sum(n):
#     add=0
#     for i in range(1,n):
#         add=add+i
#     print(add)

# re_sum(13)      



#17

# def is_palindrome(word):
#     word=word.lower()
#     if word==word[::-1]:
#         return True
#     else:
#         return False
# print(is_palindrome("level"))
# print(is_palindrome("python"))
# print(is_palindrome("Madam"))



#18
# def grade(score):
#     if score>=90:
#         return "A"
#     elif score>=80:
#         return "B"
#     elif score>=70:
#         return "c"
#     elif score>=60:
#         return "d" 
#     else:
#         return "FAil"               
# scores=list(map(int,input("ENter the scores").split()))
# for num in scores:
#     result=grade(num) 
#     print(f"{num}->{result}", end=" ") 



#19
# def count_vowels(word):
#     count=0
#     vowel='aeiou'
#     vowel=vowel.lower()
#     for w in word:
#         if w in vowel:
#             count+=1
#     return count   
# word=input("Enter the sentence")
# print(count_vowels(word))


#20
# def fizzbuz_range(start, end):
#     for i in range(start, end+1):
#         if i%3==0 and i %5==0:
#             print("FIzzBuzz")
#         elif i%3==0:
#             print("FIZZ")
#         elif   i%5==0:
#             print("Buzz")
#         else:
#             print(f"{i}  is not divisble wiith 3 or 5")
# start, end=map(int,input().split())
# fizzbuz_range(start, end)                  


# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True


# def prme_limit(limit):
#     primes=[]
#     non_primes=[]
#     for num in range(2, limit+1):
#         if is_prime(num):
#             primes.append(num)
#     return primes      
   

# print(prme_limit(30))


# def is_password(password):
#     digit=False
#     upper=False
#     for ch in password:
#         if ch.isdigit():
#             digit= True

#         if ch.isupper():
#             upper=True

#     if len(password)<6:
#         return "weak"
#     elif digit and upper and len(password)>8:
#         return "strong"
#     else:
#         return "medium"        
# print(is_password("123"))    
# print(is_password("123iytirytU"))    
# print(is_password("123jgkjk"))                   

# def build_utilities(operation, *values):
#     if operation=="sum":
#         return sum(values)
#     elif operation=="max":
#         return max(values)
#     elif operation=="min":
#         return min(values)
#     elif operation=="average":
#         return sum(values)/len(values)
#     else:
#         return "Invalid operation"
# result=build_utilities("sum",1, 2,3)        
# print(f"Build_utilites:->{result}")                        