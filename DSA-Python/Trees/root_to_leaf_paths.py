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
    def printArray(self,s,path_len):
        for i in range(path_len):
            print(s[i],' ',end="")
        print()

    def printpaths(self,root,s,path_len):
        if root is None:
            return 
        if len(s) > path_len:
            s[path_len] = root.data 
        else:
            s.append(root.data)
        if root.left is None and root.right is None:
            self.printArray(s,path_len)
        else:
            self.printpaths(root.left,s,path_len)
            self.printpaths(root.right,s,path_len)
    

    def root_to_leaf(self,root):
        s = deque()
        self.printpaths(root,s,0)
tree = Tree()
root = tree.createNode(5)
tree.insert(root,2)
tree.insert(root,6)
tree.insert(root,3)
tree.insert(root,8)
tree.root_to_leaf(root)