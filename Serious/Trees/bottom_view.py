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
    def get_vertical_order(self,root,hd,d):
        if root is None:
            return
        try:
            d[hd].append(root.data)
        except:
            d[hd] = [root.data]
        self.get_vertical_order(root.left,hd-1,d)
        self.get_vertical_order(root.right,hd+1,d)
    def bottom_view(self,root):
        hd = 0 
        d = {}
        self.get_vertical_order(root,hd,d)
        for i in sorted(d):
            print((d[i])[-1],end='->')
tree = Tree()
root = tree.createNode(5)
tree.insert(root,2)
tree.insert(root,6)
tree.insert(root,3)
tree.insert(root,8)
tree.bottom_view(root)
