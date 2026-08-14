def reset_score():
    score = 0
    print("Inside function, score =", score)

reset_score()


print(score)

# Why the error occurs:
# 'score' is a local variable defined inside reset_score().
# Local variables exist only within the function's scope and are destroyed
# once the function returns. Trying to access 'score' outside the function
# raises NameError: name 'score' is not defined, because it never existed
# in the global (module-level) scope.
