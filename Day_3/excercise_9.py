a = int(input('Enter 1st side length: '))
b = int(input('Enter 2nd side length: '))
c = int(input('Enter 3rd side length: '))

if a + b > c and a + c > b and b + c > a:
    print('Valid Triangle')
else:
    print('Not valid Triangle')    