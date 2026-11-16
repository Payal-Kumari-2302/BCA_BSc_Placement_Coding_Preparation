# Q7 - Find Duplicate Elements

# Problem:
# Find all elements that appear more than once.


# Solution:

arr = [1, 2, 3, 2, 4, 1]

duplicates = []

for num in arr:

    if arr.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate Elements:", duplicates)


# Output:
# Duplicate Elements: [1, 2]
