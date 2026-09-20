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
##    # 6. Delete Beginning
##    def delete_beginning(self):
##
##        if self.head is None:
##            return
##
##        if self.head == self.tail:
##            self.head = self.tail = None
##        else:
##            self.head = self.head.next
##            self.head.prev = None
##
##        self._size -= 1
##
##    # 7. Delete End
##    def delete_end(self):
##
##        if self.tail is None:
##            return
##
##        if self.head == self.tail:
##            self.head = self.tail = None
##        else:
##            self.tail = self.tail.prev
##            self.tail.next = None
##
##        self._size -= 1
##
##    # 8. Delete Position
##    def delete_position(self, position):
##
##        if position < 0 or position >= self._size:
##            return
##
##        if position == 0:
##            self.delete_beginning()
##            return
##
##        if position == self._size - 1:
##            self.delete_end()
##            return
##
##        temp = self.head
##
##        for i in range(position):
##            temp = temp.next
##
##        temp.prev.next = temp.next
##        temp.next.prev = temp.prev
##
##        self._size -= 1
##
##    # 9. Search
##    def search(self, value):
##
##        temp = self.head
##
##        while temp is not None:
##
##            if temp.data == value:
##                return True
##
##            temp = temp.next
##
##        return False
##
##    # 10. Get
##    def get(self, position):
##
##        if position < 0 or position >= self._size:
##            raise Exception("Invalid Position")
##
##        temp = self.head
##
##        for i in range(position):
##            temp = temp.next
##
##        return temp.data
##
##    # 11. Size
##    def size(self):
##        return self._size
##
##    # 12. Is Empty
##    def is_empty(self):
##        return self._size == 0
##
##    # 13. Update
##    def update(self, position, value):
##
##        if position < 0 or position >= self._size:
##            raise Exception("Invalid Position")
##
##        temp = self.head
##
##        for i in range(position):
##            temp = temp.next
##
##        temp.data = value
##
##    # 14. Reverse
##    def reverse(self):
##
##        current = self.head
##        temp = None
##
##        while current is not None:
##
##            # Swap prev and next
##            temp = current.prev
##            current.prev = current.next
##            current.next = temp
##
##            # Move to next node
##            current = current.prev
##
##        # Swap head and tail
##        temp = self.head
##        self.head = self.tail
##        self.tail = temp


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
