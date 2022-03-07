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
    
    def height(self,root):
        if root is None:
            return 0
        return max(self.height(root.left),self.height(root.right))+1
                
root = Node(5)
tree = Tree()
tree.insert_node(2,root)
tree.insert_node(6,root)
tree.insert_node(1,root)
tree.insert_node(3,root)
tree.insert_node(7,root)
print(tree.height(root))
    
            
    