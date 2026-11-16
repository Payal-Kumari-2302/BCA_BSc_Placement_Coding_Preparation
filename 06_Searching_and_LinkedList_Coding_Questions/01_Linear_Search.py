# Q1 - Linear Search

# Problem:
# Search for a target element in an array.

# Solution:

arr = [10, 20, 30, 40, 50]

target = int(input("Enter target element: "))

found = False

for i in range(len(arr)):

    if arr[i] == target:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")


# Output:
# Enter target element: 30
# Element found at index: 2
