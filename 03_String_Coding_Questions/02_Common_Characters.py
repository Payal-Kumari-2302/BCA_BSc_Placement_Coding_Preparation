# ==========================================
# Problem Statement
# ==========================================

# Take two strings as input.
# Find the common characters present in both strings.
# Display each common character only once.


# ==========================================
# Solution
# ==========================================

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

common = set(str1) & set(str2)

print("Common Characters:", sorted(common))


# ==========================================
# Output
# ==========================================

# Input:
# hello
# world

# Output: ['l', 'o']
