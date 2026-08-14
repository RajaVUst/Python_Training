score = int(input('enter your score: '))
if score >= 90:
    print('your grade is A')
elif score >= 75 and score <= 89:
    print('your grade is B')
elif score >= 60 and score <= 74:
    print('your grade is C')
else:
    print('your grade is D')