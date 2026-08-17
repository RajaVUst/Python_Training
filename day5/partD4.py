minimum_grade={
     "A": 90,
    "B": 80,
    "C": 70,
    "D": 60,
    "F": 0
}

for grade,minimum in minimum_grade.items():
    if 87>minimum:
        print(f"Grade:{grade},87")
        break

# OUTPUT
# Grade:B,87