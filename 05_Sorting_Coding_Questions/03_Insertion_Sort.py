# Q3 - Insertion Sort

# Problem:
# Sort an array by inserting elements into their correct positions.

# Solution:

arr = [12, 11, 13, 5, 6]

for i in range(1, len(arr)):

    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:

        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print("Sorted Array:", arr)


# Output:
# Sorted Array: [5, 6, 11, 12, 13]
