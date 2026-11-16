# ==========================================
# Problem Statement
# ==========================================

# Take two strings as input.
# Check whether the second string
# is present inside the first string.
# Display the result.


# ==========================================
# Solution
# ==========================================

text = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in text:
    print("Substring Found")

else:
    print("Substring Not Found")


# ==========================================
# Output
# ==========================================

# Input:
# Main string: programming
# Substring: gram

# Output: Substring Found
