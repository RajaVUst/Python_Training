grade_lookup = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60,
    "F": 0
}

score = 84

for grade, minimum_score in grade_lookup.items():
    if score >= minimum_score:
        print(f"Score {score} has grade {grade}.")
        break

    '''
    output
    Score 84 has grade B.
    '''