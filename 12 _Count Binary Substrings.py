# ==========================================
# Problem Statement
# ==========================================

# Take a binary string as input.
# Count substrings containing equal consecutive
# 0s and 1s, where all 0s and 1s are grouped together.
# Display the total number of valid substrings.


# ==========================================
# Solution
# ==========================================

binary = input("Enter a binary string: ")

groups = []
count = 1

for i in range(1, len(binary)):

    if binary[i] == binary[i - 1]:
        count += 1
    else:
        groups.append(count)
        count = 1

if binary:
    groups.append(count)

result = 0

for i in range(1, len(groups)):
    result += min(groups[i - 1], groups[i])

print("Count:", result)


# ==========================================
# Output
# ==========================================

# Input: 00110011
# Output: 6
