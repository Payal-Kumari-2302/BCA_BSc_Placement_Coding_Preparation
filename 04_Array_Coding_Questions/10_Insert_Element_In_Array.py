# Q10 - Insert an Element in an Array

# Problem:
# Insert an element at a specified position in an array.


# Solution:

arr = [10, 20, 30, 40]

element = int(input("Enter element: "))
position = int(input("Enter position: "))

arr.insert(position, element)

print("Updated Array:", arr)


# Output:
# Enter element: 25
# Enter position: 2
# Updated Array: [10, 20, 25, 30, 40]
