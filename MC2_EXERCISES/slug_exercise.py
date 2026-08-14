sentence = "  My First   Python Project!!  "
slug = sentence.lower().replace(" ", "_").replace("!!"," ")
print(slug)

"""
Output ->
__my_first___python_project __
"""