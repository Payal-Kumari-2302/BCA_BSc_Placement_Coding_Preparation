# Q26 - Count Array Inversions

# Problem:
# Count pairs (i, j) where i < j and arr[i] > arr[j].


# Solution:

arr = [2, 4, 1, 3, 5]

count = 0

for i in range(len(arr)):

    for j in range(i + 1, len(arr)):

        if arr[i] > arr[j]:
            count += 1

print("Inversions:", count)


# Output:
# Inversions: 3
