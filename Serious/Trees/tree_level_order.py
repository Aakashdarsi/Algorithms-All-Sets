from collections import deque


class Node:
    def __init__(self, data):
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
        if data >  root.data:
            root.right = self.insert(root.right,data)
        return root 

    def level_order(self,root): #printing level by level from left to right
        queue = deque()
        queue.appendleft(root)
        while len(queue) != 0:
            node = queue.pop()
            print(node.data,end="->")
            if node.left is not None:
                queue.appendleft(node.left)
            if node.right is not None:
                queue.append(node.right)
    
    def level_order_right_to_left(self,root):
        queue = deque()
        queue.appendleft(root)
        while len(queue) != 0 :
            node = queue.pop()
            print(node.data,end='->')
            if node.right is  not None:
                queue.appendleft(node.right)
            
            if node.left is not None:
                queue.appendleft(node.left)

    def level_order_bottom_left_to_right(self,root):
        if root is None:
            return 
        stack = deque()
        queue = deque()
        queue.appendleft(root)
        while len(queue) !=0:
            node = queue.pop()
            stack.append(node.data)
            if node.left is not None:
                queue.appendleft(node.left)
            if node.right is not None:
                stack.appendleft(node.right)
        for i in range(len(stack)):
            print(stack.pop(),end="->")
        


            
            


tree = Tree()
root = tree.createNode(1)
l = [2,10,7,15,12,20,30,6,8]
tree.insert(root,2)
tree.insert(root,3)
tree.insert(root,4)
tree.insert(root,5)
tree.insert(root,6)
print("Level order traversal --->")
tree.level_order(root)
print("Level order traversal from top right to left:")
tree.level_order_right_to_left(root)
tree.level_order_bottom_left_to_right(root)