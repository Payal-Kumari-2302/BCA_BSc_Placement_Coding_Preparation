# ==========================================
# Problem Statement
# ==========================================

# Take a text and a pattern as input.
# Check whether the pattern matches the text.
#
# '?' matches exactly one character.
# '*' matches zero or more characters.
#
# Display whether the pattern matches.


# ==========================================
# Solution
# ==========================================

text = input("Enter text: ")
pattern = input("Enter pattern: ")

m = len(text)
n = len(pattern)

dp = [[False] * (n + 1) for _ in range(m + 1)]

dp[0][0] = True

for j in range(1, n + 1):

    if pattern[j - 1] == '*':
        dp[0][j] = dp[0][j - 1]

for i in range(1, m + 1):
    for j in range(1, n + 1):

        if pattern[j - 1] == '*':
            dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        elif pattern[j - 1] == '?' or text[i - 1] == pattern[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]

if dp[m][n]:
    print("Pattern Matches")

else:
    print("Pattern Does Not Match")


# ==========================================
# Output
# ==========================================

# Input:
# text: abcde
# pattern: a*e

# Output: Pattern Matches
