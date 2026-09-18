"""
1. Slow and Fast Pointer Technique

The Slow and Fast Pointer technique uses two pointers:

slow moves one node at a time
fast moves two nodes at a time

It is commonly used for:
Finding the middle of a linked list
Detecting a cycle
Finding the starting point of a cycle

Example: Below code Find Middle of Linked List
"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head):

    slow = head
    fast = head

    while fast is not None and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

    return slow

def runner():

    # Create linked list
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
  

    
    middle = find_middle(head)

    print("Middle Element:", middle.data)


runner()


"""
For Example

10=>20=>30=>40=>50

slow=fast=head (10)

1st iteration
slow = 20
fast = 30

2nd iteration
slow = 30
fast = 50


10=>20=>30=>40

slow=fast=head (10)

1st iteration
slow = 20
fast = 30

2nd iteration
slow = 30
fast = None
"""
