from collections import deque


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
    def iterative_preorder(self,root):
        if root is None:
            return
        stack = deque()
        stack.append(root)
        while len(stack) != 0:
            node = stack.pop()
            print(node.data)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
tree = Tree()
root = tree.createNode(5)
tree.insert(root,2)
tree.insert(root,6)
tree.insert(root,3)
tree.iterative_preorder(root)