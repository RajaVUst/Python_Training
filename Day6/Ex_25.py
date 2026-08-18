class InvalidScoreError(Exception):
    pass
 
def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100.")
    return score
 
scores = [90, -5, 75, 120, 100]
 
for score in scores:
    try:
        print("Valid score:", validate_score(score))
    except InvalidScoreError as e:
        print(f"Invalid score ({score}):", e)
 
# Output:
# Valid score: 90
# Invalid score (-5): Score must be between 0 and 100.
# Valid score: 75
# Invalid score (120): Score must be between 0 and 100.
# Valid score: 100
 