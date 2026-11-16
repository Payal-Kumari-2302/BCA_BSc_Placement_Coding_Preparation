# Q3 - Detect Loop in a Linked List

# Problem:
# Check whether a Linked List contains a loop.

# Solution:

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def detect_loop(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Creating Linked List

head = Node(10)

head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

# Creating Loop
head.next.next.next.next.next = head.next.next

if detect_loop(head):
    print("Loop Detected")
else:
    print("No Loop")


# Output:
# Loop Detected
