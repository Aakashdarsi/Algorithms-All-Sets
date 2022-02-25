from collections import deque



class Queue:
    def __init__(self):
        self.queue = deque()
    
    def insert(self,data):
        self.queue.appendleft(data)

    def pop(self):
        self.queue.pop()

    def display(self):
        print(self.queue)
    
    def length(self):
        print(len(self.queue))

x = Queue()
x.insert(22)
x.insert(33)
x.insert(44)
x.display()
x.pop()
x.display()