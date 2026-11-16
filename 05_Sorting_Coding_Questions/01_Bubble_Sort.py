# Q1 - Bubble Sort

# Problem:
# Sort an array in ascending order using Bubble Sort.

# Solution:

arr = [5, 3, 8, 4, 2]

n = len(arr)

for i in range(n):
    for j in range(n - i - 1):

        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:", arr)


# Output:
# Sorted Array: [2, 3, 4, 5, 8]
