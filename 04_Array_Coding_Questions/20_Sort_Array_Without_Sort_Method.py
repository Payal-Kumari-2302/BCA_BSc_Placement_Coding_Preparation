# Q20 - Sort Without Built-in Sort Method

# Problem:
# Sort array elements without using built-in sorting methods.


# Solution:

arr = [5, 3, 1, 4, 2]

n = len(arr)

for i in range(n):

    for j in range(n - i - 1):

        if arr[j] > arr[j + 1]:

            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:", arr)


# Output:
# Sorted Array: [1, 2, 3, 4, 5]
