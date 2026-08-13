# input score from user
score = int(input("Enter score: "))

# ranking into grades based on score
if score >= 90:
    print("A")
elif score >= 75 and score < 90:
    print("B")
elif score >= 60 and score < 75:
    print("C")
elif score >= 40 and score < 60:
    print("D")
else:
    print("F")