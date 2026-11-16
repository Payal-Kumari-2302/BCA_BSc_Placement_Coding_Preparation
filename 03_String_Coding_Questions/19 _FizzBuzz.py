# ==========================================
# Problem Statement
# ==========================================

# Take a number n as input.
# Print numbers from 1 to n.
#
# If a number is divisible by 3, print Fizz.
# If divisible by 5, print Buzz.
# If divisible by both, print FizzBuzz.
# Otherwise, print the number itself.


# ==========================================
# Solution
# ==========================================

n = int(input("Enter a number: "))

for i in range(1, n + 1):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)


# ==========================================
# Output
# ==========================================

# Input: 15

# Output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
