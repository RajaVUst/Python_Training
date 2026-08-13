score=int(input("Enter your score: "))
if score>=90:
    print("Grade A")
elif score>=75 and score<90:
    print("Grade B")
elif score>=60 and score<75:
    print("Grade C")
elif score>=40 and score<60:
    print("Grade D")
else:
    print("Grade F")