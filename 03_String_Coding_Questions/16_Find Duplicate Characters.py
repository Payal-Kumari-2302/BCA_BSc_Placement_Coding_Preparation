# ==========================================
# Problem Statement
# ==========================================

# Take a string as input.
# Find all characters that appear more than once.
# Display each duplicate character only once.


# ==========================================
# Solution
# ==========================================

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Duplicate Characters:")

for char, count in frequency.items():

    if count > 1:
        print(char, ":", count)


# ==========================================
# Output
# ==========================================

# Input: programming

# Output:
# Duplicate Characters:
# r : 2
# g : 2
# m : 2
