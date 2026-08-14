def reset_score():
    score = 0
    print("Inside function:", score)

reset_score()

# print(score) # NameError

'''
score is a local variable of the function reset_score().
When you try to access it outside, it will cause
NameError: name 'score' is not defined
'''