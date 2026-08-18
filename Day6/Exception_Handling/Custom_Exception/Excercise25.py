#Catch your custom exception
def validate_score(score):

    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    return score


scores = [80, 95, 120, 60, -10]
for score in scores:
    try:
        validate_score(score)
        print(score, "is valid")

    except ValueError:
        print(score, "is invalid")

# Output:
# 80 is valid
# 95 is valid
# 120 is invalid
# 60 is valid
# -10 is invalid