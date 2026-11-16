# Q2 - Selection Sort

# Problem:
# Sort an array by repeatedly finding the smallest element.

# Solution:

arr = [64, 25, 12, 22, 11]

n = len(arr)

for i in range(n):

    min_index = i

    for j in range(i + 1, n):

        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted Array:", arr)


# Output:
# Sorted Array: [11, 12, 22, 25, 64]
