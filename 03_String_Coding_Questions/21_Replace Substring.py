# ==========================================
# Problem Statement
# ==========================================

# Take a string, old substring and new substring.
# Replace all occurrences of the old substring
# with the new substring.
# Display the updated string.


# ==========================================
# Solution
# ==========================================

text = input("Enter a string: ")
old = input("Enter substring to replace: ")
new = input("Enter new substring: ")

result = text.replace(old, new)

print("Updated String:", result)


# ==========================================
# Output
# ==========================================

# Input:
# text: I like Java
# old: Java
# new: Python

# Output: I like Python
