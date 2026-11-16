# Q2 - Check Whether Array Is Sorted

# Problem:
# Check whether the given array is sorted in ascending order.


# Solution:

arr = [1, 2, 3, 4, 5]

is_sorted = True

for i in range(len(arr) - 1):

    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("Sorted")
else:
    print("Not Sorted")


# Output:
# Sorted
