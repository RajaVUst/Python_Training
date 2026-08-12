title = " My First Python Project!! "

slug = title.strip()
slug = slug.replace("!!", "")
slug = slug.lower()
slug = slug.replace(" ", "_")

print(slug)