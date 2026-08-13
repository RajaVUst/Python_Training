#Vowel counter
text = input("Enter a word or sentence: ")
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print(f"Number of vowels: {count}")