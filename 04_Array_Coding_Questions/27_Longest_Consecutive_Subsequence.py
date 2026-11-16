# Q27 - Longest Consecutive Subsequence

# Problem:
# Find the length of the longest sequence
# of consecutive numbers in an array.


# Solution:

arr = [100, 4, 200, 1, 3, 2]

num_set = set(arr)

maximum = 0

for num in num_set:

    if num - 1 not in num_set:

        count = 1

        while num + count in num_set:
            count += 1

        maximum = max(maximum, count)

print("Longest Consecutive Length:", maximum)


# Output:
# Longest Consecutive Length: 4
