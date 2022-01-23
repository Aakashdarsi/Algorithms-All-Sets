from collections import deque
class Node:
  def __init__(self,data):
    self.left = None
    self.right = None
    self.data = data 

class Tree:
  def create_node(self,data):
    return Node(data)
  def insert_node(self,data,root):
    if root is None:
      return self.create_node(data)
    if data < root.data:
      root.left = self.insert_node(data,root.left)
    if data > root.data:
      root.right = self.insert_node(data,root.right)
    return root
  def traverse_spiral(self,root):
    if root is None:
      return 
    stk_1 = deque()
    stk_2 = deque()
    stk_1.append(root)
    while len(stk_1) != 0:
      node = stk_1.pop()
      print(node.data)
      if node.left is not None:
        stk_2.append(node.left)
      if node.right is not None:
        stk_2.append(node.right)
      while len(stk_2) != 0:
        node = stk_2.pop()
        print(node.data)
        if node.right is not None:
          stk_1.append(node.right)
        if node.left is not None:
          stk_1.append(node.left)
tree = Tree()
root = tree.create_node(5)
tree.insert_node(2,root)
tree.insert_node(6,root)
tree.insert_node(4,root)
tree.insert_node(8,root)
tree.insert_node(1,root) 
tree.traverse_spiral(root)