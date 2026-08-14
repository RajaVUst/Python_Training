score=int(input("enter the score:"))
if score>=90:
    print(f"{score} is A+")
elif score>=75 and score<=89:
    print(f"{score} is B")
elif score>=60 and score<=74:
    print(f"{score} is C")
elif score>=40 and score<=59:
    print(f"{score} is D")
else:
    print(f"{score} is F")