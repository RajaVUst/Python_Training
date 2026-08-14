# Count vowels

def count_vowels(text):
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count = count + 1

    return count

print(count_vowels("India lift the world cup"))
print(count_vowels("Hello World"))

# Output:
#7
#3