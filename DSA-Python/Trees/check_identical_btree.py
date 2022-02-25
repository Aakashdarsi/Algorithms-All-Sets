# https://www.youtube.com/watch?v=kL5Gs1YTwMM # Used to check if two binary trees are identical or not
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
def check_identical(self,root1,root2):
    if root1 is None and root2 is None:
        return True 
    if root1 is not None and root2 is not None and root1.data == root2.data :
        l = self.check_identical(root1.left,root2.left)
        r = self.check_identical(root1.right,root2.right)
        if l&r:
            return True 
        return False 
    return False 
