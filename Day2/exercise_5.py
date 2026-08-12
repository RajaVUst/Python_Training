title = "  My First   Python Project!!  "
clean = title.strip()
clean = clean.replace("!!", "")
clean = clean.lower()
clean = clean.replace(" ", "_")
print(clean)