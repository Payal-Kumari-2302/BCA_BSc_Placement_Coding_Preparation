# ==========================================
# Problem Statement
# ==========================================

# Take an Excel column name as input.
# Convert the column name into its corresponding number.
# Example: A = 1, B = 2, Z = 26, AA = 27.


# ==========================================
# Solution
# ==========================================

column = input("Enter Excel Column: ").upper()

result = 0

for char in column:
    result = result * 26 + (ord(char) - ord('A') + 1)

print("Column Number:", result)


# ==========================================
# Output
# ==========================================

# Input: AB
# Output: 28

# Input: AZ
# Output: 52
