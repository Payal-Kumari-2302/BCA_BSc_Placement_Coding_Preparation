# ==========================================
# Problem Statement
# ==========================================

# Take a string as input.
# Count the number of substrings
# that contain only unique characters.
# Display the total count.


# ==========================================
# Solution
# ==========================================

text = input("Enter a string: ")

result = 0

for i in range(len(text)):
    seen = set()

    for j in range(i, len(text)):

        if text[j] in seen:
            break

        seen.add(text[j])
        result += 1

print("Count:", result)


# ==========================================
# Output
# ==========================================

# Input: abc

# Output: Count: 6
