# Q1 - Two Sum

# Problem:
# Find two elements in an array whose sum equals the target.


# Solution:

arr = [2, 7, 11, 15]

target = int(input("Enter target: "))

found = False

for i in range(len(arr)):

    for j in range(i + 1, len(arr)):

        if arr[i] + arr[j] == target:
            print("Indices:", i, j)
            found = True
            break

    if found:
        break

if not found:
    print("No Pair Found")


# Output:
# Enter target: 9
# Indices: 0 1
