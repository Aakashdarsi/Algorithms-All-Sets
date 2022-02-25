class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class CLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_start(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.next = new_node 

            self.head = new_node 
    def insert_pos(self,data,pos):
        length = 0
        if self.head is None:
            length = 0 
        else:
            
            p = self.head.next
            length = 1 
            while p.next is not self.head:
                length += 1
                p = p.next 
        if pos > length: 
            print("You cannot insert at that position")
            return 
        elif pos <=len:
            p = self.head
            c = 0
            while p.next is not self.head:
                if c == p:
                    new_node = Node(data)
                    new_node.next = p.next
                    p.next = new_node 
                    return 
                p = p.next 
        else:
            p = self.head.next 
            while p.next is not self.head:
                p = p.next 
            new_node =Node(data)
            new_node.next = p.next 
            p.next = new_node 
    
     



