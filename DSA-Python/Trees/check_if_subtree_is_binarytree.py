
# https://www.youtube.com/watch?v=73PQ9raLEVs


'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should print the left view of the binary tree
# Note: You aren't required to print a new line after every test case


class Solution:
    def isIdentical(self,t1,t2):
        if t1 is None and t2 is None:
            return True 
        if t1 is None or t2 is None:
            return False
        if t1.data != t2.data:
            return False
        return self.isIdentical(t1.left,t2.left) and self.isIdentical(t1.right,t2.right)
    def isSubTree(self, T, S):
        # Code here
        if S is None:
            return True 
        if T is None:
            return False
        if self.isIdentical(T,S):
            return True
        return self.isSubTree(T.left,S) or self.isSubTree(T.right,S)
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
import sys
sys.setrecursionlimit(1000000)
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        rootT=buildTree(input())
        rootS=buildTree(input())
        if Solution().isSubTree(rootT, rootS) is True:
            print("1")
        else:
            print("0")
