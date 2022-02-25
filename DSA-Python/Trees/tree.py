class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self,node,data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node 
        
    def traverse_inorder(self,root): # first left and then root and then right
        if root is not None:
            self.traverse_inorder(root.left)
            print(root.data)
            self.traverse_inorder(root.right)

    def traverse_preorder(self,root): # first print root then left and right  = >Time complexity is O(N)
        if root is not None:
            print(root.data)
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)

    

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
print("Inorder traversal ----->")
tree.traverse_inorder(root)
