score1=float(input("enter the test score1"))
score2=float(input("enter the test score2"))
score3=float(input("enter the test score3"))

avg_score=(score1+score2+score3)/3


if avg_score>40:
    has_passed=True
else:
    has_passed=False

print(f"Average:{avg_score}|Passed:{has_passed}")
