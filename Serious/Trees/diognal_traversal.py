#https://www.youtube.com/watch?v=e9ZGxH1y_PE&t=495s
class Node:
  def __init__(self,data):
    self.left = None
    self.data = data 
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
  def diognal_traversal(self,root,m,dd):
      if root is None:
          return 
      try:
            m[dd].append(root.data)
      except:
            m[dd] = [root.data]
      self.diognal_traversal(root.left,m,dd+1)
      self.diognal_traversal(root.right,m,dd)
  
  def print_diag(self,root):
      dd = 0 
      m = dict()
      self.diognal_traversal(root,m,dd)
      print(m)

tree = Tree()
root = tree.createNode(5)
tree.insert(root,2)
tree.insert(root,6)
tree.insert(root,3)
tree.insert(root,8)
tree.print_diag(root)
        
