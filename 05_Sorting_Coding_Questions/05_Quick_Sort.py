# Q5 - Quick Sort

# Problem:
# Sort an array using a pivot element.

# Solution:

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for num in arr[:-1]:

        if num <= pivot:
            left.append(num)

        else:
            right.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [10, 7, 8, 9, 1, 5]

print("Sorted Array:", quick_sort(arr))


# Output:
# Sorted Array: [1, 5, 7, 8, 9, 10]
