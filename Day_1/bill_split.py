bill = float(input('Enter the total bill amount: '))
people = int(input('No of people: '))
tip = input('do you want to add tip? (yes/no): ')
wants_tip =  tip == 'yes'
if wants_tip:
    bill = bill * 1.10
share = bill / people    
print(f'Each person pays: {share:.2f}')

