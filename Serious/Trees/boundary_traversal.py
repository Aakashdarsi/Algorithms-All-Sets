#https://www.youtube.com/watch?v=0nx-t0PcccA
# Combination of left boundary , right booundary and bottom boundary gives us the boundary traversal
class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None 

class Tree:
    def createNode(self,data):
        return Node(data)
    
    def insert(self,root,data):
        if root is None:
            return self.createNode(data)
        if data < root.data:
            root.left = self.insert(root.left,data)
        if data > root.data:
            root.right = self.insert(root.right,data)
        return root
    def left_boundary(self,root):
        if root is None:
            return
        if root.left is not None:
            print(root.data)
            self.left_boundary(root.left)
        elif root.right is not None:
            print(root.data)
            self.left_boundary(root.right)
    def leaves(self,root):
        if root is None:
            return 
        self.leaves(root.left)
        if root.left is None and root.right is None:
            print(root.data)
        self.leaves(root.right)
    def right_boundary(self,root):
        if root is None:
            return
        if root.right is not None:
            self.right_boundary(root.right)
            print(root.data)
        elif root.left is not None:
            self.right_boundary(root.left)
            print(root.data)
tree = Tree()
root = tree.createNode(5)
tree.insert(root,2)
tree.insert(root,6)
tree.insert(root,3)
tree.insert(root,8)
tree.left_boundary(root.left)
tree.leaves(root.left)
tree.leaves(root.right)
tree.right_boundary(root.right)


