def reset_score():
    score = 0
    print(score)
reset_score()
print(score) 

"""
output
0
Traceback (most recent call last):
  File "c:\Users\308332\Desktop\Python_Training\Day4\task_12.py", line 5, in <module>
    print(score)  # score is local to the function
          ^^^^^
NameError: name 'score' is not defined
"""
