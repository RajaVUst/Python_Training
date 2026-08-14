#single condition
age = 12
if age > 18:
    print("you can vote")
else:
    print('Not old enough')

# chaining with elif

mark = 50
if mark >= 90:
    print('Grade A')
elif mark >= 75:
    print('Grade B')
elif mark >= 60:
    print('Grade C')    
else:
    print("Grade D")

#combining coditions 

temperature = 33
is_raining = False
if temperature > 30 and not is_raining:
    print('Good day for walk')
else:
    print('stay in')

# loop

for i in range(1,6):
    print(f'iteration {i}')

# loop + condition 

for n in range(1,10):
    if(n % 2 == 0):
        print(f'{n} is even')    
    else:
        print(f'{n} is odd')