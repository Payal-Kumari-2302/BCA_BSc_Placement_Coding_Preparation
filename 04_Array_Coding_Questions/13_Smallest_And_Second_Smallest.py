# Q13 - Smallest and Second Smallest

# Problem:
# Find the smallest and second smallest distinct elements.


# Solution:

arr = [12, 5, 8, 2, 10]

unique = list(set(arr))

unique.sort()

if len(unique) >= 2:

    print("Smallest:", unique[0])
    print("Second Smallest:", unique[1])

else:
    print("Second Smallest Not Found")


# Output:
# Smallest: 2
# Second Smallest: 5
