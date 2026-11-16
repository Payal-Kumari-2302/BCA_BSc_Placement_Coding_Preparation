# ==========================================
# Problem Statement
# ==========================================

# Take two sentences as input.
# Find words that appear exactly once
# in both sentences combined.
# Display the uncommon words.


# ==========================================
# Solution
# ==========================================

str1 = input("Enter first sentence: ")
str2 = input("Enter second sentence: ")

words1 = str1.split()
words2 = str2.split()

all_words = words1 + words2

result = []

for word in all_words:

    if all_words.count(word) == 1:
        result.append(word)

print("Uncommon Words:", result)


# ==========================================
# Output
# ==========================================

# Input:
# apple mango banana
# mango orange banana

# Output: ['apple', 'orange']
