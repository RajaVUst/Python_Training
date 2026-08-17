grade_lookup={"A":90,"B":80,"C":65,"D":50,"F":35}
score=84
for grade,mark in grade_lookup.items():
    if score>=mark:
        print("Grade:",grade)
        break
#output
#Grade: B

