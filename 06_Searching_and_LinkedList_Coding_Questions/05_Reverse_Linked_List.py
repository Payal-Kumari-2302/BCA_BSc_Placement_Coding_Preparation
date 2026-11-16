# Q5 - Reverse a Linked List

# Problem:
# Reverse the direction of links in a Linked List.

# Solution:

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):

    prev = None
    current = head

    while current:

        next_node = current.next

        current.next = prev

        prev = current
        current = next_node

    return prev


def display(head):

    current = head

    while current:

        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Creating Linked List

head = Node(10)

head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Original Linked List:")
display(head)

head = reverse_linked_list(head)

print("Reversed Linked List:")
display(head)


# Output:
# Original Linked List:
# 10 -> 20 -> 30 -> 40 -> None
#
# Reversed Linked List:
# 40 -> 30 -> 20 -> 10 -> None
