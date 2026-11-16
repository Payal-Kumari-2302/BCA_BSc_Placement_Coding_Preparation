# Q16 - Find Non-Repeating Elements

# Problem:
# Find all elements that occur exactly once.


# Solution:

arr = [1, 2, 2, 3, 4, 4, 5]

result = []

for num in arr:

    if arr.count(num) == 1:
        result.append(num)

print("Non-Repeating Elements:", result)


# Output:
# Non-Repeating Elements: [1, 3, 5]
