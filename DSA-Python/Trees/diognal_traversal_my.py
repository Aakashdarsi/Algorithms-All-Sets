#based on level order
from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left  = None
        self.right = None 
class Tree:
    def createNode(self,data):
        return Node(data)
    
    def insert_node(self,data,root):
        if root is None:
            return self.createNode(data)
        if data < root.data:
            root.left = self.insert_node(data,root.left)
        if data > root.data:
            root.right = self.insert_node(data,root.right)
        return root
    
    def diognal_traversal(self,root):
        if root is None:
            return
        queue = deque()
        hd = 0
        queue.appendleft((root,hd))
        d = {}
        while len(queue) != 0:
            node,hd = queue.pop()
            d.setdefault(hd,[]).append(node.data)
            if node.left is not None:
                queue.appendleft((node.left,hd+1))
            if node.right is not None:
                queue.appendleft((node.right,hd))
        print(d)
                
root = Node(5)
tree = Tree()
tree.insert_node(2,root)
tree.insert_node(6,root)
tree.insert_node(1,root)
tree.insert_node(3,root)
tree.insert_node(7,root)
tree.diognal_traversal(root)
    
            
    