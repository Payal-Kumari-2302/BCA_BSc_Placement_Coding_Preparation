# Q18 - Right Rotate Array by K Positions

# Problem:
# Rotate the elements of an array to the right by K positions.


# Solution:

arr = [1, 2, 3, 4, 5]

k = int(input("Enter K: "))

k = k % len(arr)

result = arr[-k:] + arr[:-k] if k != 0 else arr[:]

print("Rotated Array:", result)


# Output:
# Enter K: 2
# Rotated Array: [4, 5, 1, 2, 3]
