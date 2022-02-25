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
            self.insert(root.left,data)
        else:
            self.insert(root.right,data)
        
    def traverse_pre_iterative(self,root):
        s = deque()
        s.append(root)
        while len(s) != 0:
            node = s.pop()
            print(node.data)
            s.append(node.right)
            s.append(node.left)


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
tree.traverse_pre_iterative(root)
