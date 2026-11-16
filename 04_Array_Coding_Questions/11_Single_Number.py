# Q11 - Find the Single Number

# Problem:
# Find the element that appears only once
# when every other element appears twice.


# Solution:

arr = [4, 1, 2, 1, 2]

result = 0

for num in arr:
    result = result ^ num

print("Single Number:", result)


# Output:
# Single Number: 4
