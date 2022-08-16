from typing import *
from queue import Queue
# 225. Implement Stack using Queues
# Implement a last-in-first-out(LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack(push, top, pop, and empty).
# Implement the MyStack class:
#     void push(int x) Pushes element x to the top of the stack.
#     int pop() Removes the element on the top of the stack and returns it.
#     int top() Returns the element on the top of the stack.
#     boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:
#     You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
#     Depending on your language, the queue may not be supported natively.
#     You may simulate a queue using a list or deque(double-ended queue) as long as you use only a queue's standard operations.

# List-Based Queue
class ListBasedQueue:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for i in range(len(self.queue)-1):
            self.push(self.queue.pop(0))
        return self.queue.pop(0)

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0

# Strict Queue
class StrictQueue:
    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.put(x)

    def pop(self) -> int:
        for i in range(self.queue.qsize()-1):
            self.queue.put(self.queue.get())
        return self.queue.get()

    def top(self) -> int:
        for i in range(self.queue.qsize()-1):
            self.queue.put(self.queue.get())
        result = self.queue.get()
        self.queue.put(result)
        return result

    def empty(self) -> bool:
        return self.queue.empty()
