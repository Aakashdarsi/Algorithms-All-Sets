# https://www.youtube.com/watch?v=XuMmc-WstpI
'''
class ListNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


# Tree Node structure
class Tree:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''

#Function to make binary tree from linked list.
def convert(head):
  
    # code here
    a = []
    t = head 
    while t is not None:
        a.append(Tree(t.data)) # This is a
        t = t.next 
    n = len(a)
    for i in range(n//2):
        if 2*i+1 < n:
            a[i].left = a[2*i+1]
        if 2*i+2 < n:
            a[i].right = a[2*i+2]
    return a[0]


