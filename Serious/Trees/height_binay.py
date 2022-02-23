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
    def height(self,root): # height indicates the number of nodes present in betweeen from ground level to root !!!!! 
        h = 0 # let initial height is zero
        if root is None: # check for the root whether it is None
            return 0
        l = self.height(root.left) # Check height of left subtree
        r = self.height(root.right) # check height of right sub tree
        if l > r: # if height of left subtree is greater than right subtree
            h = 1 + l
        else: 
            h = 1 +r 
        return h
tree = Tree()
root = tree.createNode(5)
l = [2,10,7,15,12,20,30,6,8]
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7)
tree.insert(root,15)
tree.insert(root,12)
tree.insert(root,20)
tree.insert(root,30)
tree.insert(root,6)
tree.insert(root,8)
print(tree.height(root))

