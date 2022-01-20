from collections import deque
from inspect import stack
class Stack:
    def __init__(self):
        self.stack = deque()
    
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        self.stack.pop()

    def length_of_stack(self):
        print(len(self.stack))
    
    def display(self):
        print(self.stack)

   

x = Stack()
x.push(22)
x.push(33)
x.push(44)
x.length_of_stack()
x.display()
