# Q14 - Find the Third Maximum Number

# Problem:
# Find the third distinct maximum number.
# If it does not exist, return the maximum.


# Solution:

arr = [3, 2, 1]

unique = list(set(arr))

unique.sort(reverse=True)

if len(unique) >= 3:
    print("Third Maximum:", unique[2])

else:
    print("Maximum:", unique[0])


# Output:
# Third Maximum: 1
