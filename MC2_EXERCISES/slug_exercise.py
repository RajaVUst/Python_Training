sentence = "  My First   Python Project!!  "
slug = sentence.lower().replace(" ", "_").replace("!!"," ")
print(slug)