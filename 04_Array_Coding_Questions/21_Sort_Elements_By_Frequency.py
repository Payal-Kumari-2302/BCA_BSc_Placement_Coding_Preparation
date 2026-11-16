# Q21 - Sort Elements by Frequency

# Problem:
# Sort array elements according to their frequency.


# Solution:

arr = [4, 5, 6, 5, 4, 3, 4]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

result = sorted(arr, key=lambda x: -freq[x])

print("Sorted by Frequency:", result)


# Output:
# Sorted by Frequency: [4, 4, 4, 5, 5, 6, 3]
