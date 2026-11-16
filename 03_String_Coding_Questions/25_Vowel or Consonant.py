# ==========================================
# Problem Statement
# ==========================================

# Take a character as input.
# Check whether the character is a vowel or consonant.
# Display the result.
# If the input is not an alphabet, display Invalid Input.


# ==========================================
# Solution
# ==========================================

char = input("Enter a character: ")

if len(char) != 1 or not char.isalpha():
    print("Invalid Input")

elif char.lower() in "aeiou":
    print("Vowel")

else:
    print("Consonant")


# ==========================================
# Output
# ==========================================

# Input: a
# Output: Vowel

# Input: b
# Output: Consonant

# Input: 5
# Output: Invalid Input
