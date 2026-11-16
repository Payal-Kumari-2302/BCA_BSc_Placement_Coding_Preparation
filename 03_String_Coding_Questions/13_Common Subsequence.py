# ==========================================
# Problem Statement
# ==========================================

# Take two strings as input.
# Find the Longest Common Subsequence (LCS).
# A subsequence maintains character order
# but does not need to be continuous.
# Display the longest common subsequence and its length.


# ==========================================
# Solution
# ==========================================

str1 = input("Enter first string:")
str2 = input("Enter second string:")

m = len(str1)
n = len(str2)

dp = [["" for j in range(n + 1)] for i in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):

        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]

        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

result = dp[m][n]

print("Longest Common Subsequence:", result)
print("Length:", len(result))


# ==========================================
# Output
# ==========================================

# Input:
# Enter first string: ABCDGH
# Enter second string: AEDFHR

# Output:
# Longest Common Subsequence: ADH
# Length: 3
