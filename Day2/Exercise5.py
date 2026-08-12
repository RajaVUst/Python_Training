#Slug Normalizer
title = "  My First   Python Project!!  "
slug = title.strip().replace("!!", "").lower().replace(" ", "_")
print(slug)  