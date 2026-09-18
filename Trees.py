# Trees starts with root node and consists of collection of subnodes in left or right positions, the connections between each nodes have arrow lines know as edges.
# Second to root node is parent node which contains two or more child nodes. At the end of the tree, all nodes are called Leaf node.
# Tree is non-linear data structure which maintains a hierarchy of parent and child.
# HTML DOM Type hierarchy is seen.
# All Nodes are indexed. 
# Level, height, depth, root, parent, child, edges, leaf node, ancestor, path, degree.
# Binary Trees can have only max of two childs for each node.
# Path taken to reach from particular parent to child = path.
# DEPTH = No of edges from root to node.
# Height = No of edges from the longest path from root to leaf node or any node to leaf node.
# Sussy Baka.
# Ancestor = Take a path from root to any node, the nodes which come inbetween excluding the selected node including root are ancestors.
# Descendent = Node which is a child node.
# Degree = The no of children a node has.(Binary tree = Degree = 2)
# Level = The root is Level 0 or 1, the descendents has next levels 2,3,.. for all sub trees existing.(Indexing each sub trees)
# Nyaaooooooo.....dwoooshdmdmdmdmdm.
# Tree = char, int, string as elements.


# Traversal :

# Edges can be only going downwards.
# 4 Types of Traversal : Breath First Search, Depth first Search
# BFS = in_order, pre_order, post_order.(Stack of Recursion)
# DFS = Level_order.(Queue)

# Every Recursion maintains it's own call stack.

# In_order : Left - Root - Right. (Like Infix Representation of operands and operators)
# Pre_order = Root - left - right.
# Post_Order = Left - Right  - Root.
# ADGMLA
# Level_Order = Left to Right with each levels. 


from collections import deque

class TreeNode:

    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def preorder(self,node):

        if node is None:
            return

        print(node.data,end = " ")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self,node):

        if node is None:
            return

        self.inorder(node.left)
        print(node.data,end = " ")
        self.inorder(node.right)

    def postorder(self,node):
    
            if node is None:
                return
    
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data,end = " ")

    def Level_order(self,node):
        
        if self.root is None:
             return

        queue = deque()
        queue.append(self.root)

        while queue:
             current = queue.popleft()
             print(current.data, end = " ")

             if current.left:
                queue.append(current.left)

             if current.right:
                queue.append(current.right)

    def count_node(self,node):
       
       if node is None:
            return 0


            return 1 + self.count_node(node.left) + self.count_node(node.right)

    def count_Leaf_node(self,node):

        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        return self.count_Leaf_node(node.left) + self.count_Leaf_node(node.right)

    def height(self,node):
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def depth(self,node):
        if node is None:
            return -1

        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)

        return 1 + max(left_depth, right_depth)

    def degree(self,node):
        if node is None:
            return 0

        left_degree = self.degree(node.left)
        right_degree = self.degree(node.right)

        return max(left_degree, right_degree) + (1 if node.left or node.right else 0)

    def ancestor(self,node, target):
        if node is None:
            return False

        if node.data == target:
            return True

        if self.ancestor(node.left, target) or self.ancestor(node.right, target):
            print(node.data, end = "->")
            return True

        return False

    def descendant(self,node, target):
        if node is None:
            return False

        if node.data == target:
            return True

        if self.descendant(node.left, target) or self.descendant(node.right, target):
            print(node.data, end = "->")
            return True

        return False

    def path(self,node, target):
        if node is None:
            return False

        if node.data == target:
            print(node.data, end = "->")
            return True

        if self.path(node.left, target) or self.path(node.right, target):
            print(node.data, end = "->")
            return True

        return False

    def is_leaf(self,node):
        if node is None:
            return False

        return node.left is None and node.right is None

    def is_ancestor(self,node, target):
        if node is None:
            return False

        if node.data == target:
            return True

        if self.is_ancestor(node.left, target) or self.is_ancestor(node.right, target):
            print(node.data, end = "->")
            return True

        return False

    def search(self,node, key):
        if node is None:
            return False

        if node.data == key:
            return True

        return self.search(node.left, key) or self.search(node.right, key)

tree = BinaryTree()

tree.root = TreeNode(10)

tree.root.left = TreeNode(5)
tree.root.right = TreeNode(20)

tree.root.left.left = TreeNode(3)    
tree.root.left.right = TreeNode(7)

tree.root.right.left = TreeNode(15)
tree.root.right.right = TreeNode(25)

tree.preorder(tree.root)
print("\n")
tree.postorder(tree.root)
print("\n")
tree.inorder(tree.root)
print("\n")
tree.Level_order(tree.root)
print("\n")
print("Number of nodes in the tree:", tree.count_node(tree.root))
print("\n")
print("Height of the tree:", tree.height(tree.root))
print("\n")
print("Depth of the tree:", tree.depth(tree.root))
print("\n")
print("Degree of the tree:", tree.degree(tree.root))
print("\n")
print("No of Leaf nodes:", tree.count_Leaf_node(tree.root))
print("\n")
print("Ancestors of node 7:")
tree.ancestor(tree.root, 7)
print("\n")
print("Descendants of node 7:")
tree.descendant(tree.root, 7)
print("\n")
print("Path from root to node 7:")
tree.path(tree.root, 7)
print("\n")
print("Search for node 15 in the tree:", tree.search(tree.root, 15))