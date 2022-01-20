from email import header
from select import select


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class LinkedList:
    def __init__(self):
        self.head = None 

def check_loop(head):
    q = head
    p = head
    while q and q.next:
        p = p.next 
        q = q.next
        if p == q:
            return p 
    else:
        return None 

def loop_point(p,head):# p is that point where p becomes equal to q
    q = head 
    while p != q:
        p = p.next 
        q = q.next 
    return p 

  