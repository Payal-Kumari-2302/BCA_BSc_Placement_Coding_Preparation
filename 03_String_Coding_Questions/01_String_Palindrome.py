# ==========================================
# Problem Statement
# ==========================================

# Take a string as input.
# Check whether the string is a palindrome or not.
# A palindrome reads the same forward and backward.


# ==========================================
# Solution
# ==========================================

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# ==========================================
# Output
# ==========================================

# Input: madam
# Output: Palindrome

# Input: hello
# Output: Not Palindrome
