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
  
  def getVerticalOrder(self,root,m,hd):
    if root is None:
      return 
    try:
      m[hd].append(root.data)
    except:
      m[hd] = [root.data]
    self.getVerticalOrder(root.left,m,hd-1)
    self.getVerticalOrder(root.right,m,hd+1)


  def printVerticalorder(self,root):
    m = dict()
    hd = 0 
    self.getVerticalOrder(root,m,hd)
    for i in sorted(m):
      print(str(i)+"->"+str(m[i]))
tree = Tree()
root = tree.createNode(5)
tree.insert(root,2)
tree.insert(root,6)
tree.insert(root,3)
tree.insert(root,8)

tree.printVerticalorder(root)
