secret_number = 7
guesses = [2, 5, 9, 7, 10]

for guess in guesses:
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")
        break