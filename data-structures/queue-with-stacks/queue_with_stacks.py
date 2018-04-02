# from node import Node


class Queue(val):
    """ class for Queue """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    """ implement stacks with push and pop function create empty stacks """
    """ implement enqueue method by using only stacks """
    def enqueue(self, ele):
        self.stack1.append(ele)
    """ implement dequeue method by pushing all elements from stack 1 into
     stack 2, which reverses the order and then popping from stack 2 """
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
