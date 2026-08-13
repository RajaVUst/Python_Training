word = input("Enter any sentence :")

count = 0

for ch in word :
    if ch.lower() in "aeiou":
        count += 1

print(f"vowel count : {count}")

