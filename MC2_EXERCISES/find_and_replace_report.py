text = "the quick brown fox"
index = text.find("brown")
new_text = text.replace("brown","red")
print(f"original text: {text}")
print(f"Index is at: {index}")
print(f"new text: {new_text}")

"""
Output ->
original text: the quick brown fox
Index is at: 10
new text: the quick red fox
"""