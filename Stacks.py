class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    def display(self):
        print(self.stack)

def runner():
    s = Stack()
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Is Empty")
        print("5. Size")
        print("6. Display")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            value = int(input("Enter value to push: "))
            s.push(value)
        elif choice == 2:
            try:
                print("Popped value:", s.pop())
            except IndexError as e:
                print(e)
        elif choice == 3:
            try:
                print("Top value:", s.peek())
            except IndexError as e:
                print(e)
        elif choice == 4:
            print("Is stack empty?", s.is_empty())
        elif choice == 5:
            print("Stack size:", s.size())
        elif choice == 6:
            s.display()
        elif choice == 7:
            break
        else:
            print("Invalid choice, please try again.")

runner()
