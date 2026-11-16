# ==========================================
# Problem Statement
# ==========================================

# Take a string as input.
# Count how many times each character appears.
# Display the frequency of each character.


# ==========================================
# Solution
# ==========================================

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char, count in frequency.items():
    print(char, ":", count)


# ==========================================
# Output
# ==========================================

# Input: apple

# Output:
# a : 1
# p : 2
# l : 1
# e : 1
