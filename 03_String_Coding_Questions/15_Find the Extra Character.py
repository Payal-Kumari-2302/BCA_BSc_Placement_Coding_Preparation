# ==========================================
# Problem Statement
# ==========================================

# Take two strings as input.
# The second string contains one extra character.
# Find and display the extra character.


# ==========================================
# Solution
# ==========================================

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = 0

for char in str1 + str2:
    result ^= ord(char)

print("Extra Character:", chr(result))


# ==========================================
# Output
# ==========================================

# Input:
# str1: abc
# str2: abcd

# Output: Extra Character: d
