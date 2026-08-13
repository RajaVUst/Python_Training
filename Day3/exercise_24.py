secret_number = 7
guesses = [3, 10, 5, 7, 9]
for guess in guesses:
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct!")
        break