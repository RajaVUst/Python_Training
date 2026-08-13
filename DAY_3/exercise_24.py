secret_number = 42

guesses = [10, 55, 42, 30, 70]

for guess in guesses:
    if guess > secret_number:
        print(f"{guess}: Too high")
    elif guess < secret_number:
        print(f"{guess}: Too low")
    else:
        print(f"{guess}: Correct!")
        break
