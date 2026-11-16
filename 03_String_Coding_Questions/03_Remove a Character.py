# ==========================================
# Problem Statement
# ==========================================

# Take a string and a character as input.
# Remove all occurrences of the given character.
# Display the updated string.


# ==========================================
# Solution
# ==========================================

text = input("Enter a string: ")
char = input("Enter character to remove: ")

result = text.replace(char, "")

print("Result:", result)


# ==========================================
# Output
# ==========================================

# Input:
# banana
# a

# Output: bnn
