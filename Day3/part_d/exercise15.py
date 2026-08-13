# Exercise 15 - Vowel Counter
text = "Python Readiness Training"
vowel_count = 0
for ch in text:
    if ch.lower() in "aeiou":
        vowel_count += 1

print(f"Number of vowels: {vowel_count}")