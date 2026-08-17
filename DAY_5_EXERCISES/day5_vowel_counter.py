def counter(text):
    counter_dict = {v: 0 for v in "aeiou"}

    for ch in text.lower():
        if ch in "aeiou":
            counter_dict[ch] += 1

    return counter_dict

result = counter("Helloworld")
print(result)

"""
Output->
{'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}
"""