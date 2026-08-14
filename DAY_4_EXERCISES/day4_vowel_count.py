def vowel_counter(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

print(vowel_counter("Python Bootcamp")) 
print(vowel_counter("PYTHON BOOTCAMP")) 

"""
Output -> 
4
4
"""