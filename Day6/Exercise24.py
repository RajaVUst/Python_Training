
class InvalidScoreError(Exception):
    pass

def validate_score(score):
    if not (0 <= score <= 100):
        raise InvalidScoreError(f"{score} is not between 0 and 100")
    return score

#output
#It just define a custom exception
