# ==========================================
# Problem Statement
# ==========================================

# Take a string as input.
# Remove all characters except alphabets.
# Display the resulting string.


# ==========================================
# Solution
# ==========================================

text = input("Enter a string: ")

result = ""

for char in text:

    if char.isalpha():
        result += char

print("Result:", result)


# ==========================================
# Output
# ==========================================

# Input: Hello123@ World!

# Output: HelloWorld
