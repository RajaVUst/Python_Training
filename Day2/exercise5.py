# Exercise 5 - Slug Normalizer
title = " My First Python Project!! "

clean_title = title.strip()
clean_title = clean_title.replace("!!", "")
clean_title = clean_title.lower()
slug = clean_title.replace(" ", "_")

print(f"Original Title: {title}")
print(f"Slug: {slug}")