# Q4 - Find Middle of a Linked List

# Problem:
# Find the middle node of a Linked List.

# Solution:

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

    if slow:
        return slow.data

    return None


# Creating Linked List

head = Node(10)

head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print("Middle Element:", find_middle(head))


# Output:
# Middle Element: 30
