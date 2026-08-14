def grade_from_score(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

scores = [95, 82, 61, 40, 100]

for score in scores:
    print(f"Score: {score}, Grade: {grade_from_score(score)}")

#Output:
"""
Score: 95, Grade: A
Score: 82, Grade: B
Score: 61, Grade: D
Score: 40, Grade: F
Score: 100, Grade: A
"""