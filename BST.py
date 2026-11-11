class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return Node(value)
        else:
            if value < root.value:
                root.left = self.insert(root.left, value)
            else:
                root.right = self.insert(root.right, value)
        return root

    def add(self, value):
        self.insert(self.root, value)

    def search(self, root, value):
        if root is None:
            return False
        if root.value == value:
            return True
        if value < root.value:
            return self.search(root.left, value)
        return self.search(root.right, value)

    def preorder(self, root):
        if root is None:
            return 
        
        print(root.value, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.value, end=" ")
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value, end=" ")


#if __name__ == "__main__":
    
tree = BST()

values = [50,30,70,20,40,60,80]

for v in values:
    tree.add(v)

print("BST Created Successfully")

print()

key = 60
if tree.search(tree.root, key):
    print("Element found")
else:
    print("Element not found")

tree.preorder(tree.root)
print()
tree.inorder(tree.root)
print()
tree.postorder(tree.root)
