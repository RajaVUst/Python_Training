secret_number = 8
guesses = [3, 12, 6, 8,]

for guess in guesses:
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")
        break