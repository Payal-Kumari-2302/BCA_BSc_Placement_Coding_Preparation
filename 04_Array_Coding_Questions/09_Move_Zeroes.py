# Q9 - Move Zeroes to the End

# Problem:
# Move all zeroes to the end while maintaining
# the order of non-zero elements.


# Solution:

arr = [0, 1, 0, 3, 12]

result = []

for num in arr:

    if num != 0:
        result.append(num)

zero_count = arr.count(0)

result.extend([0] * zero_count)

print("Result:", result)


# Output:
# Result: [1, 3, 12, 0, 0]
