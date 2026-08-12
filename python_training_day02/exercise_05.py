title = " My First Python Project!! "

clean = title.strip()
print(clean)

clean = clean.replace("!!", "")
print(clean)

clean = clean.lower()
print(clean)

slug = clean.replace(" ", "_")
print(slug)