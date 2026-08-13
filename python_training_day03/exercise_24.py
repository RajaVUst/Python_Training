secret_number = 7

guesses = [3, 10, 5, 7, 9]

for guess in guesses:
    if guess > secret_number:
        print(guess, "Too high")
    elif guess < secret_number:
        print(guess, "Too low")
    else:
        print(guess, "Correct!")
        break