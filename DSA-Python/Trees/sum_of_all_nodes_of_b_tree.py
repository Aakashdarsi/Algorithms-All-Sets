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
    def sum_of_all_nodes(self,root):
        if root is None:
            return 0
        return root.data + self.sum_of_all_nodes(root.left)+self.sum_of_all_nodes(root.right)
tree = Tree()
root = tree.createNode(5)
tree.insert(root,2)
tree.insert(root,6)
tree.insert(root,3)
print(tree.sum_of_all_nodes(root))