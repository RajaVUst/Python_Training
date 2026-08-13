given_text="the quick brown fox"

index=given_text.find("brown")

replaced_text=given_text.replace("brown","red")
print(f"replaced_text:{replaced_text}")
print(f"the orginal text:{given_text},Starting Index of a brown:{index},Replaced:{replaced_text}")
