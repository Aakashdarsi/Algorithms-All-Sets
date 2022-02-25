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
        if data <root.data:
            root.left = self.insert(root.left,data)
        if data > root.data:
            root.right = self.insert(root.right,data)
        return root
    def get_levels(self,root,d,l):
        if root is None:
            return
        try:
            d[l].append(root.data)
        except:
            d[l]  = [root.data]
        self.get_levels(root.left,d,l+1)
        self.get_levels(root.right,d,l+1)

    def level_by_level_left(self,root):
        d = {}
        l = 1
        self.get_levels(root,d,l)
        for i in sorted(d):
            print((d[i])[0],end="->")

tree = Tree()
root = tree.createNode(5)
tree.insert(root,2)
tree.insert(root,6)
tree.insert(root,3)
tree.insert(root,8)
tree.level_by_level_left(root)
            
        