#Find the Survivor

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):

        new_node = self.Node(data)

        if self.tail is None:
            self.head = self.tail = new_node
            self.tail.next = self.head #interview question difference between this and that
            
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

def josephus(n,k):

    circular_list = CircularLL()

    for i in range(1,n+1):
        circular_list.insert_at_end(i)

        current = circular_list.head
        previous = circular_list.tail

        while current.next != current :
            for i in range(k-1):
                previous = current
                current = current.next
            print("Removed :",current.data)

            previous.next = current.next

            current = current.next
            
        return current.data

def runner():
    n = 7  # Total number of people (1 through 7)
    k = 3  # Eliminate every 3rd person

    print(f"Running Josephus Problem for n = {n}, k = {k}:")
    survivor = CircularLL.josephus(n, k)
    print(f"Survivor is: {survivor}")

    runner()

"""
The Josephus Problem is a classic circular linked-list problem.

Problem
Suppose N people are standing in a circle.
Starting from the first person, eliminate every Kth person.
Continue until only one person remains.

Josephus is an excellent example where a Circular Linked List + pointer movement + deletion 
all come together.

Find the survivor
Leetcode: 1823 - Find the winner of the Circular Game
Leetcode: 390 - Elimination Game

"""