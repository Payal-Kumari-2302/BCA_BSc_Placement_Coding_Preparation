# Q24 - Longest Continuous Increasing Subsequence

# Problem:
# Find the length of the longest continuous increasing subsequence.


# Solution:

arr = [1, 3, 5, 4, 7]

count = 1
maximum = 1

for i in range(1, len(arr)):

    if arr[i] > arr[i - 1]:
        count += 1

    else:
        count = 1

    maximum = max(maximum, count)

print("Longest Length:", maximum)


# Output:
# Longest Length: 3
