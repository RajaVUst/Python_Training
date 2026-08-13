#Exercise 24 — Number guessing game
secret_number = 42
guesses = [10, 25, 50, 42, 60]

for guess in guesses:
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")
        break

#Exercise 25 — Pyramid of numbers
n = 5

for row in range(1, n + 1):
    for num in range(1, row + 1):
        print(num, end=" ")
    print()

