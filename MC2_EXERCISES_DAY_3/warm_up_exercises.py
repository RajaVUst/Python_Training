# Exercise 1: Type & operator refresher 
whole_number = 100
decimal_number = 100.10
text = "Hello World"

print(f"{decimal_number} is of type {type(decimal_number)}")
print(f"{whole_number} is of type {type(whole_number)}")
print(f"{text} is of type {type(text)}")

quotient = whole_number/decimal_number
print(f"{whole_number} divided by {decimal_number} is {quotient}")

"""
Output ->
100.1 is of type <class 'float'>
100 is of type <class 'int'>
Hello World is of type <class 'str'>
100 divided by 100.1 is 0.999000999000999
"""

# Exercise 2: String slicing refresher 

text = "Python Readiness Training" 

print(text[0:6])
print(text[::-1])

"""
Output ->
Python
gniniarT ssenidaeR nohtyP
"""
# Exercise 3: Comparison practice 

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a <= b) 

"""
Output ->
False
True
False
True
"""

