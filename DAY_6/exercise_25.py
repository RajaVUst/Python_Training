class InvalidScoreError(Exception):
    pass

def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError(f"Score {score} is out of range (0–100).")
    return score

test_values = [85, 110, 0, -10, 99]

for value in test_values:
    try:
        result = validate_score(value)
        print(f"{value} -> valid")
    except InvalidScoreError as e:
        print(f"{value} -> Error: {e}")
