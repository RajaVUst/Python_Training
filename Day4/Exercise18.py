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
 
for s in [95, 82, 61, 40, 100]:
    print(f"{s} -> {grade_from_score(s)}")
    
# Output:
# 95 -> A
# 82 -> B
# 61 -> D
# 40 -> F
# 100 -> A