# Q22 - Find the Next Greater Element

# Problem:
# Find the first greater element on the right
# for each array element.


# Solution:

arr = [4, 5, 2, 10]

result = []

for i in range(len(arr)):

    next_greater = -1

    for j in range(i + 1, len(arr)):

        if arr[j] > arr[i]:
            next_greater = arr[j]
            break

    result.append(next_greater)

print("Next Greater Elements:", result)


# Output:
# Next Greater Elements: [5, 10, 10, -1]
