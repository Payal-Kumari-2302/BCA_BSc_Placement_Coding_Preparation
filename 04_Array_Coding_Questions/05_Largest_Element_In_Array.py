# Q5 - Largest Element in an Array

# Problem:
# Find the largest element in an array.


# Solution:

arr = [10, 45, 23, 89, 12]

largest = arr[0]

for num in arr:

    if num > largest:
        largest = num

print("Largest Element:", largest)


# Output:
# Largest Element: 89
