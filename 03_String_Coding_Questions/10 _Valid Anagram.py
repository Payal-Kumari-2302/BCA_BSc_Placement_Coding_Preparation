# ==========================================
# Problem Statement
# ==========================================

# Take two strings as input.
# Check whether both strings are anagrams or not.
# Two strings are anagrams if they contain
# the same characters with the same frequencies.


# ==========================================
# Solution
# ==========================================

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("Valid Anagram")
else:
    print("Not a Valid Anagram")


# ==========================================
# Output
# ==========================================

# Input:
# listen
# silent

# Output: Valid Anagram
