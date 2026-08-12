a = 5 
b = 10
# temp stores the value in a which is 5
temp = a
# value of the a is now 10
a = b
# b takes the value in temp which is 5
b = temp
print(f'a = {a}, b = {b}')

a = 5
b = 10
# 
a, b = b, a
print(f'a = {a}, b = {b} ')
