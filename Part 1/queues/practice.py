# Use two stacks to implement a queue data structure and write functions for enqueue and dequeue operations.
class Queue:
    def __init__(self):
        self.instack = []
        self.outstack = []

    def is_empty(self):
        return len(self.instack) == 0 and len(self.outstack) == 0

    def enqueue(self, item):
        self.instack.append(item)

    def dequeue(self):
        if self.is_empty(): return None
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
    
    def peek(self):
        if self.is_empty(): return None
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]

# Reversing a Queue
# def reverse(queue):
#     stack = []
#     while queue:
#         stack.append(queue.popleft())
#     while stack:
#         queue.append(stack.pop())
#     return queue

def reverse(queue):
    if len(queue) == 0:
        return queue
    pop_item = queue.popleft()
    reverse(queue).append(pop_item)
    return queue


from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)
print(reverse(queue))