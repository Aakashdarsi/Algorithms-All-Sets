



from platform import node


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
class LinkedList:
    def __init__(self):
        self.head = None 
    def lenght(self):
        if self.head is None:
            return 0 
        else:
            l = 1 
            temp = self.head 
            while temp.next is not None:
                temp = temp.next
                l = 1 
            return l
    
    def insert_begin(self,data): # check is head pointer is none then initialise the head pointer to current node
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else: # new node should point to the head node
            new_node.next = self.head  
            self.head = new_node # then head node is maintained as new node which we created

    def insert_position(self,data,pos):
        
        if self.head is None:
            print("cannot insert at given position")
            return
        

        
        else:
            new_node = Node(data)
            cp = 1 
            temp = self.head 
            while cp != pos:
                temp = temp.next
                cp += 1 
            cpa = temp.next 
            temp.next = new_node
            new_node.next = cpa 



    def insert_end(self,data):
        #we got the linked list last position we directly link the new node to the last node we get
        temp = self.head 
        if temp is None:
            self.head  = Node(data)
        else:
            nnode = Node(data)
            while temp.next is not None:
                temp = temp.next 
            temp.next = nnode
            nnode.next = None 
    
    def display(self):
        temp = self.head 
        while temp is not None:
            print(temp.data,end="->")
            temp = temp.next 

    def delete_start(self):
        q = self.head 
        p = self.head.next 
        self.head = p 
        del q 
    def delete_data(self,data):
         q = self.head 
         p = self.head.next
         while p.data != data :
             p = p.next
             q = q.next
         if p.next is None:
             q.next = None 
             del p 
         else:
             q.next = p.next 
             del p 
            

        




   
        

Llist = LinkedList()
n1 = 5
n2 = 6
n3  = 7
Llist.insert_begin(n1)
Llist.insert_begin(n2)
Llist.insert_begin(n3)
Llist.insert_position(22,2)
Llist.insert_end(56)
Llist.display()
Llist.delete_start()
print()
Llist.display()
Llist.delete_data(56)
print()
Llist.display()
Llist.delete_data(22)
print()
Llist.display()