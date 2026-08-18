class InvalidScoreError(Exception):
    pass


def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100")

    return score


scores = [85, 105, 72, -10, 95]

for score in scores:
    try:
        print(validate_score(score))

    except InvalidScoreError as e:
        print(e)



#output:
'''85
Score must be between 0 and 100
72
Score must be between 0 and 100
95'''