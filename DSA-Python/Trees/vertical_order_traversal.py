# https://www.techiedelight.com/vertical-traversal-binary-tree/
#  Using level order traversal
# https://www.youtube.com/results?search_query=vertical+order+traversal+binary+tree

from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left  = None
        self.right = None 
class Tree:
    def createNode(self,data):
        return Node(data)
    
    def insert_node(self,data,root):
        if root is None:
            return self.createNode(data)
        if data < root.data:
            root.left = self.insert_node(data,root.left)
        if data > root.data:
            root.right = self.insert_node(data,root.right)
        return root
    def vertical_order_traversal(self,root):
        if root is None:
            return 
        queue = deque()
        d = {}
        queue.appendleft((root,0))
        while len(queue) != 0:
            node,hd = queue.pop()
            d.setdefault(hd,[]).append(node.data)
            if node.left is not None:
                queue.append((node.left,hd-1))
            if node.right is not None:
                queue.append((node.right,hd+1))
        print(d)
root  = Node(2)
tree = Tree()
tree.insert_node(1,root)
tree.insert_node(-1,root)
tree.insert_node(3,root)
# tree.insert_node(6,root)
# tree.insert_node(7,root)
# tree.insert_node(8,root)
# tree.insert_node(9,root)
# tree.insert_node(10,root)
tree.vertical_order_traversal(root)