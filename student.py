sub1 = float(input('enter the score 1 :'))
sub2 = float(input('enter the score 2 :'))
sub3 = float(input('enter the score 3 :'))
avg = sub1 + sub2 + sub3 / 3
has_passed = avg >= 40
print(f'Average: {avg}| Passed: {has_passed}| ')
