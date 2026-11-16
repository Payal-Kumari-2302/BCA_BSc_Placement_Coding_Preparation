# Q6 - Count Frequency of Array Elements

# Problem:
# Count how many times each element appears in an array.


# Solution:

arr = [1, 2, 2, 3, 1, 1]

freq = {}

for num in arr:

    if num in freq:
        freq[num] += 1

    else:
        freq[num] = 1

for key, value in freq.items():
    print(key, ":", value)


# Output:
# 1 : 3
# 2 : 2
# 3 : 1
