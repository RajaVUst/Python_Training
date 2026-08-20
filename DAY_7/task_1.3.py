sentences = ["the sky is blue", "python is fun", "list comprehensions are handy"]

# Flat list of all words longer than 2 characters across all sentences
long_words = [word for sentence in sentences for word in sentence.split() if len(word) > 2]

# Set of all unique words (case-insensitive)
unique_words = {word.lower() for sentence in sentences for word in sentence.split()}

print("Words longer than 2 chars:", long_words)
print("Unique words:", unique_words)

# Checkpoint: A nested comprehension becomes less readable when it has more than 2 loops
# or when conditions depend on the outer variable in a non-obvious way. Example:
#   matrix_flat = [cell for row in matrix for col in row for cell in col if cell > 0]
# That's three levels deep — a plain loop with a comment would be clearer there.
