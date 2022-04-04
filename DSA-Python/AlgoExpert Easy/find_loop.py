# Find a loop in linked list 
# Node at which loop originates
# Approach 1 
# check whether the element is slready traversed in hash table if already traversed than that is the elenent where the traversing is happening
def loop(head):
    p = head 
    d = {}
    while p is not None:
        if p.data in d.keys():
            return p.data 
        else:
            d[p.data] = True 
        p = p.next 
    