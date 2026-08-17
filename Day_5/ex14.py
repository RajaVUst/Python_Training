grade_lookup = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60,
    "F": 0
}

score = 84

for grade, threshold in grade_lookup.items():
    if score >= threshold:
        print(f"Score {score} receives grade {grade}")
        break

# Output:
# Score 84 receives grade B