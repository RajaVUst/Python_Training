score1 = float(input("Enter first score: "))
score2 = float(input("Enter second score: "))
score3 = float(input("Enter third score: "))
average = (score1 + score2 + score3) / 3
has_passed = (average >= 40)
print(f"Average: {average:.1f} | Passed: {has_passed}")