def reset_score():
    score = 0
    print(score)

reset_score()
print(score)

# NameError: name 'score' is not defined
# score is local to reset_score
# It cannot be accessed outside the function