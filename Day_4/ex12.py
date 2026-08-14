def reset_score():
    score = 0  # Local variable

reset_score()

print(score)  # This will cause an error

# Error explanation:
# NameError: name 'score' is not defined
# This error occurs because 'score' is a local variable that exists
# only inside the reset_score() function. Once the function finishes,
# the variable is no longer accessible outside the function.
