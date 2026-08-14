def reset_score():
    score = 0
    print(score)
reset_score()
print(score)
 
# output:
# 0
# Getting NameError: name 'score' is not defined because the variable score is local to the function reset_score and cannot be accessed outside of it.