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
    def height(self,root):
        if root is None:
            return 0 
        return 1 + max(self.height(root.left),self.height(root.right))

    def isBalanced(self,root):
        if root is None:
            return True 
        l_height = self.height(root.left)
        r_height = self.height(root.right)
        if abs(l_height-r_height) <= 1:
            return True 
        else:
            return False
tree = Tree()
root = tree.createNode(5)
tree.insert(root,2)
tree.insert(root,6)
tree.insert(root,3)
tree.insert(root,8)
tree.insert(root,10)
tree.insert(root,25)
print(tree.isBalanced(root))