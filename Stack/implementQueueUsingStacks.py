from typing import *
from queue import LifoQueue
# 232. Implement Queue using Stacks
# Implement a First In First Out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
# Implement the MyQueue class:
#     void push(int x) Pushes element x to the back of the queue.
#     int pop() Removes the element from the front of the queue and returns it.
#     int peek() Returns the element at the front of the queue.
#     boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:
#     You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
#     Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

class MyQueue:
    def __init__(self):
        self.stack1, self.stack2 = LifoQueue(), LifoQueue()
    
    def push(self, x: int) -> None:
        self.stack1.put(x)

    def pop(self) -> int:
        while not self.stack1.empty():
                self.stack2.put(self.stack1.get())
        result = self.stack2.get()
        while not self.stack2.empty():
            self.stack1.put(self.stack2.get())
        return result

    def peek(self) -> int:
        while not self.stack1.empty():
                self.stack2.put(self.stack1.get())
        result = self.stack2.get()
        self.stack2.put(result)
        while not self.stack2.empty():
            self.stack1.put(self.stack2.get())
        return result

    def empty(self) -> bool:
        return self.stack1.empty()
