class InvalidScoreError(Exception):
    pass

def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError(f"Score {score} is out of range (0–100).")
    return score

# Test
print(validate_score(85))   # valid
print(validate_score(110))  # raises InvalidScoreError
