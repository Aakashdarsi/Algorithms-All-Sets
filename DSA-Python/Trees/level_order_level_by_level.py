from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None 
class Tree:
    def create(self,data):
        return Node(data)
    
    def insert(self,root,data):
        if root is None:
            return self.create(data)
        if data < root.data :
            root.left = self.insert(root.left,data)
        if data > root.data:
            root.right = self.insert(root.right,data)
        return root
    def preorder(self,root):
        if root is None:
            return 
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
    
    def level_order(self,root):
        if root is None:
            return 
        queue = deque()
        queue.appendleft(root)
        queue.appendleft(None)
        while len(queue) != 0:
            node = queue.pop() # append None with root . If we found None that means we successfully completed one level
            if node is  None: # print new line then . After that check whether queue is non empty then enqueue None
                print()
                if len(queue)!=0:
                    queue.appendleft(None)
            else:
                print(node.data,end = " ")
                if node.left is not None:
                    queue.appendleft(node.left)
                if node.right is not None:
                    queue.appendleft(node.right)
    
tree = Tree()
root = tree.create(5)
tree.insert(root,2)
tree.insert(root,6)
tree.level_order(root)