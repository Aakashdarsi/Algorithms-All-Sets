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

    def identical(self,root1,root2):
        if root1 is None and root2 is None:
            return False
        if root1 is not None and root2 is not None:
            return root1.data==root2.data and self.identical(root1.left,root2.right) and self.identical(root1.right,root2.right)