#Find and Replace Report
text = "the quick brown fox"
idx = text.find("brown")
new_text = text.replace("brown", "red")
print(f"Original: {text}")
print(f"Index found: {idx}")        
print(f"New text: {new_text}")     