# Q2 - Binary Search

# Problem:
# Search for a target element in a sorted array.

# Solution:

arr = [10, 20, 30, 40, 50]

target = int(input("Enter target element: "))

low = 0
high = len(arr) - 1

found = False

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == target:

        print("Element found at index:", mid)
        found = True
        break

    elif arr[mid] < target:

        low = mid + 1

    else:

        high = mid - 1

if not found:
    print("Element not found")


# Output:
# Enter target element: 40
# Element found at index: 3
