title = "  My First   Python Project!!  "

title = title.strip()
print(f"After strip: {title}")

title = title.replace("!!", "")
print(f"After removing !!: {title}")

title = title.lower()
print(f"After lower: {title}")

title = title.replace(" ", "_")
print(f"Final slug: {title}")