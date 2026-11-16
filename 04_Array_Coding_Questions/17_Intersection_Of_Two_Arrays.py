# Q17 - Intersection of Two Arrays

# Problem:
# Find the common distinct elements between two arrays.


# Solution:

arr1 = [1, 2, 2, 3]
arr2 = [2, 2, 4]

result = []

for num in arr1:

    if num in arr2 and num not in result:
        result.append(num)

print("Intersection:", result)


# Output:
# Intersection: [2]
