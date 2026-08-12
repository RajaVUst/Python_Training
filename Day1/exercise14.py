# Exercise 14 - Student Report Line
score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
score3 = float(input("Enter Score 3: "))
average = (score1 + score2 + score3) / 3
has_passed = average >= 40

print(f"Average: {average:.1f} | Passed: {has_passed}")