# Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Delete d nodes from end
    def delete_from_end(self, d):
        # Step 1: Count total nodes
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next

        # Step 2: If d >= length, delete entire list
        if d >= length:
            self.head = None
            return

        # Step 3: Traverse to (length - d - 1)th node
        temp = self.head
        for _ in range(length - d - 1):
            temp = temp.next

        # Step 4: Cut off last d nodes
        temp.next = None

    # Display linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Driver code
n_and_values = list(map(int, input().split()))
n = n_and_values[0]
values = n_and_values[1:n+1]
d = n_and_values[n+1]

ll = LinkedList()
for val in values:
    ll.insert_at_end(val)

ll.delete_from_end(d)
ll.display()
