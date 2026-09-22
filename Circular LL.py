# Circular LL 

class MyCircularLinkedList:

    # Node Definition
    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    # 1. Insert at Beginning
    def insert_at_beginning(self, data):

        new_node = self.Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    # 2. Display
    def display(self):

        if self.head is None:
            print("List Empty")
            return 

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break
        print("HEAD")

    # 4. Insert at End
    def insert_at_end(self, data):

        new_node = self.Node(data)

        if self.tail is None:
            self.head = self.tail = new_node
            self.tail.next = self.head #interview question difference between this and that
            
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node


    # 5. Insert at Position
    def insert_at_position(self, position, data):

        if position < 0:
            return

        if position == 0:
            self.insert_at_beginning(data)
            return

        if self.head is None:
            return

        temp = self.head
        size = 0

        while True:
            size += 1
            temp = temp.next
            if temp == self.head:
                break

        if position > size:
            return

        if position == size:
            self.insert_at_end(data)
            return

        temp = self.head
        for _ in range(position - 1):
            temp = temp.next

        new_node = self.Node(data)
        new_node.next = temp.next
        temp.next = new_node
##
    # 6. Delete Beginning
    def delete_beginning(self):

        if self.head is None:
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
    # 7. Delete End
    def delete_end(self):

        if self.tail is None:
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        previous = self.head
        while previous.next != self.tail:
            previous = previous.next

        self.tail = previous
        self.tail.next = self.head
    # 8. Delete Position
    def delete_position(self, position):

        if position < 0 or position >= self.size():
            return

        if position == 0:
            self.delete_beginning()
            return

        if position == self.size() - 1:
            self.delete_end()
            return

        previous = self.head
        for _ in range(position - 1):
            previous = previous.next

        previous.next = previous.next.next

    # 9. Search
    def search(self, value):

        if self.head is None:
            return False

        current = self.head
        while True:
            if current.data == value:
                return True

            current = current.next
            if current == self.head:
                break

        return False

    # 10. Get
    def get(self, position):

        if position < 0 or position >= self.size():
            raise Exception("Invalid Position")

        current = self.head
        for _ in range(position):
            current = current.next

        return current.data

    # 11. Size
    def size(self):

        if self.head is None:
            return 0

        count = 1
        current = self.head.next
        while current != self.head:
            count += 1
            current = current.next

        return count

    # 12. Is Empty
    def is_empty(self):
        return self.head is None

    # 13. Update
    def update(self, position, value):

        if position < 0 or position >= self.size():
            raise Exception("Invalid Position")

        current = self.head
        for _ in range(position):
            current = current.next

        current.data = value

    # 14. Reverse
    def reverse(self):

        if self.head is None or self.head == self.tail:
            return

        old_head = self.head
        previous = self.tail
        current = self.head

        while True:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

            if current == old_head:
                break

        self.tail = old_head
        self.head = previous


# --------------------------------------------------
# Runner Method
# --------------------------------------------------

def runner():

    linked_list = MyCircularLinkedList()

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)

    linked_list.insert_at_beginning(5)

    print("Forward:")
    linked_list.display()   

##    print("Backward:")
##    linked_list.display_backward()
##
##    print("\nAfter inserting 15 at position 2:")
##    linked_list.insert_at_position(2, 15)
##    linked_list.display_forward()
##
##    print("\nAfter deleting last element:")
##    linked_list.delete_end()
##    linked_list.display_forward()
##
##    print("\nAfter reversing:")
##    linked_list.reverse()
##    linked_list.display_forward()


# Program starts here
runner()
