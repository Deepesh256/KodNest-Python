original_scores = []

# Read three integer scores
for _ in range(3):
    original_scores.append(int(input()))

# Create alias
alias_scores = original_scores

# Read replacement and additional scores
replacement_score = int(input())
additional_score = int(input())

# Modify the shared list through alias_scores
alias_scores[0] = replacement_score
alias_scores.append(additional_score)

# Display both variables and check whether they share one object
print("Original:", original_scores)
print("Alias:", alias_scores)
print("Shared Object:", alias_scores is original_scores)
