
grade_lookup = {"A": 90, "B": 80, "C": 70, "D": 60, "F": 0}
score = 84
for letter, threshold in sorted(grade_lookup.items(), key=lambda x: -x[1]):
    if score >= threshold:
        print(f"Score {score} -> Grade {letter}")
        break
    
#output    
# Score 84 -> Grade B