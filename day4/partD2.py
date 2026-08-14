def reset_score():
    score=0
    print(f"Inside reset_score:{score}")

reset_score()
print(score)

#score variable is local to reset_score function it cannot be accessed from outside that funciton