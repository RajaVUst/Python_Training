score1 = float(input("Enter first test score: "))
score2 = float(input("Enter second test score: "))
score3 = float(input("Enter third test score: "))

average = (score1 + score2 + score3) / 3
has_passed = average >= 40

print(f"Average: {average:.1f} | Passed: {has_passed}")

"""
Output ->
Enter first test score: 70
Enter second test score: 50
Enter third test score: 89
Average: 69.7 | Passed: True
"""