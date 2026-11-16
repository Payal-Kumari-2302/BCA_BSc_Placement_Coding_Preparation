# ==========================================
# Problem Statement
# ==========================================

# Take a string as input.
# Remove consecutive duplicate characters.
# Keep only one character from each consecutive group.


# ==========================================
# Solution
# ==========================================

text = input("Enter a string: ")

result = ""

for char in text:

    if not result or result[-1] != char:
        result += char

print("Result:", result)


# ==========================================
# Output
# ==========================================

# Input: aabbccdaa
# Output: abcda
