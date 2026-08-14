# Grade from score

def grade_from_score(score):

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores = [95, 82, 70, 61, 40, 100]
for score in scores:
    grade = grade_from_score(score)
    print(f"{score} -> {grade}")


# Output:
# 95 -> A
# 82 -> B
# 70 -> C
# 61 -> D
# 40 -> F
# 100 -> A