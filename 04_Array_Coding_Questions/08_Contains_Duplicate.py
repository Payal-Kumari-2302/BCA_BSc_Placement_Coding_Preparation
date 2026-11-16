# Q8 - Check Whether Array Contains Duplicates

# Problem:
# Check whether an array contains duplicate elements.


# Solution:

arr = [1, 2, 3, 1]

if len(arr) != len(set(arr)):
    print("Duplicate Found")

else:
    print("No Duplicate")


# Output:
# Duplicate Found
