class InvalidScoreError(Exception):
    pass
 
def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100.")
    return score
 
try:
    print(validate_score(85))
    print(validate_score(120))
except InvalidScoreError as e:
    print(e)
 
# Output:
# 85
# Score must be between 0 and 100.
 