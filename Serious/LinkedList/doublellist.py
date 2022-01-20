class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None 
        self.next = None 
    
class doubleLlist:
    def __init__(self):
        self.head = None 
    
    def insert_start(self,data):
        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.prev = None 
            self.head.next = None 
        else:
            self.head.prev = new_node
            new_node.next = self.head 
        
            new_node.prev = None
            self.head = new_node
    
    def insert_pos(self,data,pos):
        new_node = Node(data)
        if self.head is None:
            print("Can't be inserted ......")
            return
        else:
            c = 1 
            t = self.head 
            while  c != pos:
                t = t.next
                c +=1 
            new_node.next = t.next 
            new_node.prev = t 
            t.next = new_node
            


        
    def display(self):
        t = self.head 
        
        
        while t.next is not None:
                print(t.data,end="->")
                t = t.next
        print()

n1 = 2 
n2 = 3 
dlist = doubleLlist()
dlist.insert_start(000)
dlist.insert_start(n2)
dlist.insert_start(22)
dlist.insert_start(34)
dlist.display()
dlist.insert_pos(56,2)
print()
dlist.display()