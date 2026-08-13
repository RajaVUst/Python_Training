# 8: Simple grading system
score=int(input("Enter the socre: "))
if score>=90:
    print("A")
elif score>75 and score<89:
    print("B")
elif score>60 and score<74:
    print("C")
elif score>40 and score<59:
    print("D")
else:
    print("F")