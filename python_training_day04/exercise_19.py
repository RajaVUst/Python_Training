def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1
    return count

text1 = "Python Bootcamp"
text2 = "Python is easy to learn"

print(f"{text1} -> {count_vowels(text1)}")
print(f"{text2} -> {count_vowels(text2)}")


#output:
'''Python Bootcamp -> 4
Python is easy to learn -> 7'''