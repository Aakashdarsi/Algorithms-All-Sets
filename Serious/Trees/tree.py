class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None
    
    def insert(self,data):
        if self.data is None:
            self.data = Node(data)
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
def inorder_print(r):
    if r is None:
        return 
    else:
        inorder_print(r.left)
        print(r.data,end = "->")
        inorder_print(r.right)

    
root = Node('g')
root.insert('a')
root.insert('c')
root.insert('b')
root.insert('d')
root.insert('e')
root.insert('f')
inorder_print(root)