def reset_score():
    score = 0
    print("Inside function:", score)

reset_score()

print("Outside function:", score)


#output:
'''Inside function: 0
NameError: name 'score' is not defined'''