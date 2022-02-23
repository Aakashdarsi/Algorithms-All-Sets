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

    def diameter_binary_tree(self,root):
        if root is None:
            return 0 
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        l_diameter = self.diameter_binary_tree(root.left)
        r_diameter = self.diameter_binary_tree(root.right)
        return max((lheight+rheight+1,max(l_diameter,r_diameter)))

tree = Tree()
root = tree.createNode(5)
tree.insert(root,2)
tree.insert(root,6)
tree.insert(root,3)
tree.insert(root,8)
print(tree.diameter_binary_tree(root))