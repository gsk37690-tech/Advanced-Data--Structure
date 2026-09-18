class MyLinkList:

    #Node definition
    class Node:

        def __init__(self,data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    #display
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end="->")
            temp = temp.next

        print("NULL")

    def insert_at_beginning(self,data):

        new_node = self.Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self._size += 1

    #insert at the end
    def insert_at_end(self,data):
        new_node = self.Node(data)

        if self.head is None:

            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    #size
    def size(self):
        return self._size

    #insert at position
    def insert_at_position(self,data,position):

        if position< 0 or position > self._size:
            print("Invalid position")
            return
        
        if position == 0:
            self.insert_at_beginning(data)
            return

        if position == self._size:
            self.insert_at_end(data)
            return

        new_node = self.Node(data)

        temp = self.head

        for i in range(position - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    #search by value
    def search(self,data):

        temp = self.head

        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next

        return False

    #Get element by the position.
    def get(self,position):

        if position< 0 or position >= self._size:
            print("Invalid position")
            return None

        temp = self.head

        for i in range(position):
            temp = temp.next

        return temp.data

    #update
    def update(self,position,value):

        if position < 0 or position >= self.size():
            print("Invalid position.")
            return None

        temp = self.head

        for i in range(position - 1):
            temp = temp.next

        temp.data = value

    #reverse
    def reverse(self):

        prev = None
        current = self.head

        self.tail = self.head 

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    #delete at the beginning
    def delete_at_beginning(self):

        if self.head is None:
            print("List is empty.")
            return

        self.head = self.head.next
        self._size -= 1

    #delete at the end
    def delete_at_end(self):

        if self.head is None:
            print("List is empty.")
            return

        if self.head == self.tail:
            self.head = self.tail = None
            self._size -= 1
            return

        temp = self.head

        while temp.next != self.tail:
            temp = temp.next

        temp.next = None
        self.tail = temp
        self._size -= 1

    #delete by position
    def delete(self,position):

        if position < 0 or position >= self._size:
            print("Invalid position.")
            return

        if position == 0:
            self.delete_at_beginning()
            return

        if position == self._size - 1:
            self.delete_at_end()
            return

        temp = self.head

        for i in range(position - 1):
            temp = temp.next

        temp.next = temp.next.next
        self._size -= 1
    #print first element
    def first_element(data):
        if self.head is None:
            print("List is empty.")
            return None
        return self.head.data

    #print last element
    def last_element(data):
        if self.tail is None:
            print("List is empty.")
            return None
        return self.tail.data

    #print by position
    def element_at_position(data,position):
        if position < 0 or position >= self._size:
            print("Invalid position.")
            return None

        temp = self.head

        for i in range(position):
            temp = temp.next

        return temp.data

    #


def runner():

    linked_list = MyLinkList()

    print("1.Insert at beginning.")
    linked_list.insert_at_beginning(30)
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_beginning(10)

    linked_list.display()

    print("\n2.Insert at the end.")

    linked_list.insert_at_end(40)
    linked_list.insert_at_end(50)

    linked_list.display()

    print("\n3.Insert 35 at position 3: ")
    linked_list.insert_at_position(35,3)

    linked_list.display()

    print("\n4.Size of the linked list:",linked_list.size())

    print("\n5.Search.")
    print("Search 30:", linked_list.search(30))
    print("Search 100:", linked_list.search(100))

    print("\n6.Get element by position:")
    print("Element at position 2:", linked_list.get(2))

    print("\n7.Update element at position 2 to 99.",linked_list.update(2,99))
    linked_list.display()

    print("\n8.Delete at beginning.")
    linked_list.delete_at_beginning()
    linked_list.display()

    print("\n9.Delete at end.")
    linked_list.delete_at_end()
    linked_list.display()

    print("\n10.Delete element at position 2.")
    linked_list.delete(2)
    linked_list.display()

    print("\n11.Reverse the linked list.")
    linked_list.reverse()
    linked_list.display()

    print("\n12.First element:", linked_list.first_element())

    print("13.Last element:", linked_list.last_element())

    print("14.Element at position 4:", linked_list.element_at_position(4))

    print("\n15.Size of the linked list:",linked_list.size())



runner()

# _ is used for protected.
# __ is used for private.
# self is considered as a pointer to the current object.
# while using self we need to use (.) to access the attributes and methods of the class.
# static methods are used to create utility functions. They don't have access to self or cls. They are restricted in what data they can access - and are primarily a way to namespace your methods.
# runner() is a function not a method of the class. It is used to run the code and test the functionality of the class.
# Methods are functions that are defined inside a class and are used to perform operations on the objects of that class. 
# They can access and modify the attributes of the class. Methods can be called only with the subject of the class. 
# They are used to define the behavior of the objects of the class.
# self.head and self.next are both pointers while self.data holds the data of the node.
# 
