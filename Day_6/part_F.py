# Exercise 23: Raise a built-in exception 

def  check_age(age):
    if age < 0 :
        raise ValueError(f'age cannot be in negative')
    return age
try:
    print('valid age:', check_age(25))
except ValueError as e:
    print('error', e)    

try:
    print('invalid age:', check_age(-8))
except ValueError as e:
    print('error',e)

# output 

# valid age: 25
# error age cannot be in negative

# Exercise 24: Define a custom exception 

class InvalidScoreError(Exception): pass

def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError('score must be between o and 100')
    return score
try:
    print('valid score:', validate_score(25))
except InvalidScoreError as e:
    print('error', e) 
try:
    print('valid score:', validate_score(-4))
except InvalidScoreError as e:
    print('error', e) 

# Output 
# valid score: 25
# error score must be between o and 100

test_scores = [85, -10, 100, 120, 50]

for score in test_scores:
    try:
        valid_score = validate_score(score)
        print(f"Valid score: {valid_score}")
    except InvalidScoreError as e:
        print(f"Invalid score {score}: {e}")

