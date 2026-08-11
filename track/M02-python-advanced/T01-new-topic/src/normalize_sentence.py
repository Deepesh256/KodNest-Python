# Read the sentence
sentence = input()

# Clean and normalize the sentence
cleaned = sentence.strip()
normalized = cleaned.lower().replace(".", "")

# Split the sentence and create the slug
words = normalized.split()
slug = "-".join(words)

# Convert to uppercase
uppercase = normalized.upper()

# Find the position of the word 'python'
position = normalized.find("python")

# Display all processed values
print("Cleaned:", cleaned)
print("Normalized:", normalized)
print("Words:", words)
print("Slug:", slug)
print("Uppercase:", uppercase)
print("Python Position:", position)
