# ==========================================
# Problem Statement
# ==========================================

# Take a word as input.
# Check whether capital letters are used correctly.
#
# Valid conditions:
# 1. All letters are uppercase.
# 2. All letters are lowercase.
# 3. Only the first letter is uppercase.
#
# Display the result.


# ==========================================
# Solution
# ==========================================

word = input("Enter a word: ")

if word.isupper() or word.islower() or word.istitle():
    print("Valid Capital Usage")

else:
    print("Invalid Capital Usage")


# ==========================================
# Output
# ==========================================

# Input: Google
# Output: Valid Capital Usage

# Input: FLaG
# Output: Invalid Capital Usage
