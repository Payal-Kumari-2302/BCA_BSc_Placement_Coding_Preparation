# Q15 - Find the Majority Element

# Problem:
# Find the element that appears more than half
# the size of the array.


# Solution:

arr = [2, 2, 1, 1, 2, 2, 2]

n = len(arr)

for num in arr:

    if arr.count(num) > n // 2:
        print("Majority Element:", num)
        break

else:
    print("No Majority Element")


# Output:
# Majority Element: 2
