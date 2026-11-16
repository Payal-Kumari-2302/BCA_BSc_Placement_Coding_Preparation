# Q23 - Find a Peak Element

# Problem:
# Find an element greater than its neighbouring elements.


# Solution:

arr = [1, 3, 20, 4, 1]

for i in range(len(arr)):

    left = (i == 0 or arr[i] > arr[i - 1])

    right = (i == len(arr) - 1 or arr[i] > arr[i + 1])

    if left and right:
        print("Peak Element:", arr[i])
        break


# Output:
# Peak Element: 20
