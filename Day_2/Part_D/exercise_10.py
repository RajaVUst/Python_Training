text = "the quick brown fox, jumps over the lazy dog"

brown_index = text.find("brown")
new_text = text.replace("brown", "red")

print(f"Original text: {text}")
print(f"Index of brown: {brown_index}")
print(f"New text: {new_text}")